class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = deque()
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        curr = nodes.popleft()
        idx = 0
        while nodes:
            if idx % 2 == 0:
                nxt = nodes.pop()
            else:
                nxt = nodes.popleft()
            idx += 1
            curr.next = nxt
            curr = nxt

        curr.next = None         # break the leftover link
        