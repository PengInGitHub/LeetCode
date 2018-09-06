func rotate(matrix [][]int) {
	//step 1, rotate matrix
	n := len(matrix)

	for i := 0; i < n; i++ {
		for j := i; j < n; j++ {
			tmp := matrix[i][j]
			matrix[i][j] = matrix[j][i]
			matrix[j][i] = tmp
		}
	}
	//step 2, swap cols
	for i := 0; i < n; i++ {
		for j := 0; j < n/2; j++ {
			tmp := matrix[i][j]
			matrix[i][j] = matrix[i][n-j-1]
			matrix[i][n-j-1] = tmp
		}
	}

}