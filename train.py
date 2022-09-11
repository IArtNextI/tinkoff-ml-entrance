import argparse
from os import listdir
from config import N

parser = argparse.ArgumentParser(description='Train the model')
parser.add_argument('--input-dir', help='directory to read the training data from')
parser.add_argument('--model', help='path to write out the trained model to')

args = parser.parse_args()

content = []
if args.input_dir is None:
    content = [input()]
else:
    files = listdir(args.input_dir)
    for file in files:
        reader = open(args.input_dir + '/' + file, "r")
        content.append([x for x in reader.read().replace('\n', '').split(' ') if x])

cnt = dict()
for file in content:
    for i in range(2, len(file)):
        if cnt.get(tuple(file[i - N : i]), None) is not None:
            cnt[tuple(file[i - N : i])][file[i]] = cnt[tuple(file[i - N : i])].get(file[i], 0) + 1
        else:
            cnt[tuple(file[i - N : i])] = dict()
            cnt[tuple(file[i - N : i])][file[i]] = 1

new_cnt = dict()
for k, v in cnt.items():
    total = 0
    new_cnt[k] = dict()
    for word, opa in v.items():
        total += opa
    for word, opa in v.items():
        new_cnt[k][word] = opa / total

fout = open(args.model, 'w')
print(new_cnt, file=fout)
fout.close()