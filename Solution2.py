# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = None
        temp = result
        hasPre = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + hasPre
            hasPre = total // 10
            total = total % 10

            if not result:
                result = ListNode(total)
                temp = result
            else:
                temp.next = ListNode(total)
                temp = temp.next

            l1 = None if l1 is None else l1.next
            l2 = None if l2 is None else l2.next

        if hasPre == 1:
            result.next = ListNode(1)

        return result


if __name__ == '__main__':
    a = ListNode(5)
    # a.next = ListNode(4)
    # a.next.next = ListNode(3)

    b = ListNode(5)
    # b.next = ListNode(6)
    # b.next.next = ListNode(4)

    c = Solution().addTwoNumbers(a, b)
    print(c)
