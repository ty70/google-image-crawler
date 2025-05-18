# GoogleImageCrawler を用いた画像収集スクリプト

このスクリプトは、Python ライブラリ `icrawler` の `GoogleImageCrawler` を使用して、Google画像検索から特定のキーワードに基づいた画像を自動でダウンロードします。

---

## 🔧 必要な環境

* Python 3.6 以降
* `icrawler` パッケージ

### インストール手順

```bash
pip install icrawler
```

---

## 🚀 使用方法

1. コマンドラインで実行：

```bash
python scripts/crawler.py --input_word "子犬" --output_dir dogs --max_num 50
```

2. 実行後、指定した `dogs/` フォルダに「子犬」の画像が最大50枚保存されます。

---

## 📁 出力例

```
dogs/
├── 000001.jpg
├── 000002.jpg
├── ...
└── 000050.jpg
```

---

## ⚠️ 注意点

* Google画像検索の仕様変更により、正常に動作しない場合があります。
* 非営利目的での使用を推奨します。著作権・利用規約にご注意ください。

---

## 📚 参考

* [icrawler ドキュメント](https://icrawler.readthedocs.io/en/latest/)

---

## 🧑‍💻 ライセンス

このスクリプトは[MITライセンス](./LICENSE)で提供されます。
