from typing import List

def total_fruit(fruits: List[int]) -> int:

    # with for and enumerate

    l = 0
    hmap = {}

    for r, fruit in enumerate(fruits):
        if fruit not in hmap:
            hmap[fruit] = 1
        else:
            hmap[fruit] += 1

        if len(hmap) > 2:
            hmap[fruits[l]] -= 1
            if hmap[fruits[l]] == 0:
                hmap.pop(fruits[l])
            
            l += 1
    
    return r-l+1


print(total_fruit([1,2,1]))
print(total_fruit([0,1,2,2]))
print(total_fruit([1,2,3,2,2]))

