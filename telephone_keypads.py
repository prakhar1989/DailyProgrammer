"""
Problem: http://www.reddit.com/r/dailyprogrammer/comments/1sody4/12113_challenge_139_intermediate_telephone_keypads/
Telephone Keypads commonly have both digits and characters on them. This is to help with remembering & typing phone numbers (called a Phoneword), like 1-800-PROGRAM rather than 1-800-776-4726. This keypad layout is also helpful with T9, a way to type texts with word prediction.
Your goal is to mimic some of the T9-features: given a series of digits from a telephone keypad, and a list of English words, print the word or set of words that fits the starting pattern. You will be given the number of button-presses and digit, narrowing down the search-space.
"""
import re
keypads = ('abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz')
number = "7777 666 555 3"
word = "".join((keypads[int(n[0])-2][len(n)-1] for n in number.split()))
with open("txtfiles/wordlist.txt") as f:
    valid_words = [w.strip() for w in f.readlines() if str.startswith(w.strip(), word)]
    print valid_words
