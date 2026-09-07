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
        deepCopyhashmap = {None : None}

        current = head
        while current:
            copy = Node(current.val)
            deepCopyhashmap[current] = copy
            current = current.next
        
        current = head
        while current:
            copy = deepCopyhashmap[current]
            copy.next = deepCopyhashmap[current.next]
            copy.random = deepCopyhashmap[current.random]
            current = current.next
        return deepCopyhashmap[head]
