'''
you get a dictionary, a list of words
["bar", "cat", "foo"] and a string "foobar",
and you return T/F if it can be written
using only words in the dictionary
'''

def function(words,s,start,end,result):
    if end == len(s)+1:
        print(result)
        return result == s
    if s[start:end] in words:
        if function(words,s,start,end+1,result):
            return True
        else:
            result += s[start:end]
            start = end
    if function(words,s,start,end+1,result):
        return True

    return False



words = ["bo", "bob", "cat"]
s = "bobcat"
function(words,s,0,0,"")
