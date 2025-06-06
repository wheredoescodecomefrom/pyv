import os

PYV_HOME = os.pat.expanduser("~/.pyv")
PROJECT_LOCAL_VERSIONS = os.path.join(PYV_HOME, "local_versions")

def ensure_dirs():
    os.makedirs(os.path.join(PYV_HOME, "versions"), exist_ok=True)
    os.makedirs(PROJECT_LOCAL_VERSIONS, exist_ok=True)