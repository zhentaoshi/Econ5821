"""Compare Local Projection and VAR impulse response estimates by simulation."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
from statsmodels.tsa.api import VAR


@dataclass(frozen=True)
class DGPParams:
    """Parameters for a stable bivariate structural VAR(1) data generating process."""

    A: np.ndarray
    B: np.ndarray


@dataclass(frozen=True)
class IRFSummary:
    """Pointwise Monte Carlo summary for one estimation method."""

    mean: np.ndarray
    lower: np.ndarray
    upper: np.ndarray


@dataclass(frozen=True)
class SimulationResults:
    """Container for true and estimated impulse response functions."""

    horizons: np.ndarray
    true_irf: np.ndarray
    lp: IRFSummary
    var: IRFSummary


def default_dgp_params() -> DGPParams:
    """Return a stable bivariate DGP."""
    A = np.array([[0.55, 0.15], [-0.10, 0.45]])
    B = np.array([[1.00, 0.00], [0.35, 0.90]])
    return DGPParams(A=A, B=B)


def simulate_dgp(
    T: int,
    burn: int,
    params: DGPParams,
    rng: np.random.Generator,
) -> tuple[np.ndarray, np.ndarray]:
    """Simulate y_t = A y_{t-1} + B e_t, with e_t ~ N(0, I)."""
    total = T + burn
    n_vars = params.A.shape[0]
    y = np.zeros((total, n_vars))
    eps = rng.standard_normal((total, n_vars))

    for t in range(1, total):
        y[t] = params.A @ y[t - 1] + params.B @ eps[t]

    return y[burn:], eps[burn:]


def true_irf(params: DGPParams, horizon: int, shock_index: int = 0) -> np.ndarray:
    """Compute the true structural IRF to one shock for horizons 0..H."""
    n_vars = params.A.shape[0]
    out = np.zeros((horizon + 1, n_vars))
    shock_vector = params.B[:, shock_index]
    for h in range(horizon + 1):
        out[h] = np.linalg.matrix_power(params.A, h) @ shock_vector
    return out


def estimate_lp_irf(
    y: np.ndarray,
    shock: np.ndarray,
    horizon: int,
    p: int = 1,
) -> np.ndarray:
    """
    Estimate local projection IRFs for all responses.

    The LP regression at horizon h is:
    y_{t+h} = alpha_h + beta_h * shock_t + Gamma_h(L) y_{t-1} + u_{t+h}
    """
    T, n_vars = y.shape
    out = np.zeros((horizon + 1, n_vars))
    start = p

    for h in range(horizon + 1):
        stop = T - h
        if stop <= start:
            raise ValueError("Sample too short for requested horizon/p.")

        reg_shock = shock[start:stop]
        controls = [y[start - lag : stop - lag, :] for lag in range(1, p + 1)]
        X = np.column_stack([reg_shock] + controls)
        X = sm.add_constant(X)

        for response in range(n_vars):
            dep = y[start + h : stop + h, response]
            model = sm.OLS(dep, X).fit(cov_type="HC1")
            out[h, response] = model.params[1]

    return out


def estimate_var_irf(y: np.ndarray, horizon: int, p: int = 1, shock_index: int = 0) -> np.ndarray:
    """Estimate orthogonalized VAR IRFs (Cholesky identification)."""
    model = VAR(y)
    result = model.fit(maxlags=p, trend="c")
    irf = result.irf(horizon).orth_irfs
    return irf[:, :, shock_index]


def summarize_draws(draws: np.ndarray, ci: float = 0.95) -> IRFSummary:
    """Compute pointwise mean and confidence bands from simulation draws."""
    alpha = 1.0 - ci
    lower_q = alpha / 2.0
    upper_q = 1.0 - alpha / 2.0
    return IRFSummary(
        mean=np.mean(draws, axis=0),
        lower=np.quantile(draws, lower_q, axis=0),
        upper=np.quantile(draws, upper_q, axis=0),
    )


def run_simulation(
    reps: int = 100,
    T: int = 200,
    burn: int = 100,
    horizon: int = 12,
    p: int = 1,
    seed: int = 5821,
    ci: float = 0.95,
) -> SimulationResults:
    """Run Monte Carlo simulation comparing LP and VAR IRF estimators."""
    params = default_dgp_params()
    n_vars = params.A.shape[0]
    rng = np.random.default_rng(seed)

    lp_draws = np.zeros((reps, horizon + 1, n_vars))
    var_draws = np.zeros((reps, horizon + 1, n_vars))

    for r in range(reps):
        y, eps = simulate_dgp(T=T, burn=burn, params=params, rng=rng)
        lp_draws[r] = estimate_lp_irf(y=y, shock=eps[:, 0], horizon=horizon, p=p)
        var_draws[r] = estimate_var_irf(y=y, horizon=horizon, p=p, shock_index=0)

    horizons = np.arange(horizon + 1)
    true_values = true_irf(params=params, horizon=horizon, shock_index=0)

    return SimulationResults(
        horizons=horizons,
        true_irf=true_values,
        lp=summarize_draws(lp_draws, ci=ci),
        var=summarize_draws(var_draws, ci=ci),
    )


def plot_irf_comparison(results: SimulationResults, output_path: str | Path | None = None) -> plt.Figure:
    """Plot true IRFs and Monte Carlo confidence bands for LP and VAR."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5), sharex=True)
    labels = ["Response: y1", "Response: y2"]
    h = results.horizons

    for j, ax in enumerate(axes):
        ax.plot(h, results.true_irf[:, j], color="black", lw=2, label="True IRF")

        ax.plot(h, results.lp.mean[:, j], color="#1f77b4", lw=1.8, label="LP mean")
        ax.fill_between(h, results.lp.lower[:, j], results.lp.upper[:, j], color="#1f77b4", alpha=0.2)

        ax.plot(h, results.var.mean[:, j], color="#ff7f0e", lw=1.8, label="VAR mean")
        ax.fill_between(h, results.var.lower[:, j], results.var.upper[:, j], color="#ff7f0e", alpha=0.2)

        ax.axhline(0.0, color="gray", lw=0.8, ls="--")
        ax.set_title(labels[j])
        ax.set_xlabel("Horizon")
        ax.set_ylabel("IRF")

    handles, legends = axes[0].get_legend_handles_labels()
    fig.legend(handles, legends, loc="upper center", ncol=3, frameon=False)
    fig.suptitle("Local Projection vs VAR: Monte Carlo IRFs (95% bands)", y=1.02)
    fig.tight_layout()

    if output_path is not None:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_path, dpi=150, bbox_inches="tight")

    return fig


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="LP vs VAR IRF Monte Carlo comparison")
    parser.add_argument("--reps", type=int, default=100, help="Number of simulation repetitions")
    parser.add_argument("--T", type=int, default=200, help="Sample size per simulation")
    parser.add_argument("--burn", type=int, default=100, help="Burn-in observations")
    parser.add_argument("--horizon", type=int, default=12, help="Maximum IRF horizon")
    parser.add_argument("--seed", type=int, default=5821, help="Random seed")
    parser.add_argument(
        "--output",
        type=str,
        default="graph/lp_vs_var_irf_ci.png",
        help="Output path for the figure",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    results = run_simulation(
        reps=args.reps,
        T=args.T,
        burn=args.burn,
        horizon=args.horizon,
        seed=args.seed,
    )
    plot_irf_comparison(results, output_path=args.output)
    print(f"Saved figure to {args.output}")


if __name__ == "__main__":
    main()
