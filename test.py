import re
from sys import argv
value = "7653"
layout = ('[abc]', '[def]', '[ghi]', '[jkl]', '[mno]', '[pqrs]', '[tuv]', '[wxyz]')
keys = ''.join(layout[k-2] for k in map(int, value))
print keys
#wlist = open("txtfiles/wordlist.txt", 'r').read()
# print '\n'.join(re.findall('^%s.*$' % keys, wlist, re.MULTILINE))