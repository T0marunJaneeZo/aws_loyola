###　こんにちは！このプロジェクトは上智大学のloyolaというサービスのクローンアプリを開発しているよ。
###　よく学期の最初にサーバーがダウンしかける原因を分析す為に、このプロジェクトをやっているよ！
###　尤も、普段大学に来ない怠惰な学生が大量にシステムに押し寄せるからなんだけどね。だから、負荷分散の処理までできたらいいな。と思ってるよ！！
###　F5アタックはやめてね！！

### 🔧 環境構築手順（開発者向け）
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

