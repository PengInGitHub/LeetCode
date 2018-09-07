/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        //int list to store all nodes val
        List<Integer> all_nodes = new ArrayList<Integer>();
        //iterate over ListNode
        for(ListNode node : lists){
            while(node != null){
                all_nodes.add(node.val);
                node = node.next;
            }
        }
        
        Collections.sort(all_nodes);
        
        //convert int list to ListNode
        ListNode head = new ListNode(0);
        ListNode tail = head;
        //made mistake here
        //1. use Integer val : all_nodes, not for i
        //2. tail should be a node instead of a int
        /*for (int i=0; i<len(all_nodes); i++){
            tail.val = all_nodes[i];
            tail = tail.next     
        }*/
        for(Integer val : all_nodes){
            ListNode node = new ListNode(val);
            tail.next = node;
            tail = tail.next;
        }
        return head.next;
    }
}










