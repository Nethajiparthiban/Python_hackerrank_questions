url="https://www.hackerrank.com/challenges/kangaroo/problem"

def kangaroo(x1,v1,x2,v2):
    if x1<x2 and v1<v2:
        return "No"
    else:
        if v1!=v2 and (x2-x1)%(v1-v2):
            return "Yes"
        else:
            return "No"

x1=2
v1=1
x2=1
v2=2
print(kangaroo(x1,v1,x2,v2))
