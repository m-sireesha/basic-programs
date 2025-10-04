
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    transpose = []

    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transpose.append(new_row)

    return transpose

# Example
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print("Original matrix:", matrix)
print("Transposed matrix:", transpose_matrix(matrix))
