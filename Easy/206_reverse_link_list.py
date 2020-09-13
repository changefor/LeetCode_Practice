# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        now = head
        next = head.next

        while next is not None:
            next = now.next
            now.next = pre
            pre = now
            now = next
        return pre

a1 = ListNode(1)
tmp = a1
tmp.next = ListNode(2)
tmp = tmp.next
tmp.next = ListNode(3)
tmp = tmp.next
tmp.next = ListNode(4)
tmp = tmp.next
tmp.next = ListNode(5)

s = Solution()

a1 = s.reverseList(a1)

while a1 is not None:
    print(a1.val)
    a1 = a1.next
