# Kintone × DeepAI（Flask）連携デモ

本リポジトリは、Kintone アプリと Flask API を連携し、外部AI処理（DeepAI風）を行うデモアプリケーションです。Render上でホストされるAPIサーバーを通じて、Kintone からボタン操作でデータを取得し、新規レコードを作成する動作を実現します。

---

## 🔧 構成概要

- **クライアント**：Kintone アプリ（JavaScript カスタマイズ）
- **APIサーバー**：Flask + Python（Render に自動デプロイ）
- **通信方式**：CORS 対応済みの `POST` リクエスト
- **データの流れ**：
    1. 一覧画面にボタンが表示
    2. ボタン押下で API を呼び出し
    3. API からの分析結果（feedback/summary）を元に新しいレコードを作成

---

## 📁 ファイル構成

# kintone-deepai
`kintone DeepAI Demo Server`



├── app.py # Flask アプリ（Render でホスト）
├── static/
├── templates/
├── kintone-deepai.js # Kintone JavaScript カスタマイズコード
└── README.md



---

## 🚀 セットアップ手順

### 1. Flask API をRenderでデプロイ

- Renderで新しいWebサービスを作成
- このリポジトリをGitHubから接続
- `app.py` に CORS 設定あり（kintoneからのアクセス許可）
- Python バージョンや `requirements.txt` をRender設定で指定
- 環境変数（APIキーなど）も Render 上で設定可能

### 2. Kintone にアプリを作成

- 必要なフィールドをフォームに追加（例：Business_ID, account_name, feedback, sumarry, datetime_user）
- 「アプリの設定」→「JavaScript / CSSでカスタマイズ」に `kintone-deepai.js` を追加
- アプリを更新し、一覧画面にボタンが表示されることを確認

---

## ✅ 使用技術

- Python 3.x
- Flask
- Flask-CORS
- kintone JavaScript API
- Render（デプロイホスティング）

---

## 🔐 セキュリティ

- `X-API-Key` による簡易認証を実装済み
- 本番環境ではさらにトークン認証やIP制限推奨

---

## 📄 免責

このアプリはデモ目的のサンプルです。実運用におけるセキュリティ・パフォーマンス要件に応じた追加実装が必要です。

---

## ✨ 今後の拡張案

- kintone のレコード選択に応じたデータ処理
- フィールドマッピングの柔軟化
- ChatGPT や外部AI APIとの本格連携
- ログ保存や通知機能の追加

---

## 📬 お問い合わせ

開発や導入に関するサポートが必要な場合は、リポジトリの [Issues](https://github.com/your/repo/issues) を通じてご連絡ください。

