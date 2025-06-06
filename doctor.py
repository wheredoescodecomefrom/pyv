import os
import shutil
from pathlib import Path
from utils import check_connection, is_in_path

def doctor():
    print("🔎 Running pyv diagnostics...")

    checks = {
        "Python Build Tools": shutil.which("make") is not None,
        "Git Installed": shutil.which("git") is not None,
        "Internet Connection": check_connection("https://python.org"),
        "Install Directory": (Path.home() / ".pyv").exists(),
        "pyv in PATH": is_in_path(str(Path.home() / ".local" / "bin")),
    }

    for n,p in checks.items():
        status = "✅" if p else "❌"
        print(f"{n}: {status}")