url="https://www.hackerrank.com/challenges/between-two-sets/problem"
'''we have to find the lcm and common divider'''
from functools import reduce
def getTotalX(a,b):
    def gcd(a,b):
        if b==0:
            return a
        return gcd(b,a%b)
    def lcm(a,b):
        return a*b//gcd(a,b)
    l=reduce(lcm,a)
    g=reduce(gcd,b)

    s=0
    for i in range(l,g+1,l):
        if g%i==0:
            s+=1
    return s
a=[2,6]
b=[24,36]
print(getTotalX(a,b))