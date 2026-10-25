class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodeList = []
        curr = head
        while curr:
            nodeList.append(curr)
            curr = curr.next

        curr = nodeList.pop(0)   # the original head stays first
        idx = 0
        while nodeList:
            if idx % 2 == 0:
                nxt = nodeList.pop(-1)
            else:
                nxt = nodeList.pop(0)
            idx += 1
            curr.next = nxt
            curr = nxt

        curr.next = None         # break the leftover link
        