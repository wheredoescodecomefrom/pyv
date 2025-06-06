import os
import requests
import shutil
from pathlib import Path

PYV_HOME = os.pat.expanduser("~/.pyv")
PROJECT_LOCAL_VERSIONS = os.path.join(PYV_HOME, "local_versions")

def ensure_dirs():
    os.makedirs(os.path.join(PYV_HOME, "versions"), exist_ok=True)
    os.makedirs(PROJECT_LOCAL_VERSIONS, exist_ok=True)

def check_connection(url):
    try:
        response = requests.head(url)
        return response.status_code == 200
    except requests.RequestException:
        return False

def is_in_path(dir):
    return True if os.path.exists(dir) else False

def clean():
    build_dir = Path.home() / ".pyv/build"
    if build_dir.exists():
        shutil.rmtree(build_dir)
    print("Build artifacts removed.")

def exec_command(ver, comm):
    import subprocess
    bin_path = Path.home() / ".pyv/data/versions" / ver / "bin" / comm[0]
    if not bin_path.exists():
        print(f"❌ Version {ver} or command not found")
        return
    subprocess.run([str(bin_path) + comm[:1]])