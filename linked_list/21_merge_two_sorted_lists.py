from typing import Optional

class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    curr = dummy
    
    while list1 and list2:
        if list1.val > list2.val:
            curr.next = list2.val
            list2 = list2.next
        else:
            curr.next = list1.val
            list1 = list1.next
        
        curr = curr.next
    
    if list1:
        curr.next = list1
    if list2:
        curr.next = list2
    
    return dummy
    

if __name__ == "__main__":

    # create a hard-coded linked list:
    # 10 -> 20 -> 30 -> 40
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(4)


print(merge_two_lists(list1 = [1,2,4], list2 = [1,3,4]))
print(merge_two_lists(list1 = [], list2 = [0]))