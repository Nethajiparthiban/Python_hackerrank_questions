url="https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem"
def jumpingOnClouds(c):
    jump=0
    c.append(1)
    if len(c)<3:
        return 0
    i=0
    while i<len(c)-2:
        if c[i+2]==0:
            i+=2
        else:
            i+=1
        jump+=1
    return print(jump)
c=[0,0,1,0,0,1,0]
jumpingOnClouds(c)

