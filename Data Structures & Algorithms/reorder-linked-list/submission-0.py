# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #get the second part of the linkedlist
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        #store the second half of the linkedlist 
        second = slow.next
        slow.next = None # setting the first part to None

        #reverse the second part of the linkedlist
        prev=None
        while second:
            next = second.next
            second.next = prev
            prev = second
            second = next

        # merge the list
        firsthalf, secondhalf = head, prev

        while secondhalf:
            firsttemp,secondtemp = firsthalf.next, secondhalf.next

            firsthalf.next = secondhalf
            secondhalf.next = firsttemp
            firsthalf,secondhalf = firsttemp, secondtemp
        



        

        