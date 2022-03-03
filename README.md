# Doraemon API

## dora_superdatabase seed 作成
root directory で
```
python ./backend/shells/gadgets/dora_superdatabase.py > ./backend/seeds/gadgets/dora_superdatabase.py
```
を実行．ひみつ道具 (`gadgets`) 以外も同様 (後に追加)．

## virtualenv activate
```
. ./dorapi-env/bin/activate
```

## lint
```
flake8 . --count --show-source --statistics --ignore="F401, F403, F405, E111, E114, E121, E402, E501, W293, W503, W504"
```
