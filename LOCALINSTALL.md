Install fftw:
```
brew install fftw --with-openmp
```

From the root directory of this repo:
```
cd ..
git clone https://github.com/pyFFTW/pyFFTW.git
cd pyFFTW
conda activate pylopsfftw
export DYLD_LIBRARY_PATH=/usr/local/lib
export LDFLAGS="-L/usr/local/lib"
export CFLAGS="-I/usr/local/include"
python setup.py build_ext --inplace
python setup.py develop
```

Output:
```

running build_ext
Build pyFFTW with support for FFTW with
double precision + pthreads
single precision + pthreads
long precision + pthreads
cythoning pyfftw/pyfftw.pyx to pyfftw/pyfftw.c
/Users/matteoravasi/anaconda/envs/pylopsfftw/lib/python3.7/site-packages/Cython/Compiler/Main.py:367: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: /Users/matteoravasi/Desktop/PyLops/pyFFTW/pyfftw/pyfftw.pxd
  tree = Parsing.p_module(s, pxd, full_module_name)
building 'pyfftw.pyfftw' extension
creating build
creating build/temp.macosx-10.7-x86_64-3.7
creating build/temp.macosx-10.7-x86_64-3.7/pyfftw
gcc -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/usr/local/include -I/Users/matteoravasi/anaconda/envs/pylopsfftw/include/python3.7m -I/Users/matteoravasi/Desktop/PyLops/pyFFTW/include -I/Users/matteoravasi/Desktop/PyLops/pyFFTW/pyfftw -I/Users/matteoravasi/anaconda/envs/pylopsfftw/lib/python3.7/site-packages/numpy/core/include -I/Users/matteoravasi/anaconda/envs/pylopsfftw/include -I/Users/matteoravasi/anaconda/envs/pylopsfftw/include/python3.7m -c pyfftw/pyfftw.c -o build/temp.macosx-10.7-x86_64-3.7/pyfftw/pyfftw.o
In file included from pyfftw/pyfftw.c:613:
In file included from /Users/matteoravasi/anaconda/envs/pylopsfftw/lib/python3.7/site-packages/numpy/core/include/numpy/arrayobject.h:4:
In file included from /Users/matteoravasi/anaconda/envs/pylopsfftw/lib/python3.7/site-packages/numpy/core/include/numpy/ndarrayobject.h:18:
In file included from /Users/matteoravasi/anaconda/envs/pylopsfftw/lib/python3.7/site-packages/numpy/core/include/numpy/ndarraytypes.h:1823:
/Users/matteoravasi/anaconda/envs/pylopsfftw/lib/python3.7/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:15:2: warning:
      "Using deprecated NumPy API, disable it by "          "#defining
      NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-W#warnings]
#warning "Using deprecated NumPy API, disable it by " \
 ^
1 warning generated.
creating build/lib.macosx-10.7-x86_64-3.7
creating build/lib.macosx-10.7-x86_64-3.7/pyfftw
gcc -bundle -undefined dynamic_lookup -L/Users/matteoravasi/anaconda/envs/pylopsfftw/lib -arch x86_64 -L/Users/matteoravasi/anaconda/envs/pylopsfftw/lib -arch x86_64 -L/usr/local/lib -I/usr/local/include -arch x86_64 build/temp.macosx-10.7-x86_64-3.7/pyfftw/pyfftw.o -L/Users/matteoravasi/anaconda/envs/pylopsfftw/lib -lfftw3l_threads -lfftw3l -lfftw3f_threads -lfftw3f -lfftw3_threads -lfftw3 -o build/lib.macosx-10.7-x86_64-3.7/pyfftw/pyfftw.cpython-37m-darwin.so
copying build/lib.macosx-10.7-x86_64-3.7/pyfftw/pyfftw.cpython-37m-darwin.so -> pyfftw

-------------------------------------------------------

running develop
running egg_info
creating pyFFTW.egg-info
writing pyFFTW.egg-info/PKG-INFO
writing dependency_links to pyFFTW.egg-info/dependency_links.txt
writing requirements to pyFFTW.egg-info/requires.txt
writing top-level names to pyFFTW.egg-info/top_level.txt
writing manifest file 'pyFFTW.egg-info/SOURCES.txt'
reading manifest file 'pyFFTW.egg-info/SOURCES.txt'
reading manifest template 'MANIFEST.in'
warning: no files found matching 'CHANGELOG.md'
no previously-included directories found matching 'docs/_build'
no previously-included directories found matching 'build'
no previously-included directories found matching '*/__pycache__'
warning: no previously-included files matching '*.py[cod]' found anywhere in distribution
warning: no previously-included files matching '*.so' found anywhere in distribution
warning: no previously-included files matching '*.dll' found anywhere in distribution
warning: no previously-included files matching '*.dylib' found anywhere in distribution
warning: no previously-included files matching '*~' found anywhere in distribution
warning: no previously-included files matching '*.bak' found anywhere in distribution
warning: no previously-included files matching '*.swp' found anywhere in distribution
writing manifest file 'pyFFTW.egg-info/SOURCES.txt'
running build_ext
Build pyFFTW with support for FFTW with
double precision + pthreads
single precision + pthreads
long precision + pthreads
skipping 'pyfftw/pyfftw.c' Cython extension (up-to-date)
copying build/lib.macosx-10.7-x86_64-3.7/pyfftw/pyfftw.cpython-37m-darwin.so -> pyfftw
Creating /Users/matteoravasi/anaconda/envs/pylopsfftw/lib/python3.7/site-packages/pyFFTW.egg-link (link to .)
Adding pyFFTW 0.11.1+4.g5bf1dda to easy-install.pth file

Installed /Users/matteoravasi/Desktop/PyLops/pyFFTW
Processing dependencies for pyFFTW==0.11.1+4.g5bf1dda
Searching for numpy==1.15.4
Best match: numpy 1.15.4
Adding numpy 1.15.4 to easy-install.pth file

Using /Users/matteoravasi/anaconda/envs/pylopsfftw/lib/python3.7/site-packages
Finished processing dependencies for pyFFTW==0.11.1+4.g5bf1dda
```