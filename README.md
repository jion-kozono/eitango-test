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

### heroku へデプロイ

```sh
cd api
heroku login
git add . # ディレクトリ直下のファイルをgitの管理対象に追加
git commit -m "first commit" # ファイルの変更をgitに登録

heroku git:remote -a simple-eitango-test # Herokuとgitを関連づける
git push heroku master # HerokuにPython(FastAPI)アプリをデプロイ(配備)
```
