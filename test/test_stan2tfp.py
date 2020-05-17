import unittest
import numpy as np
from stan2tfp import Stan2tfp, download_stan2tfp_compiler
import pkg_resources


def significant_digit(x):
    return float("{:.1}".format(x))


def significant_mean(x):
    return significant_digit(np.mean(x))


eight_schools_data_dict = dict(
    J=8, y=[28, 8, -3, 7, -1, 1, 18, 12], sigma=[15, 10, 16, 11, 9, 11, 10, 18]
)

download_stan2tfp_compiler()


class TestStan2tfp(unittest.TestCase):
    """Tests for `stan2tfp` package."""

    def test_eight_schools_from_path(self):
        model = Stan2tfp(
            stan_file_path=pkg_resources.resource_filename(
                __name__, "./eight_schools_ncp.stan"
            ),
            data_dict=eight_schools_data_dict,
        )
        mcmc_trace, _ = model.sample()
        mu, tau, theta_tilde = [model.merge_chains(x) for x in mcmc_trace]

        self.assertAlmostEqual(significant_mean(mu), 4, delta=2)
        self.assertAlmostEqual(significant_mean(tau), 3, delta=2)
        self.assertAlmostEqual(significant_mean(theta_tilde), 0.08, delta=0.1)

    def test_eight_schools_from_stan_code(self):
        stan_code = """
data {
  int<lower=0> J;
  real y[J];
  real<lower=0> sigma[J];
}

parameters {
  real mu;
  real<lower=0> tau;
  vector[J] theta_tilde;
}

transformed parameters {
  vector[J] theta = mu + tau * theta_tilde;
}

model {
  mu ~ normal(0, 5);
  tau ~ normal(0, 5);
  theta_tilde ~ normal(0, 1);
  y ~ normal(theta, sigma);
}
        """
        model = Stan2tfp(stan_model_code=stan_code, data_dict=eight_schools_data_dict)
        mcmc_trace, _ = model.sample()
        mu, tau, theta_tilde = [model.merge_chains(x) for x in mcmc_trace]

        self.assertAlmostEqual(significant_mean(mu), 4, delta=2)
        self.assertAlmostEqual(significant_mean(tau), 3, delta=2)
        self.assertAlmostEqual(significant_mean(theta_tilde), 0.08, delta=0.1)

    def test_init_without_data(self):
        stan_code = """
data {
  int<lower=0> J;
  real y[J];
  real<lower=0> sigma[J];
}

parameters {
  real mu;
  real<lower=0> tau;
  vector[J] theta_tilde;
}

transformed parameters {
  vector[J] theta = mu + tau * theta_tilde;
}

model {
  mu ~ normal(0, 5);
  tau ~ normal(0, 5);
  theta_tilde ~ normal(0, 1);
  y ~ normal(theta, sigma);
}
        """
        model = Stan2tfp(stan_model_code=stan_code)
        model.init_model(eight_schools_data_dict)
        mcmc_trace, _ = model.sample()
        mu, tau, theta_tilde = [model.merge_chains(x) for x in mcmc_trace]

        self.assertAlmostEqual(significant_mean(mu), 4, delta=2)
        self.assertAlmostEqual(significant_mean(tau), 3, delta=2)
        self.assertAlmostEqual(significant_mean(theta_tilde), 0.08, delta=0.1)


if __name__ == "__main__":
    unittest.main()
