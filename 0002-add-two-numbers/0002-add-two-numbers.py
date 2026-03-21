2# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        res=dummy
        curr=l1
        cur=l2
        rem=0

        while cur and curr:
            value=cur.val+curr.val+rem
            if rem:  
                rem=0

            if value>=10:
                v=value%10
                rem=1
                res.next=ListNode(v)
            else:
                res.next=ListNode(value)
            cur=cur.next
            curr=curr.next
            res=res.next

        while curr:
            value=curr.val+rem
            if rem:  
                rem=0

            if value>=10:
                v=value%10
                rem=1
                res.next=ListNode(v)
            else:
                res.next=ListNode(value)
            curr=curr.next
            res=res.next

        while cur:
            value=cur.val+rem
            if rem:  
                rem=0

            if value>=10:
                v=value%10
                rem=1
                res.next=ListNode(v)
            else:
                res.next=ListNode(value)
            cur=cur.next
            res=res.next
        if rem:
            res.next=ListNode(1)

        return dummy.next