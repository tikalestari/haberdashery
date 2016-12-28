'''

Print all possible expressions that evaluate to a target
Given a string that contains only digits from 0 to 9, and an integer value, target.
Find out how many expressions are possible which evaluate to target using binary
operator +, – and * in given string of digits.

Input : "123",  Target : 6
Output : {“1+2+3”, “1*2*3”}

Input : “125”, Target : 7
Output : {“1*2+5”, “12-5”}

'''

def evaluate(string, index, target, current, expressions):
    if target == 0:
        copy = current[:-1]
        expressions.append(copy)
        return

    if index == len(string):
        return

    #don't include
    evaluate(string,index+1,target,current,expressions)

    #add
    num = string[index:index+1]
    current += num + "+"
    evaluate(string,index+1,target-int(num),current,expressions)
    current = current[:-2]

    #subtract
    num = string[index:index+1]
    current += num + "-"
    evaluate(string,index+1,target+int(num),current,expressions)
    current = current[:-2]

    #multiply
    num = string[index:index+1]
    current += num + "*"
    evaluate(string,index+1,target/int(num),current,expressions)
    current = current[:-2]


expressions = []
evaluate("125",0,7,"",expressions)
print(expressions)
