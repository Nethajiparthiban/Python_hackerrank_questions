def countTriplets(arr,r):
    list1=arr
    count=0
    for i in range(len(list1)-1):
        for j in list1[i+1:len(list1)]:
            if j/list1[i]==r:
                for k in list1[list1.index(j)+1:len(list1)]:
                    if k/j==r and k/list1[0]==r*j:
                        count+=1
    return print(count)
arr=[1,4,16,64]
r=4
countTriplets(arr,r)