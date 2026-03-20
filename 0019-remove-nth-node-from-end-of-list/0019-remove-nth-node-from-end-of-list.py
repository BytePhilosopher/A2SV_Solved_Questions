# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # size=0
        # prev,cur=head,head
        # while cur:
        #     size+=1
        #     cur=cur.next

        # idx=size-n+1

        # if idx==1:
        #     return head.next

     
        # for _ in range(idx-2):
        #     prev=prev.next

        # if prev.next:
        #     prev.next=prev.next.next


        # return head

        dummy=ListNode(0)
        dummy.next=head
        first=dummy
        second=dummy
        
        for _ in range(n+1):
            first=first.next

        while first:
            first=first.next
            second=second.next

        second.next=second.next.next
        return dummy.next
        
            