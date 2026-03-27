#!/usr/bin/env python3
# Copyright (c) 2026, Kazuhiro FUJIHARA

import pikepdf
import sys
import os

usage = "usage: /path/to/%prog <pdf filename> <start num>"
args = sys.argv

def initialize(args):
    if len(args) != 3:
        print(usage)
        print('need two parameters')
        sys.exit()

    if not os.path.isfile(args[1]):
        print(usage)
        print('need correct filename')
        sys.exit()

    try:
        i = int(args[2])
    except ValueError:
        print(usage)
        print('Please input integer')
        sys.exit()

    return(i)

start_num = initialize(args)
orig_filename = args[1]
base, ext = os.path.splitext(orig_filename)
filename = f"{base}_orig.{ext}"
os.rename(orig_filename, filename)
output_filename = orig_filename

with pikepdf.open(filename) as pdf:
    # 0ページ目から、数値形式で、開始番号を0に設定
    pdf.Root.PageLabels = pikepdf.Dictionary({
        '/Nums': [
            0, 
            pikepdf.Dictionary({
                '/S': pikepdf.Name('/D'), 
                '/St': start_num
            })
        ]
    })
    pdf.save(output_filename)
