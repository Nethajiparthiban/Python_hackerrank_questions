url="https://www.hackerrank.com/challenges/minimum-swaps-2/problem"
def minimumSwaps(arr):
    swap=0
    visited=[False]*len(arr)#assiging arr to false when it met the range it will b true
    for i in range(len(arr)):
        if visited[i]==False:#ith index is equal to Fales then
            a=i# assiging value for a is equal to i
            b=arr[i]-1 #b value will be index of arr -1
            l=1#assining 1 to the l variable
            visited[i]=True # once the look up is over it visted value will be true
            while b!=i:
                visited[b]=True
                a=b
                b=arr[b]-1
                l+=1
            swap+=l-1
    return print(swap)
arr=[7,1,3,2,4,5,6]
minimumSwaps(arr)