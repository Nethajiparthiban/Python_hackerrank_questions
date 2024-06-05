url="https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem"
def sherlockAndAnagrams(s):
    res=0#initializing res variable for count
    for i in range(1,len(s)): #loop for check the substrings
        d={}# count the anagram chracters
        for j in range(len(s)-i+1):# looping to run string backwards
            sub=''.join(sorted(s[j:j+1]))
            if sub not in d:
                d[sub]=1
            else:
                d[sub]+=1
            res+=d[sub]-1
    return print(res)
s='abba'
sherlockAndAnagrams(s)
