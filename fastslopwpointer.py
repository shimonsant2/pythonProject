class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                current = head
                while current is not slow:
                    current = current.next
                    slow = slow.next
                return slow
        return None
