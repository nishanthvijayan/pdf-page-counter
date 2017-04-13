#!/usr/bin/env python
from __future__ import division, print_function
import argparse
import os
import re

from terminaltables import AsciiTable


rxcountpages = re.compile(r"/Type\s*/Page([^s]|$)", re.MULTILINE | re.DOTALL)


def print_table(table_data):
    table_data = [["File Name", "Page count"]] + table_data
    ascii_table = AsciiTable(table_data)
    ascii_table.inner_row_border = True
    print (ascii_table.table)


def count_pages(filename):

    data = open(filename, "rb").read()
    return len(rxcountpages.findall(str(data)))



def search(root_dir, recursive_search):
    file_list = []
    for (dirpath, dirnames, filenames) in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(b'.pdf'):
                file_list.append(dirpath.decode('utf-8') + '/' + filename.decode('utf-8'))
        if not recursive_search:
            break
    return file_list


def display_page_sum(file_list):
    page_sum = 0
    result = []
    for file in file_list:
        page_count = str(count_pages(file))
        result.append([file, page_count])
        page_sum += int(page_count)
    result.append(["Total", page_sum])
    print_table(result)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Calculate sum of pages of all pdf files in a given folder"
    )

    parser.add_argument("-r", "--recursive",
                        const=True, default=False, type=bool, nargs='?',
                        help="Recursively search subdirectories as well")

    parser.add_argument("dir", default=".", type=str, nargs='*',
                        help="Directory containing pdf files")

    args = parser.parse_args()
    
    pdf_files = []
    for directory in args.dir:
        if directory.endswith(".pdf"):
            pdf_files.append("./"+directory)
        else :
            pdf_files.extend(search(directory.rstrip("/").encode('utf-8'), bool(args.recursive)))

        
    display_page_sum(pdf_files)
