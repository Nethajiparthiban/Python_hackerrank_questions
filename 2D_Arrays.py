url="https://www.hackerrank.com/challenges/2d-array/problem"
def hourglassSum(arr):
    max=-float('inf') #lowest possible numbere
    for i in range(1,5):#row
        for j in range(1,5):#column
            sum=0#initializing sum
            sum+=arr[i][j] #adding the center element
            sum+=arr[i-1][j-1]+arr[i-1][j]+arr[i-1][j+1]#it is for abc one
            #row above one column left right side one element
            sum += arr[i + 1][j - 1] + arr[i + 1][j] + arr[i + 1][j + 1]
            #to take the bottom row "efg" we assiginig all i values to possitive

            if sum>max:
                max=sum
    return max
#hourglassSum()
