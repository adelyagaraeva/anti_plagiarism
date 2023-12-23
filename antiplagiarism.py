import argparse
import os

import pandas as pd
from prettytable import PrettyTable

from backend.model import *


def parse_arguments():
    parser = argparse.ArgumentParser(description='Antiplagiarism checker compare files using different metrics. '
                                                 'The program is made specifically to find plagiarism in python code, '
                                                 'but it can also be used with text files in utf-8 encoding')

    parser.add_argument('input', type=str, nargs='+', help='there could be a folder (one path to it) '
                                                           'or two python files (two paths to each file)')

    parser.add_argument('-m', type=str, help='metrics for comparisons',
                        choices=predicting_functions.keys(), nargs='+')
    parser.add_argument('-pandas', type=str, help='path to folder to save results as pandas dataframe '
                                                  '(recommended for folder comparisons). '
                                                  'If not specified, result is printed and is not saved',
                        required=False, nargs=1)

    args_ = parser.parse_args()
    metrics = args_.m

    if not all(os.path.exists(file) for file in args_.input):
        print_color('No such input path exists :(', color='red')
        sys.exit(1)

    return args_.input, metrics, args_.pandas


def save_to_pandas(results, metrics, pandas_convert):
    first, second = [], []
    values = {name: [] for name in metrics}

    for key, row_value in results.items():
        first.append(key[0].split('/')[-1])
        second.append(key[1].split('/')[-1])

        for metric, metric_value in zip(metrics, row_value):
            values[metric].append(metric_value)

    pd.DataFrame({'first': first, 'second': second, **values}).to_csv(
        pandas_convert[0], index=False)


def print_result(results, metrics):
    print_color(f'metrics increasing from plagiarism: '
                f'{[metric for metric in metrics if metric in increasing_from_plagiarism]}', color='red')

    print_color(f'metrics decreasing from plagiarism: '
                f'{[metric for metric in metrics if metric not in increasing_from_plagiarism]}', color='red')

    table = PrettyTable(['first', 'second', *metrics])

    for key, value in results.items():
        table.add_row([key[0].split('/')[-1], key[1].split('/')[-1], *value])

    print(table)


def get_filenames(file_paths):
    parse_dir: bool = len(file_paths) == 1
    try:
        filenames_to_compare = file_paths if not parse_dir else \
            [f'{file_paths[0]}/{file}' for file in os.listdir(file_paths[0]) if
             os.path.isfile(f'{file_paths[0]}/{file}')]
        parse_python: bool = all(file.endswith('.py') for file in filenames_to_compare)

        if not parse_python and any(file.endswith('.py') for file in filenames_to_compare):
            print_color('not all files in folder have extension .py, we compare them as pure strings', color='blue')

        return filenames_to_compare, parse_python

    except FileNotFoundError as e:
        print_color(e, color='red')
        sys.exit(1)


if __name__ == "__main__":
    file_paths, metrics, pandas_convert = parse_arguments()

    if len(file_paths) > 2:
        raise ValueError("More than two arguments in files")

    filenames_to_compare, parse_python = get_filenames(file_paths)

    model = Model(parse_python, metrics)
    results = model.compare_all_files(filenames_to_compare)
    print_result(results, metrics)

    if pandas_convert:
        save_to_pandas(results, metrics, pandas_convert)
