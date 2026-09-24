# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fp = head
        sp = head
        if not fp or not fp.next:
            return False

        while fp and sp:
            sp = sp.next
            fp = fp.next.next if fp.next else fp.next
            if fp == sp:
                return True
        return False
        