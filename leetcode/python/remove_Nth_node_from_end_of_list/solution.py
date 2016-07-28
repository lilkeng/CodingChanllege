# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        slow=fast=dummy
        
        for i in range(n):
            fast = fast.next
        # While fast.next is none, slow.next is the node should be deleted
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        #Don't forget return dummy.next!
        return dummy.next