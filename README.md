# xrootdpyfs-auth-test
Testing EOS authentication for xrootdpyfs


## Installing `xrootdpyfs`
### OSX
1. Install XRootD via Homebrew
    - `brew install xrootd`
2. Install the [python xrootd bindings ("pyxrootd")](http://xrootd.org/doc/python/xrootd-python-0.1.0/).
  You can follow the installation instructions provided in the pyxrootd docs.
  Though it most likely won't work without the two exports below.
    a. `$ git clone git://github.com/xrootd/xrootd-python.git && cd xrootd-python`
    b. `$ export XRD_INCDIR='/usr/local/Cellar/xrootd/4.1.1/include/xrootd'
    c. `$ export XRD_LIBDIR='/usr/local/Cellar/xrootd/4.1.1/lib'
    d. `$ python setup.py install --user`
3. Install `xrootdpyfs`
    - `$ pip install xrootdpyfs`
