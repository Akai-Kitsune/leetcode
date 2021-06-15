# addTwoNumber
# Result ~73%

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def print(self):
    	while(self != None):
    		print(self.val)
    		self = self.next

class Solution(object):
	
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        result = ListNode()
        tmp = result
        current = 0
        while(l1 != None or l2 != None or carry):
        	current = carry + (l1.val if l1 != None else 0) + (l2.val if l2 != None else 0)
        	carry = 1 if current > 9 else 0
        	if carry == 1:
        		current -= 10
        	if l1 != None:
        		l1 = l1.next
        	if l2 != None:
        		l2 = l2.next
        	tmp.next = ListNode(current)
        	tmp = tmp.next
        return result.next