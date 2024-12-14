class Solution:
    def rotate(self, matrix):
        n = len(matrix)

        # Transposition
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reflection ( mirrored acc a specific axis | 90` clockwise )
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]

# Example usage
s = Solution()
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
s.rotate(matrix)

# Print the rotated matrix
for row in matrix:
    print(row)
