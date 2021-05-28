# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        hh = head
        value = ""
        while hh != None:
            value += str(hh.val)
            hh = hh.next
        return int(value, 2)