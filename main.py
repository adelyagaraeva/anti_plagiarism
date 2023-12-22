import argparse
import os

import pandas as pd

from itertools import product
from backend.metrics import *
from backend.model import *


def read_code(name):
    with open(name, encoding='utf8') as f:
        file = f.read()
    return file


def parse_arguments():
    parser = argparse.ArgumentParser(description='Antiplagiarism checker compare files using different metrics. '
                                                 'The program is made specifically to find plagiarism in python code, '
                                                 'but it can also be used with text files in utf-8 encoding')

    parser.add_argument('input', type=str, nargs='+', help='there could be a folder (one path to it) '
                                                           'or two python files (two paths to each file)')

    parser.add_argument('-l', type=str, help='metrics for comparisons',
                        choices=['lev', 'jaro', 'dam-lev'], nargs=1)
    parser.add_argument('-pandas', type=str, help='path to folder to save results as pandas dataframe '
                                                  '(recommended for folder comparisons). '
                                                  'If not specified, result is printed and is not saved',
                        required=False, nargs=1)

    args_ = parser.parse_args()
    return args_.input, args_.l, args_.pandas


args, compare_type, pandas_convert = parse_arguments()
anti_plag = Model()


if len(args) > 2:
    raise ValueError("More than two arguments in files")

parse_dir: bool = len(args) == 1
files_to_compare = args if not parse_dir else [f'{args[0]}/{file}' for file in os.listdir(args[0])]


files_pair = {(pair[0], pair[1]): (read_code(pair[0]), read_code(pair[1])) for pair in
              product(files_to_compare, repeat=2) if pair[0] < pair[1]}

parse_python: bool = all(file.endswith('.py') for file in files_to_compare)

if parse_python:
    files_pair = {(pair[0], pair[1]): (Model.preprocessing(read_code(pair[0])), Model.preprocessing(read_code(pair[1])))
                  for pair in product(files_to_compare, repeat=2) if pair[0] < pair[1]}
else:
    files_pair = {(pair[0], pair[1]): (read_code(pair[0]), read_code(pair[1])) for pair in
                  product(files_to_compare, repeat=2) if pair[0] < pair[1]}


results = {}


for (filename_1, filename_2), (file_1, file_2) in files_pair.items():
    if parse_python:
        alphabet = {word: chr(40 + index) for index, word in enumerate(set(file_1).union(set(file_2)))}
    else:
        alphabet = None

    result = Model.predict(file_1, file_2, predicting_functions[compare_type[0]], alphabet)
    results[(filename_1, filename_2)] = result


if not parse_dir:
    for key, value in results.items():
        print(f'result for {compare_type} is {value}')

else:
    for key, value in results.items():
        print(key[0].split('/')[-1], key[1].split('/')[-1], value)

    if pandas_convert:
        first, second = [], []
        values = []

        for key, value in results.items():
            first.append(key[0].split('/')[-1])
            second.append(key[1].split('/')[-1])
            values.append(value)

        pd.DataFrame({'first': first, 'second': second, f'{compare_type[0]}_metrics': values}).to_csv(
            f'{pandas_convert[0]}/results.csv', index=False)
