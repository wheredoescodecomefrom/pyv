import subprocess
import shutil
from pathlib import Path

PYV_DIR = Path.home() / ".pyv"

def update_pyv():
    if not (PYV_DIR / ".git").exists():
        response = input("pyv is not installed. Would you like to install it using git? (y/n): ")
        if response.lower() == "y":
            if PYV_DIR.exists():
                shutil.rmtree(PYV_DIR)

            subprocess.run(["curl", "-fsSL", "https://raw.githubusercontent.com/wheredoescodecomefrom/pyv/main/install.sh", "|", "bash"])
        else:
            print("pyv will not be installed.")
    
    try:
        print("🔄 Updating pyv...")
        subprocess.run(["git", "-C", str(PYV_DIR), "pull"], check=True)
        print("✅ pyv is now up to date.")
    except subprocess.CalledProcessError as e:
        print("❌ Failed to update pyv. Please check your internet connection or install location.")
