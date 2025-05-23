### こんにちは！

このプロジェクトは、上智大学のLoyolaという履修管理サービスのクローンアプリです。  
よく学期初日にサーバーがダウンしかける現象を観察し、その原因を技術的に分析する目的で作っています。  
怠惰な学生が突然大量にアクセスしてくるF5アタック的状況にも耐えられるよう、最終的には**負荷分散（スケーラビリティ）**も視野に入れています。

※ F5アタックはやめてね笑

---

**注:** Djangoの基本（`manage.py`, `urls.py`, `settings.py`, MTVモデルなど）は理解している前提でコメントを書いています。

---

### 環境構築手順（開発者向け）
git clone https://github.com/T0marunJaneeZo/aws_loyola.git   # ← GitHubからプロジェクトをコピー（初回のみ）
cd aws_loyola                                                # ← コピーしたディレクトリに移動
python -m venv venv                                          # ← 仮想環境を作成
source venv/bin/activate                                     # ← 仮想環境を有効化（Mac/Linux）
pip install -r requirements.txt                              # ← 必要なライブラリを一括インストール
cp .env.example .env                                         # ← 環境変数ファイルをコピーして準備
python manage.py migrate                                     # ← DB構造を反映
python manage.py runserver                                   # ← サーバー起動

## 更新履歴

- 2025/05/23: カスタムユーザーモデル（CustomUser）作成 & マイグレーション済み

## Loyola 履修管理システム
.
├── Dockerfile
├── README.md
├── accounts                                                  # アカウント登録のモデルとビュー
├── db.sqlite3
├── main_loyola                                               # プロジェクトディレクトリ_setting.pyが格納されているよ。
├── manage.py
├── requirements.txt
├── templates
│   └── accounts                                              # ./accountsのテンプレート
└── venv                                                          

###     アカウント登録機能（暫時）

./accounts
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py                                               # ←　生徒一括登録フォーム
    ├── migrations
    ├── models.py                                              # ←　簡易的なユーザーモデルを作成
    ├── tests.py  
    ├── urls.py                                                 
    └── views.py                                               # ←　生徒一括登録のビュー