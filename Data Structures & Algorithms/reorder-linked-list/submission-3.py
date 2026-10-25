class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # nodes = deque()
        # curr = head
        # while curr:
        #     nodes.append(curr)
        #     curr = curr.next

        # curr = nodes.popleft()
        # idx = 0
        # while nodes:
        #     if idx % 2 == 0:
        #         nxt = nodes.pop()
        #     else:
        #         nxt = nodes.popleft()
        #     idx += 1
        #     curr.next = nxt
        #     curr = nxt

        # curr.next = None         # break the leftover link
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = None
        while second: 
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp 
        

        first, second = head, prev
        while second: 
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        
        first.next = None



        