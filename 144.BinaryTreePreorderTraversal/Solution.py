#144. Binary Tree Preorder Traversal

#definition of a binary tree
class BinaryTree:
#mistake made here, class BinaryTree(self)
#declare a class needs no () and keyword self
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #constructor
    def __init__(self):
        self.res = []
    
    #recursion version #1
    #root of type BinaryTree
    def preorderTraversalRe1(self, root):
        #global variable res
        res = []
        def dfs(root):
            if root:
                res.append(root.val)
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        return res

    #recursion version #2
    def preorderTraversalRe2(self, root):
        res = []
        def dfs(root, res):
            if root:
                res.append(root.val)
                dfs(root.left, res)
                dfs(root.right, res)
            return res
        return dfs(root, res)

    #recursion version #3
    #no helper func, recurse itself
    def preorderTraversalRe3(self, root):
        if root:
            self.res.append(root.val)
            self.preorderTraversalRe3(root.left)
            self.preorderTraversalRe3(root.right)
        return self.res
    
    #iteration version
    #use stack
    def preorderTraversal(self, root):
    #made mistake here preorderTraversal(root):
    #func in class should have self
        res = []
        stack = [root]
        #remember stack is Last In First Out
        while stack:
            node = stack.pop()
            if node:  
            #made mistake here, if node: is forgoten             
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res
