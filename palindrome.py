""" Description:
Input Description:
Integer a_start - The starting range of the integer a
Integer a_end - The ending range of the integer a
Integer b_start - The starting range of the integer b
Integer b_end - The ending range of the integer b
Output Description:
Print an integer pair if their product is a palindrome.
Sample Inputs & Outputs:
Let a_start and a_end be 10, 11, and let b_start and b_end be 10, 11. Your code, given these arguments, should print "11, 11", since 11 * 11 is 121, and is a palindrome.
"""

def find_palindrome(a_start, a_end, b_start, b_end):
    a = range(a_start, a_end + 1)
    b = range(b_start, b_end + 1)
    return [i*j for i in a for j in b if str(i*j) == str(i*j)[::-1]]
