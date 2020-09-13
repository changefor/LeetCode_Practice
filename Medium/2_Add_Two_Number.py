# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(1)
        nowNode = result
        global overflow, sum, temp
        overflow = 0
        while l1 is not None or l2 is not None :
            if l1 is None:
                sum = l2.val + overflow
                l2 = l2.next
            elif l2 is None:
                sum = l1.val + overflow
                l1 = l1.next
            else:
                sum = l1.val + l2.val + overflow
                l1 = l1.next
                l2 = l2.next

            temp = ListNode(sum % 10)
            nowNode.next = temp
            nowNode = nowNode.next
            if sum // 10 != 0:
                overflow = 1
            else:
                overflow = 0

        if overflow != 0:
            temp = ListNode(overflow)
            nowNode.next = temp
        return result.next



list1 = ListNode(1)
temp = ListNode(8)
list1.next = temp
#temp = ListNode(3)
#list1.next.next = temp

list2 = ListNode(0)
#temp = ListNode(6)
#list2.next = temp
#temp = ListNode(4)
#list2.next.next = temp

s = Solution()
temp = s.add_two_numbers(list1, list2)
while temp is not None:
    print(temp.val)
    temp = temp.next
