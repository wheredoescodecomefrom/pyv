# pyv 🐍 - A Simple Python Version Manager

`pyv` is a lightweight, cross-platform Python version manager — like `nvm`, but for Python.

## ✨ Features

- Install any Python version from python.org
- Use global or per-project versions (`.python-version`)
- Automatically switch versions when entering directories
- List and uninstall versions
- Easy to update via `pyv update`

## 📦 Installation

```bash
curl -fsSL https://raw.githubusercontent.com/wheredoescodecomefrom/pyv/main/install.sh | bash
```

Then restart your terminal or run:

```bash
source ~/.bashrc # or ~/.zshrc
```

Make sure ~/.local/bin` is in your $PATH

## Usage

```bash
pyv install 3.12.2        # Install Python
pyv use 3.12.2            # Set as global version
pyv current               # Show current version
pyv list                  # List installed versions
pyv uninstall 3.12.2      # Remove a version
pyv available             # See versions from python.org
pyv update                # Update pyv
```

### Per-Project Version
Create a `.python-version` file in any directory:


```
3.11.0
```
Then pyv will use that version when you cd into it

### Pro Tip: Auto-switch
Add this to your `.bashrc` or `.zshrc`:

```bash
pyv_auto_switch() {
  if [ -f .python-version ]; then
    export PYV_ACTIVE_VERSION=$(cat .python-version)
    export PATH="$HOME/.pyv/data/versions/$PYV_ACTIVE_VERSION/bin:$PATH"
  fi
}

cd() {
  builtin cd "$@" && pyv_auto_switch
}
```

### Requirements:

- Python 3.7+
- Build tools (make, gcc, etc)
- Unix-like OS (Linux, macOS, Raspberry Pi)

### Development

```bash
git clone https://github.com/YOURUSER/pyv.git
cd pyv
pip install .
```

### License
MIT License