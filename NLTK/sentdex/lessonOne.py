# tokenizeng

from nltk.tokenize import word_tokenize


example_text = "Hello mr. Smith, how are you?"


for i in word_tokenize(example_text):
    print(i)