func hammingDistance(x int, y int) int {
	count := 0
	for i := 0; i < 31; i++ {
		x_bin, y_bin := x%2, y%2
		if x_bin != y_bin {
			count++
		}
		x, y = x/2, y/2
	}
	return count
}