import "sort"

func triangleNumber(nums []int) int {
	if nums == nil || len(nums) == 0 {
		return 0
	}

	counter := 0
	//sort slice
	sort.Ints(nums)

	//iterate index of the 3rd edge, nums[3rd_idx] has to be larger than nums[2nd_idx] + nums[1st_idx]
	for third_edge_idx := 2; third_edge_idx < len(nums); third_edge_idx++ {
		first_edge_idx := 0
		second_edge_idx := third_edge_idx - 1
		//second_edge_idx, the right pointer while the first_edge_idx works as the left pointer
		//iterate over condition that two pointers do not overlap
		for first_edge_idx < second_edge_idx {
			//model the condition
			if nums[first_edge_idx]+nums[second_edge_idx] > nums[third_edge_idx] {
				counter += second_edge_idx - first_edge_idx
				second_edge_idx--
			} else {
				first_edge_idx++
			}
		}

	}
	return counter
}