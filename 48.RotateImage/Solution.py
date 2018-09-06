class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        #two steps 1.rotate 2.swap cols
        #step 1.rotate matrix by diagonal aka matrix[i][i]
        n = len(matrix)
        for i in range(n):
            #j ranges from 0 to i instead to n, b/c that would rotate the rotated matrix back
            for j in range(i):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
        
        #step 2: swap first n/2 cols by matrix[i][j] = matrix[i][n-1-j]
        for i in range(n):
            for j in range(n//2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[i][n-1-j]
                matrix[i][n-1-j] = tmp
        