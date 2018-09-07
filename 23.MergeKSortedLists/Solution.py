# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        #lists of type ListNode[]
        #step 1, put all ListNode val into a int array
        all_nodes = []
        for node in lists:
            while node is not None:
                all_nodes.append(node.val)
                node = node.next
        #sort list
        all_nodes.sort()
        #step 2, convert int list to ListNode
        head = ListNode(0);#a dummy
        tail = head
        for num in all_nodes:
            node = ListNode(num)
            tail.next = node
            tail = tail.next
        return head.next
        
        
        
        
        
        
        
        
        
        
        
        
        