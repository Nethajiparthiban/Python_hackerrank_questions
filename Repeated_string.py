url="https://www.hackerrank.com/challenges/repeated-string/problem"

def repeatedString(s,n):
    ans=0
    for i in s:
        if i=='a':
            ans+=1
    ans=ans*(n//len(s))

    for i in range(n%len(s)):
        if s[i]=='a':
            ans+=1
    return print(ans)

s='abcac'
n=10
repeatedString(s,n)