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

        if not head: 
            return None 
        if n == 1 and not head.next:
            return None
        
        first = head
        first_idx = n
        while first_idx > 0:
            first = first.next
            first_idx -= 1

        if not first:
            return head.next

        second = head
        while first.next:
            first = first.next
            second = second.next
        print(second.val)

        if second.next and second.next.next:
            second.next = second.next.next
        else:
            second.next = None
        
        return head

