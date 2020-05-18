from ListNode import ListNode

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # Returns Given head if Given head have <2 Values
        if head == None or head.next == None:
            return head
        
        # Initialising Odd and Even heads
        odd_head = odd = ListNode(0)
        even_head = even = ListNode(0)
        
        # Counter to Track Odd/Even
        counter = 1
        
        # Iterates over Given head
        while head:
            # Put Node in Even head
            if counter % 2 == 0:
                even.next = head
                even = even.next
            # Put Node in Odd head
            else:
                odd.next = head
                odd = odd.next
            # Update Values for Next Loop
            counter += 1
            head = head.next
        
        # Prevent Cycle Error
        even.next = None
        
        # Combining Odd and Even heads
        odd.next = even_head.next
         
        # Return Odd Even Linked List
        return odd_head.next
