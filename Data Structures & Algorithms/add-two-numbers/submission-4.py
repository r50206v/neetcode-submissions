# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.add(l1, l2, 0)
        
        # ans = l1
        # carry = 0
        # while l1 and l2: 
        #     num = l1.val + l2.val + carry
        #     l1.val = num % 10
        #     carry = num // 10

        #     if not l1.next and l2.next: 
        #         l1.next = ListNode(val=0)
        #     elif l1.next and not l2.next: 
        #         l2.next = ListNode(val=0)
        #     elif not l1.next and not l2.next and carry > 0:
        #         l1.next = ListNode(val=carry)

        #     l1 = l1.next
        #     l2 = l2.next
        
        # return ans
            
    def add(self, l1, l2, carry):
        if not l1 and not l2 and carry == 0:
            return None 

        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        val = (v1 + v2 + carry) % 10
        carry = (v1 + v2 + carry) // 10

        next_node = self.add(
            l1.next if l1 else None, 
            l2.next if l2 else None, 
            carry
        )
        return ListNode(val=val, next=next_node)


    
        