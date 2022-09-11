from pickle import dump, load
from os import listdir
from random import randint
import numpy as np

class Model:
    def train(self, input_dir, model_path, N):
        content = []
        if input_dir is None:
            content = [input()]
        else:
            files = listdir(input_dir)
            for file in files:
                reader = open(input_dir + '/' + file, "r")
                content.append([x for x in reader.read().replace('\n', '').split(' ') if x])

        cnt = dict()
        for file in content:
            for j in range(1, N + 1):
                for i in range(N, len(file)):
                    if cnt.get(tuple(file[i - N + j - 1 : i]), None) is not None:
                        cnt[tuple(file[i - N + j - 1 : i])][file[i]] = cnt[tuple(file[i - N + j - 1 : i])].get(file[i], 0) + 1
                    else:
                        cnt[tuple(file[i - N + j - 1 : i])] = dict()
                        cnt[tuple(file[i - N + j - 1 : i])][file[i]] = 1

        new_cnt = dict()
        for k, v in cnt.items():
            total = 0
            new_cnt[k] = dict()
            for word, opa in v.items():
                total += opa
            for word, opa in v.items():
                new_cnt[k][word] = opa / total

        fout = open(model_path, 'wb')
        dump(new_cnt, fout)
        fout.close()
    
    def generate(self, model_path, prefix, length, N):
        fin = open(model_path, 'rb')
        cnt = load(fin)
        fin.close()

        all_words = set()
        for k, v in cnt.items():
            for word in k:
                all_words.add(word)
        all_words = list(all_words)
        result = prefix if prefix is not None else []
        if not result:
            result = [all_words[randint(0, len(all_words) - 1)]]
        while len(result) < length:
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
        return ' '.join(result)
