url="https://www.hackerrank.com/challenges/ctci-merge-sort/problem"
#arr=[2,4,1]
def countInversions(arr):
    n = len(arr)
    if n < 2:  # base case: if the array has less than 2 elements
        return 0

    mid = n // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursively count inversions in left and right halves
    inversions = countInversions(left) + countInversions(right)

    # Merge the two halves and count cross inversions
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            inversions += len(left) - i
            j += 1
        k += 1

    # Copy the remaining elements of left, if any
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    # Copy the remaining elements of right, if any
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return inversions


arr = [2, 1, 3, 1, 2]
print(countInversions(arr))  # Output the number of inversions
