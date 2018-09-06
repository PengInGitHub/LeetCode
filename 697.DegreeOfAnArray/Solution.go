const MaxUint = ^uint(0)
const MinUint = 0
const MaxInt = int(MaxUint >> 1)
const MinInt = -MaxInt - 1

func findShortestSubArray(nums []int) int {
	starts, ends, counts := make(map[int]int), make(map[int]int), make(map[int]int)
	maxCount, res := MinInt, MaxInt

	//iterate nums
	for idx, num := range nums {
		if _, ok := starts[num]; !ok {
			starts[num] = idx
			counts[num] = 0
		}
		//if not first time
		counts[num]++
		ends[num] = idx
		//update maxCount
		maxCount = max(maxCount, counts[num])
	}

	//iterate counts map (dict)
	for num, count := range counts {
		if count == maxCount {
			res = min(res, ends[num]-starts[num]+1)
		}
	}
	return res
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}