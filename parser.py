import argparse
from model import *


def read_code(name):
    with open(name, encoding='utf8') as f:
        file = f.read()
    return file


parser = argparse.ArgumentParser(description='Проверка на антиплагиат')
parser.add_argument('input', type=str, help='Программы для сравнения', nargs=2)
args = parser.parse_args()

anti_plag = Model()

scores = []
try:
    orig, candidate = map(lambda x: Model.preprocessing(read_code(x)), args.input)
    scores.append(anti_plag.predict(orig, candidate))
except SyntaxError:
    scores.append(0)

for score in scores:
    print(score)

