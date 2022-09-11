import urllib.request

urllib.request.urlretrieve("https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt", "a.txt")
urllib.request.urlretrieve("https://raw.githubusercontent.com/formcept/whiteboard/master/nbviewer/notebooks/data/harrypotter/Book%201%20-%20The%20Philosopher's%20Stone.txt", "harry.txt")
urllib.request.urlretrieve("https://raw.githubusercontent.com/formcept/whiteboard/master/nbviewer/notebooks/data/harrypotter/Book%202%20-%20The%20Chamber%20of%20Secrets.txt", "2harry.txt")
urllib.request.urlretrieve("https://raw.githubusercontent.com/formcept/whiteboard/master/nbviewer/notebooks/data/harrypotter/Book%203%20-%20The%20Prisoner%20of%20Azkaban.txt", "3harry.txt")