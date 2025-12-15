from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        m = 0

def remove_nth_node_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode()
    slow = dummy
    fast = head

    while n > 0 and fast:
        fast = fast.next
        n -= 1
    
    while fast:
        slow = slow.next
        fast = fast.next
    
    slow.next = slow.next.next

    return dummy.next
        


