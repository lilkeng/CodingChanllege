# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0); p = dummy
        carry = 0
        
        while l1 and l2:
            p.next = ListNode((l1.val + l2.val + carry) % 10)
            carry = (l1.val + l2.val + carry) / 10
            p = p.next; l1 = l1.next; l2 = l2.next
        
      
        while l2:
            p.next = ListNode((l2.val + carry) % 10)
            carry = (l2.val + carry) / 10
            p = p.next; l2 = l2.next
        
        
        while l1:
            p.next = ListNode((l1.val + carry) % 10)
            carry = (l1.val + carry) / 10
            p = p.next; l1 = l1.next
                
        if carry == 1:
            p.next = ListNode(1)
                
        return dummy.next
                
                
                
                
                