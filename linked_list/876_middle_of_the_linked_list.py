from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middle_node(head: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
    # def count_nodes(head):
    #     # Base Case
    #     if head is None:
    #         return 0
    #     # Count this node plus the rest of the list
    #     return 1 + count_nodes(head.next)
    
    # middle = count_nodes(head) // 2
    # for _ in range(middle):
    #     head = head.next

    # return head

    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow


print(middle_node(head = [1,2,3,4,5]))
print(middle_node(head = [1,2,3,4,5,6]))