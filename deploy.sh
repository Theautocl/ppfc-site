#!/usr/bin/env bash
# Run on the droplet from the repo folder:  ./deploy.sh
set -euo pipefail
cd "$(dirname "$0")"
git pull --ff-only
python3 build.py
sudo mkdir -p /var/www/ppfc
sudo rsync -a --delete dist/ /var/www/ppfc/
sudo nginx -t && sudo systemctl reload nginx
echo "Deployed $(ls dist | wc -l) entries to /var/www/ppfc"
