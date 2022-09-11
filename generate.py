import argparse
from config import N
from random import randint
import numpy as np
from pickle import load

parser = argparse.ArgumentParser(description='Generate the text')
parser.add_argument('--model', help='Path to trained model')
parser.add_argument('--prefix', metavar="WORD", help='Prefix to begin the generation with', nargs='*')
parser.add_argument('--length', type=int, default=200, help='Length of desired generated text. Default is 200')

args = parser.parse_args()

fin = open(args.model, 'rb')
cnt = load(fin)
fin.close()

all_words = set()
for k, v in cnt.items():
    for word in k:
        all_words.add(word)
all_words = list(all_words)
result = args.prefix if args.prefix is not None else []
if not result:
    result = [all_words[randint(0, len(all_words) - 1)]]
while len(result) < args.length:
    done = False
    for j in range(N, 0, -1):
        options = cnt.get((tuple(result[-j:])), None)
        if options is None:
            continue
        else:
            result.append(np.random.choice(list(options.keys()), p=list(options.values())))
            done = True
            break
    if not done:
        result.append(all_words[randint(0, len(all_words) - 1)])

print(' '.join(result))
