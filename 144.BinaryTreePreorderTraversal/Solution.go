/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

//recursion version
func preorderTraversal(root *TreeNode) []int {
    if root == nil{return nil}

    res := []int{root.Val}
    l := preorderTraversal(root.Left)
    r := preorderTraversal(root.Right)
    
    res = append(res, l...)
    res = append(res, r...)
    
    return res
}
