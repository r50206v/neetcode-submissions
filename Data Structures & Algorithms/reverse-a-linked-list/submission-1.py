# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # if not head:
        #     return head 

        # new_tail = None
        # while head.next:
        #     temp = ListNode(head.val)
        #     temp.next = new_tail
        #     new_tail = temp

        #     head = head.next

        # ans = ListNode(head.val)
        # ans.next = new_tail
        # return ans



        if not head: 
            return head

        prev, curr = None, head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr 
            curr = tmp
        return prev
            

