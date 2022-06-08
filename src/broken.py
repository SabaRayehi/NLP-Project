import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from operator import itemgetter


file = open('train.csv', encoding='utf-8', errors='ignore')
read_file = file.read()

print(sent_tokenize(read_file))
print(word_tokenize(read_file))
word_count=len(word_tokenize(read_file))
sent_count=len(sent_tokenize(read_file))
words = word_tokenize(read_file)
fdist1 = nltk.FreqDist(words)

filtered_word_freq = dict((word, freq) for word, freq in fdist1.items() if not word.isdigit())

sorted_counts = sorted(filtered_word_freq.items(), key=itemgetter(1))

print("Sentence_count:")
print(sent_count)
print("word_count:")
print(word_count)
print("Unique words_count:")
print(len(filtered_word_freq))
print("sortedFrequency_repetitions of unique words:")
print(sorted_counts)
print("frequency_repetitions of unique words:")
print(filtered_word_freq)

