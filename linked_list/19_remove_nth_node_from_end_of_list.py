from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
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
        

node5 = ListNode(5)
node4 = ListNode(4, next=node5) # 4 -> 5
node3 = ListNode(3, next=node4) # 3 -> 4 -> 5
node2 = ListNode(2, next=node3) # 2 -> 3 -> 4 -> 5
node1 = ListNode(1, next=node2) # 1 -> 2 -> 3 -> 4 -> 5
head = node1 # entry point to the list

n = 2

# call the function
new_head = remove_nth_from_end(head, n)

# print the Result Manually
print(f"List after removing the {n}nd node from the end:")
current = new_head
output = []
while current:
    output.append(current.val)
    current = current.next

print(output)
