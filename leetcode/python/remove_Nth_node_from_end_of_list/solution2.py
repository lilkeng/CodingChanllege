# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        n = len(lists)
        if n == 1:
            return lists[0]
        mid = n/2
        listNode1 = self.mergeKLists(lists[:mid])
        listNode2 = self.mergeKLists(lists[mid:])
        return self.merge(listNode1, listNode2)
        
    def merge(self, l1, l2):
        dummy = ListNode(0)
        head = dummy
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                head.next = l1
                l1 = l1.next
                head = head.next
            else:
                head.next = l2
                l2 = l2.next
                head = head.next
        if l1 != None:
            head.next = l1
        if l2 != None:
            head.next = l2
        return dummy.next
            