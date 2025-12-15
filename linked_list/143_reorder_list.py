from typing import Optional

class ListNode:
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next

def reorder_list(head: Optional[ListNode]):
    fast = head
    slow = head
    
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    second = slow.next
    node = slow.next = None

    while second:
        temp = second.next
        second.next = node
        node = second
        second = temp
    
    first = head
    second = node

    while second:
        temp1  = first.next
        temp2 = second.next
        first.next = second
        second.next = temp1
        first,second = temp1, temp2
    
        


        


node5= ListNode(5)
node4 = ListNode(4, next = node5)
node3 = ListNode(3, next = node4)
node2 = ListNode(2, next = node3)
node1 = ListNode(1, next = node2)
head = node1

new_head = reorder_list(head)

print("List after reorder:")
current = new_head
output = []
while current:
    output.append(current.val)
    current = current.next

print(output)