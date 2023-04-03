# Linear algebra package

If you wish to create an `Anaconda` environment, an `environment.yml` file has
been provided from which you can create the `mpm_la` environment
by running
```bash
conda env create -f environment.yml
```
from within the base folder of this repository. If you wish to use some other virtual environment solution,
when in your environment ensure that all requirements are satisfied via
```bash
pip install -r requirements.txt
```

Following the installation of the requirements, the `mpm_la` package should be installed by running
```bash
pip install -e .
```
from within the base folder of this repository.

You can ensure the `mpm_la` package has been installed in the environment via
```bash
pip show mpm_la
```
