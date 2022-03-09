# 簡易英単語アプリ

### poetry による Python 環境のセットアップ

- `sh init.sh`

### 依存パッケージ のインストール

- `docker-compose run --entrypoint "poetry install" app`

- 新しい Python パッケージを追加した場合などは以下のようにイメージを再ビルドするだけで、 pyproject.toml に含まれている全てのパッケージをインストールすることができます。

- `docker-compose build --no-cache`

### API の立ち上げ

- `docker-compose up`

### 追加パッケージのインストール

- `docker-compose exec app poetry add {ライブラリ名}`

- docker コンテナの中の Python 環境は、ローカル環境と異なるパス定義となるため、vscode ではそのままではパッケージの参照ができず、エラーの下線が表示されてしまう。そのため、仮想環境に入って、`poetry install or poetry update`をし、インタプリンタを仮想環境のものに変更する必要がある。
