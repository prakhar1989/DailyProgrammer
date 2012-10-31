"""
Write a function, where given a string of 
arbitrary characters, returns true if 
all brackets (defined as parentheses, square-brackets,
curly-braces, and chevrons) are correctly paired and ordered.
This is to say that all brackets,
if they enclose other brackets, enclose both the 
paired opening and closing characters.
"""

def brackets(a):
    brack_dict = {'(':')','[':']','{':'}','<':'>'}
    return [brack_dict[i] for i in a if i in '([{<'] == [i for i in a[::-1] if i in ')]}>']
    
print brackets("()abc[])")
print brackets("([<{abc123abc}>])")
