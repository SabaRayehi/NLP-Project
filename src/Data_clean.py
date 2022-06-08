import csv
import re
from nltk.tokenize import TreebankWordTokenizer
from nltk.corpus import stopwords
from nltk.tokenize.treebank import TreebankWordDetokenizer


def whiteSpace(res):
    return  re.sub(' +', ' ', res)

def removeStopwords(text):
    words = set(stopwords.words('english'))
    rsw = [i for i in tokens if not i in words]
    return rsw

if __name__ == '__main__':
    with open('train_raw.csv', 'r', encoding='utf-8') as file_reader:
        data =( csv.reader(file_reader)[100])
        new_csv_data = []
        for line in data:
            sentence = line[0]
            res = whiteSpace(sentence)
            text = whiteSpace(re.sub(r'[^a-zA-Z\s]+', '', res))
            tokens = TreebankWordTokenizer().tokenize(text)
            token = removeStopwords(tokens)
            new_csv_data.append([TreebankWordDetokenizer().detokenize(token)])
            with open('cleaned.csv', 'w', encoding='utf-8', newline='') as fd:
                writer = csv.writer(fd)
                writer.writerows(new_csv_data)