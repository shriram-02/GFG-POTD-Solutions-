class Solution:
    def compute(self, head):
        # Reverse linked list
        def reverse(head):
            prev = None
            curr = head
            
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            return prev
        
        if not head or not head.next:
            return head
        
        # Step 1: Reverse the list
        head = reverse(head)
        
        # Step 2: Remove nodes smaller than max seen so far
        max_so_far = head.data
        curr = head
        
        while curr and curr.next:
            if curr.next.data < max_so_far:
                curr.next = curr.next.next
            else:
                curr = curr.next
                max_so_far = curr.data
        
        # Step 3: Reverse back
        return reverse(head)