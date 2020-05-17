# Stan2tfp

![](https://github.com/adamhaber/stan2tfp/workflows/CI/badge.svg)

The new [Stan compiler](https://github.com/stan-dev/stanc3) features a TensorFlow Probability backend, transpiling Stan programs to python code. 

stan2tfp is a lightweight interface wrapper around this functionality, allowing users to:

* call the compiler (emitting TFP code)
* run the code (creating a model object in the current namespace)
* sample the model (using TFP's NUTS)

... without leaving the notebook or their favorite IDE.

The new compiler and the TFP backend are under active development. Currently only a small subset of Stan's functionality is supported. For a list of supported distributions, see [here](https://github.com/adamhaber/stan2tfp/blob/master/distributions.md).

## Install

stan2tfp is a pure-Python package which can be installed from PyPI

> `pip install stan2tfp`

This will also install TensorFlow and TensorFlow Probability (both in nightly version; needed for XLA compilation of the model). 

stan2tfp provides the function `download_stan2tfp_compiler` which downloads a pre-compiled binary of the compiler. By default it installs the latest version into the same directory as the package itself. A different path or a different version of the compiler can be specified.

## "Hello world"

For a simple end-to-end example of using stan2tfp, see [here](https://github.com/adamhaber/stan2tfp/blob/master/examples/eight%20schools%20example.ipynb).

