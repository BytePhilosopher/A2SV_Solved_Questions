class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
      
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
     
        cur = prev
        maxval = cur.val
        dummy = ListNode(0)  
        dummy.next = cur
        p = cur  
        
        cur = cur.next
        while cur:
            if cur.val < maxval:
             
                p.next = cur.next
            else:
               
                maxval = cur.val
                p = cur
            cur = cur.next
        
       
        new_head = dummy.next
        prev = None
        current = new_head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        return prev  