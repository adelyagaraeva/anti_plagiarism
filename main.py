import argparse
import os
import jellyfish
from itertools import product
from backend.model import *


def read_code(name):
    with open(name, encoding='utf8') as f:
        file = f.read()
    return file


def parse_arguments():
    parser = argparse.ArgumentParser(description='Antiplagiarism checker')
    parser.add_argument('input', type=str, help='two programmes or folder name to compare files in it',
                        nargs='+', metavar='N')
    parser.add_argument('-l', type=str, help='way of comparison',
                        choices=['lev', 'jaro', 'dam-lev'], nargs=1)
    args_ = parser.parse_args()
    return args_.input, args_.l


args, compare_type = parse_arguments()
parse_dir = len(args) == 1

if len(args) > 2:
    raise ValueError("More than two arguments in files")

files_to_compare = args if not parse_dir else [args[0] + '/' + file for file in os.listdir(args[0])]
parse_python = all(file.endswith('.py') for file in files_to_compare)

anti_plag = Model()
compare_pair = [pair for pair in product(files_to_compare, repeat=2) if pair[0] < pair[1]]
results = {}
predicting_functions = {'lev': jellyfish.levenshtein_distance,
                        'dam-lev': jellyfish.damerau_levenshtein_distance,
                        'jaro': jellyfish.jaro_similarity}

for pair in compare_pair:
    if parse_python:
        first = Model.preprocessing(read_code(pair[0]))
        second = Model.preprocessing(read_code(pair[1]))
        alphabet = {word: chr(40 + index) for index, word in enumerate(set(first).union(set(second)))}

    else:
        first, second = read_code(pair[0]), read_code(pair[1])
        alphabet = None

    result = Model.predict(first, second, predicting_functions[compare_type[0]], alphabet)
    results[(pair[0], pair[1])] = result

if not parse_dir:
    for key, value in results.items():
        print(value)
else:
    for key, value in results.items():
        print(key[0].split('/')[-1], key[1].split('/')[-1], value)
