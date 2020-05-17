# Supported distributions

The TFP backend is still work in progress, and currently supports only a small subset of the Stan langauge.

The following distributions are currently supported:

* Binary:
    * Bernoulli
	* Bernoulli (logit parameterization)
* Bounded discrete
    * Binomial
	* Binomial (logit parameterization)
* Unounded discrete
    * Poisson
	* Poisson (log parameterization)
* Continuous:
    * Normal
    * Student-T
    * Cauchy
    * Laplace
    * Gumbel
* Positive Continuous:
    * Lognormal
    * Chi-2
    * Exponential
    * Gamma
    * Inverse Gamma
* Positive Lower-Bounded:
    * Pareto
* Continuos [0,1]:
    * Beta
* Unbounded Vectors:
    * Multivariate Normal (Cholesky parameterization)