### こんにちは！

このプロジェクトは、上智大学のLoyolaという履修管理サービスのクローンアプリです。  
よく学期初日にサーバーがダウンしかける現象を観察し、その原因を技術的に分析する目的で作っています。  
怠惰な学生が突然大量にアクセスしてくるF5アタック的状況にも耐えられるよう、最終的には**負荷分散（スケーラビリティ）**も視野に入れています。

※ F5アタックはやめてね笑

---

**注:** Djangoの基本（`manage.py`, `urls.py`, `settings.py`, MTVモデルなど）は理解している前提でコメントを書いています。

---

### 環境構築手順（開発者向け）
~~~zsh
git clone https://github.com/T0marunJaneeZo/aws_loyola.git
cd aws_loyola
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver
~~~

- 2025/05/23: カスタムユーザーモデル（CustomUser）作成 & マイグレーション済み

## Loyola 履修管理システム
~~~zsh:tree
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
~~~                                                    

###     アカウント登録機能（暫時）

~~~zsh:tree
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
~~~

###     更新履歴

~~~
- 2025/05/23: カスタムユーザーモデル `CustomUser` 実装、ユーザー種別（生徒・教員・執行部）に対応
- 2025/05/23: 執行部向け「生徒アカウント一括発行フォーム」を追加
  - 学籍番号形式 `Ayyddnnn`（例: A2442001）で自動生成
  - 英数字8桁ランダムな初期パスワード生成を実装
- 2025/05/23: `.gitignore` を更新（不要ファイル除外）
- 2025/05/23: 初回マイグレーションファイル `0001_initial.py` を追加
- 2025/05/23: `README.md` をMarkdown整形、構成図・セットアップ手順を記載
~~~