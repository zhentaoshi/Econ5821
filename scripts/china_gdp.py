# AI generated

import os
import requests
import pandas as pd
import matplotlib.pyplot as plt


def fetch_gdp(start=1960, end=2024):
    url = (
        f"http://api.worldbank.org/v2/country/CHN/indicator/NY.GDP.MKTP.CD"
        f"?format=json&date={start}:{end}&per_page=1000"
    )
    resp = requests.get(url, timeout=20)
    resp.raise_for_status()
    data = resp.json()
    if not isinstance(data, list) or len(data) < 2:
        raise RuntimeError("Unexpected World Bank response format")
    records = data[1]
    rows = []
    for r in records:
        year = r.get("date")
        val = r.get("value")
        if val is None:
            continue
        try:
            rows.append({"year": int(year), "gdp_usd": float(val)})
        except Exception:
            continue
    df = pd.DataFrame(rows).sort_values("year").reset_index(drop=True)
    return df


def plot_gdp(df, out_path):
    try:
        plt.style.use("seaborn-whitegrid")
    except Exception:
        plt.style.use("ggplot")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df["year"], df["gdp_usd"] / 1e12, lw=2)
    ax.set_xlabel("Year")
    ax.set_ylabel("GDP (trillions USD)")
    ax.set_title("China GDP (current US$)")
    ax.ticklabel_format(axis="y", style="plain")
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


def main():
    df = fetch_gdp()
    out_dir = os.path.join(os.getcwd(), "data_example")
    os.makedirs(out_dir, exist_ok=True)
    csv_path = os.path.join(out_dir, "china_gdp.csv")
    png_path = os.path.join(out_dir, "china_gdp.png")
    df.to_csv(csv_path, index=False)
    plot_gdp(df, png_path)
    print(f"Saved CSV: {csv_path}")
    print(f"Saved plot: {png_path}")


if __name__ == "__main__":
    main()
