from collections import defaultdict

keypads = {'2': 'ABC', '3': 'DEF', '4': 'GHI',
           '5': 'JKL', '6': 'MNO', '7': 'PQRS',
           '8': 'TUV', '9': "WXYZ"}

def get_letter_count(number):
    """ gets the count of alphabets in a number """
    counts = defaultdict(int)
    alphas = "".join([keypads.get(n) for number in number.split() for n in number])
    alphas = str.lower(alphas)
    for c in alphas:
        counts[c] += 1
    return counts

def get_alpha_count(word):
    """ gets the count of alphabets in a word """
    counts = defaultdict(int)
    for w in word: counts[w] += 1
    return counts

def check_inclusion(dict1, dict2):
    """ returns true if all keys in dict1 are in dict2 """
    for k in dict1.keys():
        if k not in dict2:
            return False
    return True

if __name__ == "__main__":
    number = "7653"
    number_counts = get_letter_count(number)
    valid_words = []
    with open("txtfiles/wordlist.txt") as f:
        for w in f.readlines():
            if check_inclusion(get_alpha_count(w.strip()), number_counts):
                valid_words.append(w.strip())
    print len(valid_words)
