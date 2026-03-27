# 目的
- 問題集をPDF化して，間違えたところだけ印刷して復習しているのですが，基本的に問題集のページ番号とPDFのページ番号を合わせることで（＝p.1から全Scan）印刷したいページをすぐに探せるようにしています．
- しかし，表紙の裏にも大切なことが書いてあったり，ページ数が多すぎて分割したりした場合などは問題集のページ番号とPDFのページ番号が合わなくなり，印刷したいページを探すのが少し手間になります．
- そこで，問題集のページ番号とPDFのページ番号を合わせるためのツールを作りました．


# 環境
- macOS Tahoe 26.3.1 / Mac mini(2020)
- python3.9.6
- pikepdf9.11.0

# 使い方
- `/path/to/mod_pagelabel.py <pdf file> <start No>`
  - もしくは`python3 mod_pagelabel.py <pdf file> <start No>`
    - このときは実行権限はつけなくて可
- もとのpdfファイルは，ファイル名が`filename.pdf`の場合，`filename_orig.pdf`に変更されます．
- 出力ファイルは，元のファイル名（`filename.pdf`）になります．

# Installation
- pikepdfをインストール(venvの環境のほうが安全かと思います)
  - `pip install pikepdf`
- 実行権限をつける
  - `chmod a+x mod_pagelabel.py`