import argparse
import os
import sys
from itertools import product

import pandas as pd
from prettytable import PrettyTable
from print_color import print as print_color
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

    parser.add_argument('-m', type=str, help='metrics for comparisons',
                        choices=['lev', 'jaro', 'dam-lev'], nargs=1)
    parser.add_argument('-pandas', type=str, help='path to folder to save results as pandas dataframe '
                                                  '(recommended for folder comparisons). '
                                                  'If not specified, result is printed and is not saved',
                        required=False, nargs=1)

    args_ = parser.parse_args()
    return args_.input, args_.m, args_.pandas


args, metrics, pandas_convert = parse_arguments()
anti_plag = Model()

if len(args) > 2:
    raise ValueError("More than two arguments in files")

parse_dir: bool = len(args) == 1
try:
    filenames_to_compare = args if not parse_dir else [f'{args[0]}/{file}' for file in os.listdir(args[0])]
except FileNotFoundError as e:
    print_color(e, color='red')
    sys.exit(1)

parse_python: bool = all(file.endswith('.py') for file in filenames_to_compare)

if parse_python:
    files_to_compare = {filename: Model.preprocessing(read_code(filename)) for filename in filenames_to_compare}
else:
    filenames_to_compare = {filename: read_code(filename) for filename in filenames_to_compare}

lengths = {key: len(value) for key, value in files_to_compare.items()}

files_pair = [(pair[0], pair[1]) for pair in product(filenames_to_compare, repeat=2) if pair[0] < pair[1]]
results = {}

for filename_1, filename_2 in files_pair:
    file_1 = files_to_compare[filename_1]
    file_2 = files_to_compare[filename_2]
    if parse_python:
        alphabet = {word: chr(40 + index) for index, word in enumerate(set(file_1).union(set(file_2)))}
    else:
        alphabet = None

    result = Model.predict(file_1, file_2, predicting_functions[metrics[0]], alphabet)
    results[(filename_1, filename_2)] = result

if not parse_dir:
    for key, value in results.items():
        print(f'result for {metrics[0]} is {value}')

        if 'lev' in metrics or 'dam-lev' in metrics:
            print_color(f'the lower this metric, the higher the probability of plagiarism \n', color='red')
            print(f'the share of non-edited code is {1 - value / max(lengths[key[0]], lengths[key[0]])}')

    if pandas_convert:
        pass


else:
    if 'lev' in metrics or 'dam-lev' in metrics:
        table = PrettyTable(['First', 'Second', metrics[0], 'Non-edit Share'])
        print_color(f'the lower {metrics[0]} metric, the higher the probability of plagiarism', color='red')
    else:
        table = PrettyTable(['First', 'Second', metrics[0]])
        print_color(f'the higher {metrics[0]} metric, the higher the probability of plagiarism', color='red')

    for key, value in results.items():
        if 'lev' in metrics or 'dam-lev' in metrics:
            table.add_row([key[0].split('/')[-1], key[1].split('/')[-1], value,
                           1 - value / max(lengths[key[0]], lengths[key[0]])])
        else:
            table.add_row([key[0].split('/')[-1], key[1].split('/')[-1], value])

    print(table)

    if pandas_convert:
        first, second, values, interpretation = [], [], [], []

        for key, value in results.items():
            first.append(key[0].split('/')[-1])
            second.append(key[1].split('/')[-1])
            values.append(value)

            if 'lev' in metrics or 'dam-lev' in metrics:
                interpretation.append(1 - value / max(lengths[key[0]], lengths[key[0]]))

        if 'lev' in metrics or 'dam-lev' in metrics:
            pd.DataFrame({'first': first, 'second': second, f'{metrics[0]}_metrics': values,
                          'percentage_of_non-edited': interpretation}).to_csv(
                        f'{pandas_convert[0]}/results.csv', index=False)
        else:
            pd.DataFrame({'first': first, 'second': second, f'{metrics[0]}_metrics': values}).to_csv(
                        f'{pandas_convert[0]}/results.csv', index=False)
