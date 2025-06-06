import os
from pathlib import Path
import json

PYV_HOME = Path.home() / ".pyv"
CONFIG_FILE = PYV_HOME / "data" / "config.json"
VERSIONS_DIR = PYV_HOME / "data" / "versions"

def ensure_config():
    CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not CONFIG_FILE.exists():
        CONFIG_FILE.write_text(json.dumps({"current": ""}))

def set_version(version: str):
    ensure_config()
    config = json.loads(CONFIG_FILE.read_text())
    if not (VERSIONS_DIR / version).exists():
        print(f"Version {version} is not installed.")
        return
    config["current"] = version
    CONFIG_FILE.write_text(json.dumps(config))
    print(f"Global Python version set to {version}")

def uninstall_version(version):
    path = VERSIONS_DIR / version
    if not path.exists():
        print(f"Version {version} not found.")
        return
    import shutil
    shutil.rmtree(path)
    print(f"✅ Uninstalled Python {version}")

def get_current_version():
    if os.getenv("PYV_VERSION"):
        return os.getenv("PYV_VERSION")
    local = get_local_version()
    if local:
        return local
    ensure_config()
    config = json.loads(CONFIG_FILE.read_text())
    return config.get("current", "")

def get_local_version():
    from pathlib import Path
    path = Path.cwd() / ".python-version"
    if path.exists():
        return path.read_text().strip()
    return None

def list_versions():
    if not VERSIONS_DIR.exists():
        return []
    return [p.name for p in VERSIONS_DIR.iterdir() if p.is_dir()]
