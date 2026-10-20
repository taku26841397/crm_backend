# CRM Backend

顧客管理システム（CRM）のバックエンドAPIです。

Django REST Framework を使用して開発し、顧客情報・対応履歴の管理機能を提供しています。

---

# 概要

営業活動や顧客対応の管理を目的としたCRMシステムのバックエンドです。

フロントエンド（Next.js）からのリクエストを受け取り、顧客情報や対応履歴の保存・更新・検索を行います。

---

# 使用技術

## Backend

- Python 3
- Django
- Django REST Framework
- Token Authentication
- dj-rest-auth
- django-allauth

## Database

- SQLite（開発環境）
- PostgreSQL（本番環境予定）

## Infrastructure

- Oracle Cloud Free Tier（導入予定）

---

# 主な機能

## 認証機能

- ユーザーログイン
- Token認証
- APIアクセス制御

## 顧客管理

- 顧客作成
- 顧客一覧取得
- 顧客詳細取得
- 顧客編集
- 顧客削除

## 対応履歴管理

- 対応履歴作成
- 対応履歴一覧取得
- 対応履歴編集
- 対応履歴削除

## ダッシュボード

- 顧客総数表示
- 新規顧客数表示
- 対応中顧客数表示
- 成約顧客数表示

## 一覧機能

- キーワード検索
- ステータス絞り込み
- ソート
- ページネーション

## 次回アクション管理

- 次回アクション登録
- 実施予定日登録
- 実施予定日の更新

---

# セキュリティ

## 認証

Django REST Framework の Token Authentication を採用しています。

## 認可

ログインユーザーごとにデータを分離しています。

ユーザーは自身が登録した顧客情報および対応履歴のみ閲覧・編集・削除できます。

---



# 環境変数

`.env`

```env
SECRET_KEY=your-secret-key
```

開発環境と本番環境で設定を分離しています。

```text
config/
└ settings/
    ├ base.py
    ├ dev.py
    └ prod.py
```

---

# 学習・工夫したポイント

- Django REST FrameworkによるAPI設計
- Token認証の実装
- ユーザー単位の認可制御
- ページネーション実装
- 検索・ソート機能実装
- settingsの開発環境／本番環境分離
- .envによる環境変数管理
- Next.jsとのAPI連携

---

# 今後の改善予定

- Oracle Cloudへのデプロイ
- PostgreSQL運用
- HTTPS対応
- Docker対応
- 自動テスト導入
- CI/CD構築

---

# Frontend

本システムは Next.js + TypeScript で開発したフロントエンドと連携して動作します。
