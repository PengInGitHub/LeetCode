/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        
        List<Integer> res = new ArrayList<Integer>();
        if(root == null){
            return res;
        }        
        res.add(root.val);
        List<Integer> left = preorderTraversal(root.left);
        List<Integer> right = preorderTraversal(root.right);
        
        if (left != null){
            res.addAll(left);            
        }
        if (right != null){
            res.addAll(right);            
        }    
        
        return res;
        
    }
}