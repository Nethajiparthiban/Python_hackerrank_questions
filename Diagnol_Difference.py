matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n = len(matrix)
left = right = 0

for i in range(n):
    left += matrix[i][i]# The primary diagonal elements are matrix[0][0],
    # matrix[1][1], and matrix[2][2] which are 1, 5, and 9 respectively.
    right += matrix[i][n-1-i]#diagonal elements are matrix[0][2],
    # matrix[1][1], and matrix[2][0] which are 3, 5, and 7 respectively.

out = abs(left - right)

print(out)
