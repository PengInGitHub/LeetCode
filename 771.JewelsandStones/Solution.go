//ref
//https://stackoverflow.com/questions/18130859/how-can-i-iterate-over-a-string-by-runes-in-go
func numJewelsInStones(J string, S string) int {
	count := 0
	for _, j := range J {
		for _, s := range S {
			if s == j {
				count++
			}
		}
	}
	return count
}