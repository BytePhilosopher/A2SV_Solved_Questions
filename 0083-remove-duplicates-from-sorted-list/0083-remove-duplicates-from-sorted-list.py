# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        cur=head
        hash=set()
        hash.add(cur.val)

        while cur and cur.next:
            if cur.next.val in hash:
                cur.next=cur.next.next
            else:
                hash.add(cur.next.val)
                cur=cur.next

        return head
