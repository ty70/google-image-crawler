# Image Collection Script Using GoogleImageCrawler

This script uses the `GoogleImageCrawler` from the Python library `icrawler` to automatically download images from Google Images based on specified keywords.

---

## 🔧 Requirements

* Python 3.6 or higher
* `icrawler` package

### Installation

```bash
pip install icrawler
```

---

## 🚀 Usage

1. Run from the command line:

```bash
python scripts/crawler.py --input_word "puppy" --output_dir dogs --max_num 50
```

2. After execution, up to 50 images of "puppy" will be saved in the specified `dogs/` folder.

---

## 📁 Output Example

```
dogs/
├── 000001.jpg
├── 000002.jpg
├── ...
└── 000050.jpg
```

---

## ⚠️ Notes

* The script may not work properly if Google Images changes its specifications.
* Recommended for non-commercial use. Please be aware of copyright and usage policies.

---

## 📚 Reference

* [icrawler Documentation](https://icrawler.readthedocs.io/en/latest/)

---

## 🧑‍💻 License

This script is provided under the [MIT License](./LICENSE).
