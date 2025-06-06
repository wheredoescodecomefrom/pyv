#!/bin/bash

set -e

REPO_URL="https://github.com/wheredoescodecomefrom/pyv"
INSTALL_DIR="$HOME/.pyv"
BIN_DIR="$HOME/.local/bin"

echo "📦 Installing pyv..."

mkdir -p "$INSTALL_DIR"
mkdir -p "$BIN_DIR"

if [ -d "$INSTALL_DIR"/.git]; then
    echo "📦 Updating existing installation..."
    git -C "$INSTALL_DIR" pull
else
    echo "⬇️ Cloning from $REPO_URL..."
    git clone "$REPO_URL" "$INSTALL_DIR"
fi

cat > "$BIN_DIR/pyv" <<EOF
#!/usr/bin/env bash
python3 "$INSTALL_DIR/pyv.py" "\$@"
EOF

if [[ ":$PATH:" != *":BIN_DIR:"* ]]; then
    echo "📦 Adding $BIN_DIR to PATH..."
    
    SHELL_RC="\$HOME/.bashrc"
    [ -n "\$ZSH_VERSION" ] && SHELL_RC="\$HOME/.zshrc"
    echo "export PATH=\"\$HOME/.local/bin:\$PATH\"" >> "\$SHELL_RC"
    echo "✅ Restart your shell or run: source \$SHELL_RC"
fi

echo "✅ pyv installed! Try 'pyv --help'"