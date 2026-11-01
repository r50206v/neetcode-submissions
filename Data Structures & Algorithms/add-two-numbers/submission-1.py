# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        '''
        221 => 122
        999 => 999
        1220 => 0221

        999 => 999
        999 => 999
        1998 => 8991
        '''

        ans = l1
        carry = 0
        while l1 and l2: 
            num = l1.val + l2.val + carry
            l1.val = num % 10
            carry = num // 10

            if not l1.next and l2.next: 
                l1.next = ListNode(val=0)
            elif l1.next and not l2.next: 
                l2.next = ListNode(val=0)
            elif not l1.next and not l2.next and carry > 0:
                l1.next = ListNode(val=carry)

            l1 = l1.next
            l2 = l2.next
        
        return ans
            

        