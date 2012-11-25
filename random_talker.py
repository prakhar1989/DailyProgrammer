"""
Your program will be responsible for analyzing a small chunk of text, the text of this entire dailyprogrammer description. Your task is to output the distinct words in this description, from highest to lowest count with the number of occurrences for each. Punctuation will be considered as separate words where they are not a part of the word.
The following will be considered their own words: " . , : ; ! ? ( ) [ ] { }
For anything else, consider it as part of a word.
"""
from collections import Counter
import re

def get_top_n_words(file, n):
    with open(file) as f:
        text = f.read()
        regex = re.compile("\w+|[\".,:;!?()[\]{}]")
        words = regex.findall(text)
        return Counter(words).most_common(n)

for w in get_top_n_words("txtfiles/kafka.txt", 10):
    print "%s - %s" % (w[0], w[1])
