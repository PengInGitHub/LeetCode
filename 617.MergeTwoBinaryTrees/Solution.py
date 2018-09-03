class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        #set t1 as the main tree
        if t1 is not None and t2 is not None:
            #update t1
            #update value
            t1.val += t2.val
            #update left
            t1.left = self.mergeTrees(t1.left, t2.left)
            #update right
            t1.right = self.mergeTrees(t1.right, t2.right)
            
            return t1
        return t1 if t2 is None else t2