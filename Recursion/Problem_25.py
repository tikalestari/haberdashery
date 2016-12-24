'''
you get a dictionary, a list of words
["bar", "cat", "foo"] and a string "foobar",
and you return T/F if it can be written
using only words in the dictionary
'''

def function(words,s,start,end,result):
    if s[start:end] in words:
        result += s[start:end]
        start = end
    if end == len(s):
        if result == s:
            print("True")
            return True
        else:
            print("False")
            return False
    function(words,s,start,end+1,result)



words = ["bar", "cat", "foo"]
s = "foobar"
function(words,s,0,0,"")
