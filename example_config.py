"""Contains "config" variables used for the EOS-XRootD connection demo.

EXAMPLE FILE. INSERT DESIRED VALUES AND RENAME THIS TO `config.py`
"""
from fs.opener import opener

# XRootD root server address
remote_root = "XRD ROOT SERVER ADDRESS"
# username on server/"principal" in keytab
principal = "USER_NAME"
# kerberos keytab file
keytab_file = ""
# Remote directory to connect to, appends to `remote_root`
# Example value is for CERN's EOS userbox service thingy
_remote_dir = lambda: "//eos/user/{0}/{1}/".format(principal[0], principal)

_full_url = lambda: remote_root + _remote_dir()


def connect(url=None):
    url = url or _full_url()
    return opener.parse(url)
