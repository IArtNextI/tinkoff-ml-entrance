import argparse
from config import N
from model import Model

parser = argparse.ArgumentParser(description='Generate the text')
parser.add_argument('--model', help='Path to trained model')
parser.add_argument('--prefix', metavar="WORD", help='Prefix to begin the generation with', nargs='*')
parser.add_argument('--length', type=int, default=200, help='Length of desired generated text. Default is 200')

args = parser.parse_args()

model = Model()
print(model.generate(args.model, args.prefix, args.length, N))
