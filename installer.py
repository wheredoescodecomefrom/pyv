import os
import subprocess
import urllib.request
import tarfile
from pathlib import Path

PYV_HOME = Path.home() / ".pyv"
VERSIONS_DIR = PYV_HOME / "data" / "versions"

def install_version(version: str):
    install_path = VERSIONS_DIR / version
    if install_path.exists():
        print(f"Python {version} already installed.")
        return

    print(f"Installing Python {version}...")

    url = f"https://www.python.org/ftp/python/{version}/Python-{version}.tgz"
    archive_path = PYV_HOME / f"Python-{version}.tgz"

    # Download
    urllib.request.urlretrieve(url, archive_path)
    print("Downloaded.")

    # Extract
    with tarfile.open(archive_path, "r:gz") as tar:
        tar.extractall(PYV_HOME / "build")

    source_dir = PYV_HOME / "build" / f"Python-{version}"
    configure_cmd = ["./configure", f"--prefix={install_path}"]

    # Build & install
    subprocess.run(configure_cmd, cwd=source_dir, check=True)
    subprocess.run(["make", "-j4"], cwd=source_dir, check=True)
    subprocess.run(["make", "install"], cwd=source_dir, check=True)

    print(f"Python {version} installed at {install_path}")
