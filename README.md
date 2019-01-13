## PyFFTW Playground
This repo is used to identify if PyFFTW can be included in Pylops and create a .travis pipeline for installing
and using PyFFTW

### Installation steps on mac

Create environment:
```
make install_conda
```

Install pyfftw:

* option 1: local install, see ``LOCALINSTALL.md`` file
* option 2:
    ```
    pip install pyfftw
    ```
* option 3:
    ```
    conda install -c conda-forge pyfftw
    ```