# %%

import numpy as np
from scipy.optimize import minimize

def Poisson_nll(theta, x, y):
    """
    Perform Poisson regression to fit the model y ~ Poisson(exp(theta * x)).

    Parameters:
    theta (float): The parameter of the regression model.

    Returns:
    float: The negative log-likelihood of the model.
    """

    # Predict lambda using the model
    # change theta to a column vector
    lambda_pred = np.exp(np.dot(x, theta))
    
    # Calculate the negative log-likelihood
    nll = -np.sum(y * np.log(lambda_pred) - lambda_pred)

    return nll


def Poisson_est(theta_init, x, y):
    # Perform the optimization
    result = minimize(Poisson_nll, theta_init, args=(x, y), method='BFGS')

    # Extract the optimal value of theta
    theta_hat = result.x
    
    return theta_hat
    

# %%
# Example usage

# Generate data according to the Poisson regression model with a true theta = 2.0
# np.random.seed(0)  # For reproducibility


n = 100
K = 3
x = np.random.normal(0, 1, [n, K])
# add a column of ones for the intercept
x = np.concatenate((np.ones([n, 1]), x), axis=1)

true_theta = np.ones(K + 1) * 2.0

# generate the response variable
lambda_true = np.exp(np.dot(x, true_theta))
y = np.random.poisson(lambda_true)

# set the initial value of theta as a vector of 4 ones
theta_init = np.ones(K + 1) 

theta_hat = Poisson_est(theta_init, x, y)

print(f"true_theta: {true_theta}")
print(f"theta_hat: {theta_hat}")

# %%