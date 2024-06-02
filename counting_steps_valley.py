url="https://www.hackerrank.com/challenges/counting-valleys/problem"
def countingValleys(steps,path):
    valley=0
    current=0
    for i in range(steps):
        previous=current
        if path[i]=='U':
            current+=1
        if path[i]=='D':
            current-=1
        if current==0 and i!=0:
            if previous==-1:
                valley+=1
    return print(valley)
steps=8
path='UDDDUDUU'
countingValleys(steps,path)