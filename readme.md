# Tinkoff ML entrance exam

This repository contains implementaion of an N-gram model for text generation

There is a **'config.py'** file from which the constant N is derived.

# Usage

To install requirements:
```bash
pip install -r requirements.txt
```

To generate a model file
```sh
python3 train.py [--input-dir INPUT_DIR] [--model MODEL]

arguments:
  --input-dir INPUT_DIR
                        directory to read the training data from
  --model MODEL         path to write out the trained model to
```
To generate text used a saved model file
```sh
python3 generate.py [--model MODEL] [--prefix [WORD [WORD ...]]] [--length LENGTH]

arguments:
  --model MODEL         Path to trained model
  --prefix [WORD [WORD ...]]
                        Prefix to begin the generation with. Default is empty text.
  --length LENGTH       Length of desired generated text. Default is 200
```

# Scripts

This repository also offers pre-written scripts to test out the offered model

## donwload-and-prepare-sample.sh
This script downloads and prepares some files to be used by train.py and puts them into the **'data'** directory

To call:
```bash
./scripts/download-and-prepare-sample.sh
```

## train.sh
This script generates a model with all the files from **'data'** folder and stores it into a **'model'** file.

To call:
```bash
./scripts/train.sh
```

## generate.sh
This script is to be used with parameter that determines the desired length of generated text

For example, following call will generate a text consisting of 200 wordsL
```bash
./scripts/generate.sh 200
```