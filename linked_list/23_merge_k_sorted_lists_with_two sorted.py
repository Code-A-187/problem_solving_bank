from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two(head1, head2):
    dummy = ListNode()
    curr = dummy

    while head1 and head2:
        if head1.val > head2.val:
            curr.next = head2.val
            head2 = head2.next
        else:
            curr.next = head1.val
            head1 = head1.next
        
        curr = curr.next
    if head1:
        curr.next = head1
    if head2:
        curr.next = head2

    return dummy.next      

def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    res = None

    for list in lists:
        res = merge_two(res, list)
    
    return res

def printList(node):
    while node is not None:
        print(f"{node.data}", end="")
        if node.next is not None:
            print(" -> ", end="")
        node = node.next
    print()

if __name__ == "__main__":
    arr = []

    node1 =ListNode(1)
    node1.next = ListNode(3)
    node1.next.next = ListNode(5)
    node1.next.next.next = ListNode(7)
    arr.append(node1)

    node2 = ListNode(2)
    node2.next = ListNode(4)
    node2.next.next = ListNode(6)
    node2.next.next.next = ListNode(8)
    arr.append(node2)

    node3 = ListNode(0)
    node3.next = ListNode(9)
    node3.next.next = ListNode(10)
    node3.next.next.next = ListNode(11)
    arr.append(node3)

    head = merge_k_lists(arr)
    printList(head)