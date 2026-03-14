import heapq
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    # use heap for searching always the min in the lists
    res = []
    for i in range(0, len(lists)):
        head = lists[i]
        if head:
            heapq.heappush(res, (head.val, i, head))

    dummy = ListNode()
    tail = dummy

    while res:
        _, index, top = heapq.heappop(res)
        tail.next = top
        tail =top
    
        if top.next:
            heapq.heappush(res, (top.next.val, index, top.next))

    return dummy.next


if __name__ == "__main__":

    # create a hard-coded linked list:
    # 10 -> 20 -> 30 -> 40
    head = ListNode(1)
    head.next = ListNode(4)
    head.next.next = ListNode(5)


print(merge_k_lists(lists = [[1,4,5],[1,3,4],[2,6]]))
print(merge_k_lists(lists = []))
print(merge_k_lists(lists = [[]]))

