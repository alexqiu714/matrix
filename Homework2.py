matrixC = [[1, 2], [3, 4]]
matrixD = [[6, 7], [8, 9]]

dif = [[0, 0], [0, 0]]

for row in range(2):
    for col in range(2):
        dif[row][col] = matrixC[row][col] - matrixD[row][col]

for row in range(2):
    for col in range(2):
        print(dif[row][col], end = " ")
    print("\n")