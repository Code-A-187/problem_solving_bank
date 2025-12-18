from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.x = int(x)
        self.next = next
        self.random = random
    

def copy_random_list(head: Optional[Node]) -> Optional[Node]:
    hash = {None:None}
    cur = head

    while cur:
        hash[cur] = Node(cur.val)
        cur = cur.next
    
    cur = head

    while cur:
        copy = hash[cur]
        copy.next = hash[cur.next]
        copy.random = hash(cur.random)
        cur = cur.next
    
    return hash[head]


    




node3 = Node(4)
node2 = Node(6, next=node3)
node1 = Node(5, next=node2)
head = node1

new_head = copy_random_list(head)

# print the Result Manually
print(f"List after add l1 l2:")
current = new_head
output = []
while current:
    output.append(current.val)
    current = current.next

print(output)