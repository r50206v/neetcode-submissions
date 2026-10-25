# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        one_step = head
        two_step = None
        if head and head.next and head.next.next:
            two_step = head.next.next

        while one_step and two_step:
            if one_step == two_step:
                return True
            
            one_step = one_step.next
            if two_step.next:
                two_step = two_step.next.next
            else: 
                break
        
        return False