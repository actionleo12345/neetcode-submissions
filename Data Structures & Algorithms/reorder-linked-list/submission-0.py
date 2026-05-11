# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next or not head.next.next:
            return

        # split
        mid, end = head, head
        while end.next and end.next.next:
            mid = mid.next
            end = end.next.next

        
        # reverse part02
        p2_head = mid.next # must be next
        mid.next = None
        ## start verse part02
        pre = None
        while p2_head:
            tem = p2_head.next
            p2_head.next = pre
            pre = p2_head
            p2_head = tem
        
        # merge part01 and part02
        p2 = pre
        p1 = head
        while p2:
            tem_p1 = p1.next
            tem_p2 = p2.next
            p1.next = p2
            p2.next = tem_p1
            p2 = tem_p2
            p1 = tem_p1


