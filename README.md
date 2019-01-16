## PyFFTW Playground
This repo contains recipes to install PyFFTW, and a python script to test the performnce of
different ffts (numpy, scipy, FFTW) in pythob


### Installation steps
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

### Benchmarking

A python script called ``benchmark.py`` can be used to benchmark the speed of different ffts (numpy, scipy, FFTW) in your system.
Run the script in the following way

```
python performance.py computer fft 10
```
where you can specify your computer name (eg ``mac_book_air_1_3_GHz_Intel_Core_i5``), if you want to use
numpy fft (``fft``) or fftpack (``fftpack``) - the first using MKL if installed with conda, the second being the slower if MKL
is not available - and the number of times an fft is tested by timeit function (>10 to be somehow reliable).

This script will automatically create some summary plots, please commit them so with time we will
get a library of performance tests and can see which fft is best in which environment.