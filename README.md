# Stan2tfp

The new [Stan compiler](https://github.com/stan-dev/stanc3) features a TensorFlow Probability backend, translating Stan programs to python code. 

stan2tfp is a lightweight python wrapper around this functionality, allowing users to:

* call the compiler (emitting TFP code)
* run the code (creating a model object in the current namespace)
* sample the model (using TFP's NUTS)

... without leaving the notebook or their favorite IDE.

The new compiler and the TFP backend are under active development. Currently only a small subset of Stan's functionality is supported. For a list of supported distributions, see ...

## Install

`pip install stan2tfp`

## How to use
