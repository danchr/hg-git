import setuptools
import subprocess
import sys

# don't guard this with a try; users should use pip for
# installing/building hg-git, as it ensures the proper dependencies
# are present
import setuptools_scm

assert setuptools_scm  # silence pyflakes

try:
    setuptools.setup()
except subprocess.CalledProcessError as e:
    print("A CalledProcessError was raised:", file=sys.stderr)
    print(e, file=sys.stderr)
    print(f"STDOUT:\n{e.stdout}\n=============\n", file=sys.stderr)
    print(f"STDERR:\n{e.stderr}\n=============\n", file=sys.stderr)
    raise
