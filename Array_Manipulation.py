url="https://www.hackerrank.com/challenges/crush/problem"
def arrayManipulation(n,queries):
    arr=[0]*(n+1)
    for q in queries:
        a=q[0]#q[0] is nothing but it is nested list 0th item which means 1 remember it is in loop
        b=q[1]
        k=q[2]
        arr[a-1]+=k
        if b<len(arr):
            arr[b]-=k
    max=sum=0
    for i in arr:
        sum+=i
        if sum>max:
            max=sum
    return print(max)
n=10
queries=[[1,5,3],[4,8,7],[6,9,1]]
arrayManipulation(n,queries)
