import argparse
from config import N
from model import Model

parser = argparse.ArgumentParser(description='Train the model')
parser.add_argument('--input-dir', help='directory to read the training data from')
parser.add_argument('--model', help='path to write out the trained model to')

args = parser.parse_args()

model = Model()
model.train(args.input_dir, args.model, N)
