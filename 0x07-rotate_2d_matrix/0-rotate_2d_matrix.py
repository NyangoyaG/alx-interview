def rotate_2d_matrix(matrix):
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()

# Example usage:
# Create a sample 3x3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Rotate the matrix 90 degrees clockwise in-place
rotate_2d_matrix(matrix)

# Display the rotated matrix
for row in matrix:
    print(row)

