# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummynode=ListNode(0)
        current=dummynode
        carry=0
        sumi=0
        while (l1!=None or l2!=None):
            sumi=0
            if l1:
                sumi+=l1.val
            if l2:
                sumi+=l2.val
            sumi+=carry
            current.next = ListNode(sumi%10)
            current=current.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
            carry=sumi//10
        if carry>0:
            current.next=ListNode(carry)
            current=current.next
        return dummynode.next
                
            
