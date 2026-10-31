# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # if not head:
        #     return None

        # orderList = []
        # curr = head
        # while curr:
        #     orderList.append(curr)
        #     curr = curr.next
        
        # idx = len(orderList) - n
        # if idx == 0:
        #     return head.next

        # curr = head
        # while idx > 0:
        #     if idx == 1 and n > 1:
        #         curr.next = curr.next.next
        #         break
        #     elif idx == 1 and n == 1:
        #         print(curr.val)
        #         curr.next = None
        #         break
            
        #     curr = curr.next
        #     idx -= 1

        # return head

        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right: 
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next
