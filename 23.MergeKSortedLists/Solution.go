import (
	"fmt"
	"sort"
)

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

const MaxUint = ^uint(0)
const MinUint = 0
const MaxInt = int(MaxUint >> 1)
const MinInt = -MaxInt - 1

func mergeKLists(lists []*ListNode) *ListNode {
	//head and tail
	head := &ListNode{Val: 0}
	tail := head
	for tail != nil {
		cur := findMinAndMove(lists)
		tail.Next = cur
		tail = tail.Next
	}
	return head.Next
}

func findMinAndMove(lists []*ListNode) *ListNode {
	return_idx := -1
	min_val := MaxInt
	for idx := range lists {
		if lists[idx] == nil {
			continue
		}
		if lists[idx].Val < min_val {
			min_val = lists[idx].Val
			return_idx = idx
		}
	}
	//manipulate ListNode when the return_idx is valid
	if return_idx != -1 {
		returnNode := lists[return_idx]
		lists[return_idx] = lists[return_idx].Next
		return returnNode
	}
	return nil
}

func mergeKLists1(lists []*ListNode) *ListNode {
	allNodes := make([]int, 0)
	for _, node := range lists {
		//made mistake here,
		//ifnode != nil
		for node != nil {
			allNodes = append(allNodes, node.Val)
			node = node.Next
		}
	}
	sort.Ints(allNodes)
	fmt.Println(allNodes)
	head := ListNode{Val: 0}
	tail := &head
	for _, val := range allNodes {
		newNode := ListNode{Val: val}
		tail.Next = &newNode
		tail = tail.Next
	}
	return head.Next
}







