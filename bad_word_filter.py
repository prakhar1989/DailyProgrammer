"""
Challenge - 100 [Intermediate]
Write a program called 'censor' that takes in one argument on the command line. This argument is the filename of a newline-separated wordlist of profanity
The program should then read a text from standard in, and print it out again, but replacing every instance of a word in the wordlist with a 'censored' version. The censored version of a word has the same first character as the word, and the rest of the characters are replaced with '*'.
For example, the 'censored' version of 'peter' would be 'p****'
usage- echo fuck suck lick dick | bad_word_filter.py 'txtfiles/badwords.txt'
"""
import sys, re
badwords = map(str.strip, open(sys.argv[1]))
text = sys.stdin.read()
regx = re.compile("\w+")
for t in regx.findall(text):
    if t in badwords:
        text = re.sub(t, t[0] + "*"*(len(t)-1), text, flags=re.I)
print text
