"""
Challenge - 105[Easy]
Given a wordlist of your choosing, make a program to unscramble scrambled words from that list. For sanity and brevity, disregard any words which have ambiguous unscramlings, such as "dgo" unscrambling to both "dog" and "god."
Input:
A file which contains scrambled words and a wordlist to match it against
Output:
The unscrambled words which match the scrambled ones
"""
scrambled_words = ["rodo", "irtdy", "labl", "ksabet", 
                   "agb","ikle"]
f = map(str.strip, open("txtfiles/1000words.txt"))
words = ["".join(sorted(w)) for w in f]
print ["".join(sorted(w)) in words for w in scrambled_words]
