"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # hashMap = {}
        # curr = head
        # copyHead = Node(x=head.val)
        # currCopy = copyHead
        # while curr:
        #     print(curr.val, currCopy.val)
        #     hashMap[curr] = currCopy
        #     curr = curr.next
        #     if curr.next:
        #         currCopy.next = Node(x=curr.val)
        #         currCopy = currCopy.next
        #     else:
        #         hashMap[curr] = currCopy
        #         break
        
        # for ori, cop in hashMap.items():
        #     ran = ori.random
        #     if not ran:
        #         cop.random = None
        #     else: 
        #         print(ran.val)
        #         copyRandom = hashMap[ran]
        #         cop.random = copyRandom
        
        # return copyHead

        oldToMap = { None : None }
        curr = head
        while curr:
            copy = Node(x=curr.val)
            oldToMap[curr] = copy
            curr = curr.next

        curr = head
        while curr: 
            copy = oldToMap[curr]
            copy.next = oldToMap[curr.next]
            copy.random = oldToMap[curr.random]
            curr = curr.next
        
        return oldToMap[head]
        


        
