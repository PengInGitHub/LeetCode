import "sort"
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeKLists(lists []*ListNode) *ListNode {
    allNodes := make([]int, 0)
    for _, node := range lists{
        //made mistake here,
        //ifnode != nil
        for node != nil{
            allNodes = append(allNodes, node.Val)
            node = node.Next
        }
    }
    sort.Ints(allNodes)
    fmt.Println(allNodes)
    head := ListNode{Val:0}
    tail := &head
    for _, val := range allNodes{
        newNode := ListNode{Val:val}
        tail.Next = &newNode
        tail = tail.Next
    }
    return head.Next
}