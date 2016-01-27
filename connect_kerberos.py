import xrootdpyfs
from subprocess import call, PIPE
import os
from fs.opener import opener
import config as cfg
import pdb


_kinit_via_keytab = lambda: call_discard(['kinit', '-t', cfg.keytab_file,
                                          cfg.principal])

_kdestroy = lambda: call_discard(['kdestroy'])


def call_discard(cmd):
    """Call `cmd` and discard the stderr and -out."""
    with open(os.devnull, 'wb') as discard:
        call(cmd, stdout=discard,
             stderr=discard)


def do_connect():
    # set up kerberos ticket
    _kdestroy()
    _kinit_via_keytab()
    xrdfs, path = cfg.connect()
    assert xrdfs
    assert xrdfs.listdir('')


if __name__ == '__main__':
    do_connect()
