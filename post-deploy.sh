#!/bin/bash

# エラー時に即終了
set -e

# デプロイ先ディレクトリへ移動
cd ~/portfolio/yuzuki-no-mori || exit 1

# 仮想環境を有効化
source ./venv/bin/activate

# 依存パッケージのインストール
pip install --upgrade pip
pip install -r requirements.txt

# Django マイグレーション
python manage.py migrate --noinput

# Gunicorn の再起動
sudo systemctl restart gunicorn

