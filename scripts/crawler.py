# scripts/crawler.py
# -------------------
# Google画像検索から特定のキーワード（例：子犬）で画像をダウンロードするスクリプト。
#
# 入力:
#   --input_word: 検索キーワード（例: "子犬"）
#   --output_dir: 出力先ディレクトリ（例: dogs）
#   --max_num: 最大ダウンロード件数（例: 100）
# 出力:
#   - 指定フォルダ内に画像ファイルが保存される

import argparse
from icrawler.builtin import GoogleImageCrawler

parser = argparse.ArgumentParser(description="Google画像検索から画像をダウンロードするスクリプト")
parser.add_argument("--input_word", required=True, help="検索キーワード")
parser.add_argument("--output_dir", required=True, help="画像の保存先ディレクトリ")
parser.add_argument("--max_num", type=int, default=100, help="ダウンロードする画像の最大数（デフォルト: 100）")
args = parser.parse_args()

crawler = GoogleImageCrawler(storage={"root_dir": args.output_dir})
crawler.crawl(keyword=args.input_word, max_num=args.max_num)