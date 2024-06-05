def countSwaps(a):
    swap=0
    for i in range(len(a)-1):
        for j in range(i,len(a)):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
                swap+=1
    print("Array is sorted in numSwaps",swap,"swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[-1])
    return
a=[6,4,1]
countSwaps(a)
