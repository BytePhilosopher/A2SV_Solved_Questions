# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        size=0
        if not head.next:
            return None


        while cur:
            size+=1
            cur=cur.next
        mid=size//2
        counter=0

        slow=head
        prev=None

        while slow:
            counter+=1
            if mid==counter:
                prev=slow
                slow=slow.next
                prev.next=slow.next
            
            slow=slow.next
        dummy=ListNode(0)
        dummy.next=head
        return dummy.next
    


        