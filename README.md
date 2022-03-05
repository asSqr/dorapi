# Doraemon API
ドラえもんのひみつ道具等のデータを提供します．

## virtualenv activate
```
. ./dorapi-env/bin/activate
```

## dora_superdatabase seed 作成
root directory で
```
python ./backend/shells/gadgets/dora_superdatabase.py > ./backend/seeds/gadgets/dora_superdatabase.py
```
を実行．ひみつ道具 (`gadgets`) 以外も同様 (後に追加)．

## DB リセット / Seed 投入
```
sh ./backend/shells/db_reset.sh
```

## lint
```
flake8 . --count --show-source --statistics --ignore="F401, F403, F405, E111, E114, E121, E402, E501, W293, W503, W504"
```
