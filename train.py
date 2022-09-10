import argparse
from os import listdir

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

print(content)