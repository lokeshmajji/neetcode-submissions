# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pointers approach
        # left pointer and right pointers should have distance of n
        # right goes until it is end of the list
        # use a dummy pointer to get the left node of the left pointer as we need to delete the 
        # node at the left pointer
        # we increment the left and right pointers until we reach the end of the list
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next

        # delete the node at left
        left.next = left.next.next

        return dummy.next