# Function to change all elements of row `x` and column `y` to -1
def changeRowColumn(mat, M, N, x, y):
    for j in range(N):
        if mat[x][j]:
            mat[x][j] = -1

    for i in range(M):
        if mat[i][y]:
            mat[i][y] = -1


# Function to convert the matrix
def convert(mat):
    # base case
    if not mat or not len(mat):
        return

    # `M × N` matrix
    (M, N) = (len(mat), len(mat[0]))

    # traverse the matrix
    for i in range(M):
        for j in range(N):
            if mat[i][j] == 0:  # cell `(i, j)` has value 0
                # change each non-zero element in row `i` and column `j` to -1
                changeRowColumn(mat, M, N, i, j)

    # traverse the matrix once again and replace cells having
    # value -1 with 0
    for i in range(M):
        for j in range(N):
            if mat[i][j] == -1:
                mat[i][j] = 0


if __name__ == '__main__':

    mat = [
        [1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1]
    ]

    # convert the matrix
    convert(mat)

    # print matrix
    for r in mat:
        print(r)
