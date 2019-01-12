## PyFFTW Playground
This repo is used to identify if PyFFTW can be included in Pylops and create a .travis pipeline for installing
and using PyFFTW

### Installation steps on mac

Create environment:
```
make install_conda
```

Install fftw:
```
brew install fftw --with-openmp
```

Finally install pyfftw:

* option 1: local install, see ``LOCALINSTALL.md`` file
* option 2:
    ```
    export DYLD_LIBRARY_PATH=/usr/local/lib
    export LDFLAGS="-L/usr/local/lib"
    export CFLAGS="-I/usr/local/include"
    ```
    followed by
    ```
    pip install pyfftw
    ```
    or
    ```
    conda install -c conda-forge pyfftw
    ```