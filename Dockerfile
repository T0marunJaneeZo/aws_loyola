# ベースイメージ：軽量な Python イメージを使用
FROM python:3.10-slim

# 環境変数（キャッシュ防止とログの即時出力）
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 作業ディレクトリを作成
WORKDIR /app

# requirements.txt をコピーして依存をインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# プロジェクト全体をコピー
COPY . .

# Django 開発用サーバを起動（本番は後でgunicornに変える）
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

