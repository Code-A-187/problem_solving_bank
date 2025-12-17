from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    res = dummy

    total = carry = 0

    while l1 or l2 or carry:
        total = carry
        if l1:
            total += l1.val
            l1 = l1.next
        if l2:
            total += l2.val
            l2 = l2.next
        num = total % 10
        carry = total // 10
        dummy.next = ListNode(num)
        dummy = dummy.next

    return res.next

        




node3 = ListNode(3)
node2 = ListNode(4, next=node3)
node1 = ListNode(2, next=node2)
l1 = node1


node3 = ListNode(4)
node2 = ListNode(6, next=node3)
node1 = ListNode(5, next=node2)
l2 = node1

new_head = add_two_numbers(l1, l2)

# print the Result Manually
print(f"List after add l1 l2:")
current = new_head
output = []
while current:
    output.append(current.val)
    current = current.next

print(output)