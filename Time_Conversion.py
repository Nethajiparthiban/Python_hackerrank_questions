url='https://www.hackerrank.com/challenges/time-conversion/problem'
def timeConversion(s):
    meridian=s[-2:]
    if meridian=='PM' and s[:2]!='12':
        s=str(12+int(s[:2]))+s[2:]
    if meridian =='AM' and s[:2]=='12':
        s='00'+s[2:]
    return print(s[:-2])
s='07:01:00PM'
timeConversion(s)