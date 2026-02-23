"""" the problem statement were asking about if two word contains all similar letters 
    then it is anagram else not. so frst we sort the both words and check
    it is equal or not it takes o(n log n) in time and o(n) in space
    
"""

def anangram(s,t):
    if sorted(t) != sorted(s):
        return False
    return True

""" the next approach is using a counter library which is the subcalss 
    of dict in python its also very similar to the hashmap 
    and it gives o(n) in time and o(k) in space if you have max
    26 char so its a constant space.
"""
from collections import Counter
def anagram(s,t):
    if Counter(s) != Counter(s):
        return False
    return True

"""
    we move to next approach and that is the optimize one so here
    we creating two hashmap for storing thos two strings
    and its iterate through the character and increament the count
    then we check if the counts are equal we return true else
    false so for this problem it takes o(n+m) which both length is
    same so it takes o(n) in time effectively and o(n) in space.
"""
def anagaram(s,t):
    if len(s) != len(t) :   #edgecase
        return False
    first = {}
    sec = {}
    for ch in s:
        if ch in first:
            first[ch] += 1
        else:
            first[ch] = 1 
    for ch in t:
        if ch in sec:
            sec[ch] += 1
        else:
            sec[ch] = 1
    if first != sec :
        return False
    else:
        return True
    
""" 
    here same optimize one but doing with single hash map
    which better for space . so here we are creating a one hash map
    and check the character if that char in dic we increament 
    else we retuen and for another string we check the ch in 
    the same dict if the ch is not in that immediately return false
    if ch in dict we decreament values so if both has same ch 
    it value should be 0 finally we check the value is 0 or not
    if 0 return true else false  it take o(n) in time and o(n) in space.
    
"""


def anagram(s,t):
    if len(s) != len(t):
        return False
    seen = {}
    for ch in s :
        if ch in seen:                 # here you can use get() builtin also
            seen[ch] += 1              #seen[ch] = seen.get(ch,0) + 
            
        else: 
            seen[ch] =1 
    for ch in t:
        if ch not in seen:
            return False
        seen[ch] -= 1
        if seen[ch] < 0 :
            return False
    return True


    