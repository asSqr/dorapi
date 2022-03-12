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

## TODO
- スクレイピング失敗してる
```
{
    "id": "7a708dda-57a5-4c92-aa3f-c8655b13fecb",
    "name": "悪魔のイジワールのききめをなくす薬",
    "ruby": "あくまのいじわーるのききめをなくすくすり",
    "desc": "「",
    "mbooks": [
    {
        "id": "e62026d2-91dd-4171-ac4b-26e3f59346f7",
        "series": "tencomi",
        "volume": "第35巻"
    },
    {
        "id": "746aa159-6034-4e53-afe0-d4f41bc5630b",
        "series": "f_land",
        "volume": "第43巻"
    },
    {
        "id": "77a213ed-d777-4e11-baf1-700e8035eb55",
        "series": "f_collect",
        "volume": "第14巻"
    }
    ]
},
```
- `[参照]` リンク未処理
```
{
    "id": "af345077-9612-45d4-94e9-86fab0e60402",
    "name": "ふしぎなめがね",
    "ruby": "ふしぎなめがね",
    "desc": "[参照] あいてをみるだけで、うごかせるめがね",
    "mbooks": []
},
```