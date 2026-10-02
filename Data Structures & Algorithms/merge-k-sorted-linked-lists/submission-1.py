# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        res = lists
        while len(res) > 1:
            sres = []
            for i in range(0, len(res),2):
                l1 = res[i]
                l2 = res[i+1] if i + 1 < len(res) else None
                # print("l1:", l1 , " l2:", l2)
                merged = self.mergeList(l1, l2)
                # print("merged", merged)
                sres.append(merged)
            # print("mergedlist:",sres)    
            res = sres
        return res[0] if len(res) >= 1 else None



    def mergeList(self, l1: ListNode, l2:ListNode):
        dummy = ListNode(0)
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next


