import argparse
from config import N
from random import randint
import numpy as np

parser = argparse.ArgumentParser(description='Train the model')
parser.add_argument('--model', help='Path to trained model')
parser.add_argument('--prefix', metavar="WORD", help='Prefix to begin the generation with', nargs='*')
parser.add_argument('--length', type=int, default=200, help='Length of desired generated text. Default is 200')

args = parser.parse_args()

fin = open(args.model)
opa = fin.read()
cnt = dict()
exec("cnt=" + opa)
fin.close()
all_words = set()
for k, v in cnt.items():
    for word in k:
        all_words.add(word)
all_words = list(all_words)
result = args.prefix if args.prefix is not None else []
while len(result) < args.length:
    if len(result) < N:
        result.append(all_words[randint(0, len(all_words) - 1)])
    else:
        options = cnt.get((tuple(result[-N:])), None)
        if options is None:
            result.append(all_words[randint(0, len(all_words) - 1)])
        else:
            result.append(np.random.choice(list(options.keys()), p=list(options.values())))
print(' '.join(result))
