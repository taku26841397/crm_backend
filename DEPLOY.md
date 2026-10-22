# Oracle Cloud デプロイ手順

## サーバー情報

- Oracle Cloud Free Tier
- Ubuntu
- Django 5
- PostgreSQL
- Gunicorn
- Nginx

---

# 初回セットアップ

## リポジトリ取得

```bash
git clone <repository>
cd crm_backend
```

## 仮想環境

```bash
python3 -m venv venv
source venv/bin/activate
```

## パッケージインストール

```bash
pip install -r requirements.txt
```

---

# 環境変数

`.env` を作成

```env
SECRET_KEY=xxxx

DB_NAME=xxxx
DB_USER=xxxx
DB_PASSWORD=xxxx
DB_HOST=xxxx
DB_PORT=5432
```

---

# Django

## マイグレーション

```bash
python manage.py migrate \
  --settings=config.settings.prod
```

## 管理ユーザー

```bash
python manage.py createsuperuser \
  --settings=config.settings.prod
```

---

# Static

## collectstatic

```bash
python manage.py collectstatic \
  --settings=config.settings.prod
```

---

# Gunicorn

## サービス配置

```bash
sudo cp deploy/gunicorn.service \
  /etc/systemd/system/gunicorn.service
```

## 起動

```bash
sudo systemctl daemon-reload
sudo systemctl enable gunicorn
sudo systemctl start gunicorn
```

## 確認

```bash
sudo systemctl status gunicorn
```

---

# Nginx

## 設定配置

```bash
sudo cp deploy/nginx.conf \
  /etc/nginx/sites-available/crm_backend
```

## 有効化

```bash
sudo ln -s \
/etc/nginx/sites-available/crm_backend \
/etc/nginx/sites-enabled/
```

## 確認

```bash
sudo nginx -t
```

## 再起動

```bash
sudo systemctl restart nginx
```

---

# 本番設定

## gunicorn.service

```ini
Environment="DJANGO_SETTINGS_MODULE=config.settings.prod"
```

必須。

設定しない場合、

```text
config.settings.dev
```

で起動する。

---

## prod.py

```python
DEBUG = False

ALLOWED_HOSTS = [
    "168.110.20.125",
    "10.0.0.202",
    "127.0.0.1",
    "localhost",
]

STATIC_ROOT = BASE_DIR / "staticfiles"
```

---

# Oracle Cloud

## Security List

許可

- 22
- 80

---

## NSG

許可

- 22
- 80

---

# iptables

確認

```bash
sudo iptables -L INPUT -n --line-numbers
```

80番ルールが消えていないこと。

追加

```bash
sudo iptables -I INPUT 5 \
  -p tcp --dport 80 -j ACCEPT
```

---

# 動作確認

## Gunicorn

```bash
sudo systemctl status gunicorn
```

## Nginx

```bash
sudo systemctl status nginx
```

## Admin

```text
http://168.110.20.125/admin/
```

---

# 今回ハマったポイント

- gunicorn が停止していて 502 Bad Gateway
- `ALLOWED_HOSTS` が不足していて 400 Bad Request
- `collectstatic` 未実行で管理画面の CSS が効かなかった
- iptables の 80 番ルールが消えてタイムアウトになった
- `DJANGO_SETTINGS_MODULE=config.settings.prod` を設定しないと dev.py で起動する