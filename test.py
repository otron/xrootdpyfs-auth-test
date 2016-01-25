import xrootdpyfs
import pdb
from subprocess import call, PIPE
import os

from fs.opener import opener


def connect_test():
    """Do some test connecting awww yeahhhh"""

    kdestroy()
    # `klist` is empty (returns 0 when not empty)
    with open(os.devnull, 'wb') as discard:
        call(['klist'], stdout=discard,
             stderr=discard)
    # pdb.set_trace()
    kinit_via_tab('cern.butts', 'otrondru')

    xrdfs, path = connect()
    assert xrdfs


def connect():
    """Connect to the EOS server thingy."""
    remote_root = "root://eosuser.cern.ch"
    remote_dir = "//eos/user/o/otrondru/"

    return opener.parse(remote_root + remote_dir)


def kinit_via_tab(keytab, principal):
    """Get a kerberos ticket via a keytab."""
    cmd = ['kinit', '-t', keytab, principal]
    call_discard(cmd)


def kdestroy():
    """Destroy kerberos tickets on system."""
    call_discard(['kdestroy'])


def call_discard(cmd):
    """Call `cmd` and discard the stderr and -out."""
    with open(os.devnull, 'wb') as discard:
        call(cmd, stdout=discard,
             stderr=discard)


if __name__ == '__main__':
    connect_test()
