# given n, print all combinations of brackets
# ex: 3 ((())) or ()()() or (())() or

def par(n, o, c, s):
    if c == n and o == n:
        print(s)
    if o < n:
        par(n, o + 1, c, s + "(")
    if c < o:
        par(n, o, c + 1, s + ")" )


par(7,0,0,"")
