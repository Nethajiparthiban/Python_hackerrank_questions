url="https://www.hackerrank.com/challenges/special-palindrome-again/problem"
def substrCount(n,s):
    l=[]#contain count of char in r8 order
    count=0
    ch=None#store the character

    for i in range(n):
        if s[i]==ch:#store each caracter at i
            count+=1
        else:
            if ch is not None:
                l.append((ch,count))
            ch=s[i]
            count=1
    l.append((ch,count))#

    ans=0
    for i in l:
        ans+=(i[1])*(i[1]+1)//2# counting all the digits

    for i in range(1,len(l)-1):#pallindromic part
        if l[i-1][0]==l[i+1][0] and l[i][1]==1:
            ans+=min(l[i-1][1],l[i+1][1])
    return ans

n=7
s="abcbaba"
print(substrCount(n,s))

