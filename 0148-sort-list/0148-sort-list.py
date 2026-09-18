# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if head == None or head.next == None:
            return head
        
        lst = []
        temp = head

        while temp != None:
            lst.append(temp.val)
            temp = temp.next
        
        lst.sort()
        ans = head
        count = 0

        while ans != None:
            ans.val = lst[count]
            ans = ans.next
            count += 1
        
        return head
        