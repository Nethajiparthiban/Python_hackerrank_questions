url="https://www.hackerrank.com/challenges/array-left-rotation/problem"
'''Based on the given steps we have to skip the number of elements and add 
in the end here the given array is 12345 after skiping it will be 34512'''
def rotLeft(a,d):
    res=a[0:d]# this contain no of elemnts we going to rotate
    #here 0 is start end is d means 2
    for i in range(len(a)-d):#here len of a is 5 and d is 2 ., 5-2=3
        a[i]=a[i+d]#array of index is array of index+d
    a[-d:]=res#here it takes the index value -d:complet array means -2:end of array
    return print(a)

a=[1,2,3,4,5]
d=2
rotLeft(a,d)
