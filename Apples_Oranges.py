
def countApplesAndOranges(s, t, a, b, apples, oranges):
    total_apples=total_oranges=0
    for i in range(len(apples)):
        if s<=a+apples[i]<=t:
            total_apples+=1
    for i in range(len(oranges)):
        if s<=b+oranges[i]<=t:
            total_oranges+=1
    print(total_apples)
    print(total_oranges)
    return
s=7
t=10
a=4
b=12
apples=[2,3,-4]
oranges=[3,-2,-4]
countApplesAndOranges(s,t,a,b,apples,oranges)