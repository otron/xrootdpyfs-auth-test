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


## Generating a kerberos keytab file
Kudos goes to the [source on the interwebs](https://kb.iu.edu/d/aumh).

`ktutil -k 'keytab.file' add -p PRINCIPAL -e ENCTYPE`
(will prompt for the password of PRINCIPAL)

Outputs a keytab file with credentials for the given principal.
For a CERN principal, it'd be on the form `UNAME@CERN.CH`,
where you'd replace `UNAME` with your CERN username.
Enctype is... uh. It works with `arcfour-hmac-md5`.

