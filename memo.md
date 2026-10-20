#　開発メモ

## Postgres接続方法
pgAdmin4とかでデータベース作成

.env 作成して、以下を追加

DB_NAME='DB名'

DB_USER='postgres'

DB_PASSWORD='password'

DB_HOST=localhost

DB_PORT=5432


pip install python-dotenv して、
settings.py(別で分けていたら、base.pyとかに)

from dotenv import load_dotenv

load_dotenv(BASE_DIR / ".env")

を追加して、
python manage.py migrate を実行 

