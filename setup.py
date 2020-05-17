"""The setup script."""

from setuptools import setup, find_packages

# with open("README.rst") as readme_file:
#     readme = readme_file.read()

# with open("HISTORY.rst") as history_file:
#     history = history_file.read()

requirements = [
    "pip",
    "numpy",
    "tf-nightly",
    "tfp-nightly",
]

# setup_requirements = []

# test_requirements = []

setup(
    name="stan2tfp",
    author="Adam Haber",
    author_email="adamhaber@gmail.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: BSD-3",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
    ],
    url="https://github.com/adamhaber/stan2tfp",
    python_requires=">=3.6",
    description="Python Boilerplate contains all the boilerplate you need to create a Python package.",
    entry_points={"console_scripts": ["stan2tfp=stan2tfp.cli:main",],},
    install_requires=requirements,
    license="MIT license",
    # long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
    keywords="stan, tfp, bayesian models",
    packages=find_packages(include=["stan2tfp", "stan2tfp.*"]),
    # setup_requires=setup_requirements,
    test_suite="tests",
    # tests_require=test_requirements,
    version="0.1.0",
)
