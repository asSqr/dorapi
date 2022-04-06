# Doraemon API
[![codecov](https://codecov.io/gh/asSqr/dorapi/branch/main/graph/badge.svg?token=beNGa1fXR3)](https://codecov.io/gh/asSqr/dorapi)

ドラえもんのひみつ道具等のデータを提供します．

## virtualenv activate
```
. ./dorapi-env/bin/activate
```

## `.env` ファイル作成
直下に作成．内容は以下：
```
#!/bin/bash

# [ENV]
ENV=local

# [DB]
DB_NAME=dorapi
DB_USERNAME=admin
DB_PASSWORD=password
DB_ENDPOINT=db
DB_PORT=5432

# [Django]
SECRET_KEY=...

# Google Custom Search
CSE_ID=...          # Custom Search Engine ID
GOOGLE_API_KEY=...
```

`SECRET_KEY` は任意 (例：`@gey=ud2=ry+_3_u(=jsh9b*y743i=8odr@4ocx5tt*^n6)bqi`)
`CSE_ID` と `GOOGLE_API_KEY` は Google Custom Search API の使用法を参照．

## dora_superdatabase seed 作成
root directory で
```
python ./backend/shells/gadgets/dora_superdatabase.py > ./backend/seeds/gadgets/dora_superdatabase.py
```
を実行．ひみつ道具 (`gadgets`) 以外も同様 (後に追加)．

その後，`image_url` 等は
```
python ./backend/shells/custom_search/custom_search.py > ./backend/seeds/gadgets/_dora_superdatabase.py
mv ./backend/seeds/gadgets/_dora_superdatabase.py ./backend/seeds/gadgets/dora_superdatabase.py
```
で取得．

## DB リセット / Seed 投入
```
sh ./backend/shells/db_reset.sh
```

## lint
```
flake8 . --count --show-source --statistics --ignore="F401, F403, F405, E111, E114, E121, E402, E501, W293, W503, W504"
```

## deploy for Heroku (自分用メモ)
Heroku へログイン

```
heroku login
```

docker イメージを push
```
cd ./backend
heroku container:push web -a dorapi
heroku release:push web -a dorapi
```

必要なら
```
heroku ps:scale web=1 -a dorapi
```

DB データをローカルからコピー
```
PGUSER=$DB_USERNAME PGPASSWORD=$DB_PASSWORD PGHOST=127.0.0.1 heroku pg:push dorapi DATABASE_URL --app dorapi
```
