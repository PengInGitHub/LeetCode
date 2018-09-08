/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeKLists1(ListNode[] lists) {
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

    public ListNode mergeKLists(ListNode[] lists){
        //create head and tail
        ListNode head = new ListNode(0);
        ListNode tail = head;
        ListNode tmp = null;
        while (tail != null){
            tmp = findMinAndMove(lists);
            tail.next = tmp;
            tail = tail.next;
        }
        return head.next;
    }
	private ListNode findMinAndMove1(ListNode[] lists) {
		int min_value = Integer.MAX_VALUE;
		int ret_i = -1;
		for (int i = 0; i < lists.length; i++) {
			if (lists[i] == null) {
				continue;
			}

			if (lists[i].val < min_value) {
				min_value = lists[i].val;
				ret_i = i;
			}
		}

		ListNode ret_node = null;
		if (ret_i != -1) {
			ret_node = lists[ret_i];
			lists[ret_i] = lists[ret_i].next;
		}

		return ret_node;
	}    
    
    private ListNode findMinAndMove(ListNode[] lists){
        //iterate lists, use index
        //to get return index of the lists
        int min_value = Integer.MAX_VALUE; 
        int return_idx = -1;

        for(int i=0; i<lists.length; i++){
            if(lists[i]==null){
                continue;
            }
            
            if(lists[i].val<min_value){
                min_value = lists[i].val;
                return_idx = i;
            }
        }
        //with the return index
        //manipulate single ListNode
        //find the return Node
        ListNode return_node = null;
        if(return_idx != -1){
            return_node = lists[return_idx];
            lists[return_idx] = lists[return_idx].next;
        }
        return return_node;
            
        }
    }








