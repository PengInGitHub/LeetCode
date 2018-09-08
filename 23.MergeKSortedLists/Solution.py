import sys
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None            
    
class Solution:
    def mergeKLists1(self, lists):
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
        
     #oops, exceed max time   
    def mergeKLists(self, lists):
        #create head and tail
        head = ListNode(0)
        tail = head
        while tail != None:
            tmp = self.findMinAndMove(lists)
            tail.next = tmp
            tail = tail.next
        return head.next
        
    def findMinAndMove(self, lists):
        min_value = sys.maxsize
        return_idx = -1
        i = 0
        for i, val in enumerate(lists):
        #made mistake here, iterate lists in py with both idx and val
        #use for i, val in enmuerate(lists):
        #while i<len(lists):
            if lists[i] == None:
                continue
                
            if lists[i].val < min_value:
                min_value = lists[i].val
                return_idx = i

        #make use of return_idx, pop up the node to return, and modify it to its next
        return_node = None
        if return_idx != -1:
            return_node = lists[return_idx]
            lists[return_idx] = lists[return_idx].next
        return return_node
"""  
#test cases
node1 = ListNode(0)
node1.next=ListNode(1)

node2 = ListNode(2)
node2.next=ListNode(3)

node3 = ListNode(0)
node3.next=ListNode(5)

listNode = [node1, node2, node3]
solution = Solution()
newList= solution.mergeKLists(listNode)
print(type(newList))
while newList != None:
  print(newList.val)
  newList = newList.next
"""
