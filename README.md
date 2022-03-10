# 簡易英単語アプリ

### poetry による Python 環境のセットアップ

- ローカルに poetry をインストール(Poetry version 1.1.13)

  - `pip3 install poetry`
  - or
  - ```sh
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
    ```

- バージョン確認

  - ```sh
    $ poetry -V
    Poetry version 1.1.13
    ```

### 仮想環境のセットアップ

- poetry でライブラリをインストール (pyproject.toml が既にある場合)
  - `sh init.sh`
  - ルートディレクトリに仮想環境`.venv`フォルダが作られる。

### API の立ち上げ

- `sh run_api.sh`

### 追加パッケージのインストール

- `poetry add <package-name>}`
