/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func mergeTrees(t1 *TreeNode, t2 *TreeNode) *TreeNode {
	if t1 != nil && t2 != nil {
		//create a new node
		val := t1.Val + t2.Val
		node := &TreeNode{Val: val}
		node.Left = mergeTrees(t1.Left, t2.Left)
		node.Right = mergeTrees(t1.Right, t2.Right)
		return node
	}
	if t1 != nil {
		return t1
	}
	return t2
}

































