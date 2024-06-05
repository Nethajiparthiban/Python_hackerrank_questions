url="https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem"

def getMedian(countExp,d,mid):
    counter=0
    pos=0
    while counter<mid:
        counter+=countExp[pos]
        pos+=1
    pos-=1
    if counter>mid or d%2 !=0:
        return pos
    else:
        return (2*pos+1)
    return notif
def activityNotifications(expenditure,d):
    countExp=[0]*201
    end=d
    for i in range(0,end):
        countExp[expenditure[i]]+=1
    notif =0

    if d%2==0:
        mid=int(d/2)
    else:
        mid=int(d/2)+1
    length=len(expenditure)
    current=0
    while end<length:
        median=getMedian(countExp,d,mid)
        if expenditure[end]>=2+median:
            notif+=1
        countExp[expenditure[current]]-=1
        countExp[expenditure[end]]+=1
        current+=1
        end+=1
    return print(notif)
expenditure=[10,20,30,40,50]
d=3
activityNotifications(expenditure,d)

