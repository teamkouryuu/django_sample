# django_sample

## 動作環境

python3.8.2

## 仮想環境での実行

virtualenvをインストールすることをおすすめします。

1. virtualenvのインストール  

- ubuntu

    ```bash
    sudo apt install virtualenv
    ```

- windows

    ```bash
    pip install virtualenv
    ```

2. 仮想環境作成

    rootディレクトり内で以下コマンド入力

    ```bash
    virtualenv .env
    ```

    仮想環境の有効化

    ```bash
    source .env/bin/active
    ```

    依存関係のインストール

    ```bash
    pip install -r requirements.txt
    ```

- サーバー起動

    1.初めにmigrateの実行と管理アカウントの作成が必要

    - migrateの実行

        ```bash
        python manage.py migrate
        ```

    - 管理アカウントの作成

        ```bash
        python manage.py createsuperuser
        ユーザー名 (leave blank to use 'ubuntu'): admin
        Password: admin
        Password (again): admin
        このパスワードは ユーザー名 と似すぎています。
        このパスワードは短すぎます。最低 8 文字以上必要です。
        このパスワードは一般的すぎます。
        Bypass password validation and create user anyway? [y/N]: y
        ```

    2. サーバー起動

        ```bash
        python manage.py runserver
        ```

