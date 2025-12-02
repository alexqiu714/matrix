matrix = [[1, 2, 3], [4, 5, 6], [6, 7, 8]]
print(len(matrix)) #to calculate rows
print(len(matrix[0])) #to calculate columns
print((matrix[0][2]))
print((matrix[2][1]))
print(matrix)

for row in range(3):
    for col in range(3):
        print(matrix[row][col], end = " " )
    print("\n")

matrixA = [[1, 2], [3, 4]]
matrixB = [[6, 7], [8, 9]]
sum = [[0, 0], [0, 0]]

for row in range(2):
    for col in range(2):
        sum[row][col] = matrixA[row][col] + matrixB[row][col]

for row in range(2):
    for col in range(2):
        print(sum[row][col], end = " ")
    print("\n")