'''
Given a string, determine if it fits a pattern.
Ex: "redbluebluegreen" fits "abbc"
Idea: try all possible substrings
and see if that ordering of substrings
matches that pattern
"red" maps to "a"
"blue" maps to "b"
"green" maps to c
and then it's valid
'''

def pattern(s):
    
