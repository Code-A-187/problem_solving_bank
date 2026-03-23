from typing import Optional

class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# recursive way to reverse k group in linked list
def reverse_k_group(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head:
        return None
    
    tail = head
    # we get the needed k elements
    for _ in range(k):
        if not tail:
            return head
        tail = tail.next

    # reverse the k elements
    def reverse(cur, end):
        prev=None

        while cur != end:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        return prev
    
    # using reverse function to reverse k elements
    new_head = reverse(head, tail)
    
    # recursivly using the function to attach the reversed elements to head

    head.next = self.reverse_k_group(tail, k)

    return new_head



if __name__ == "__main__":
    arr = []

    node1 =ListNode(1)
    node1.next =ListNode(2)
    node1.next.next = ListNode(3)
    node1.next.next.next = ListNode(4)
    node1.next.next.next.next = ListNode(5)
    arr.append(node1)

    head = reverse_k_group(arr, 2)

    print(head)