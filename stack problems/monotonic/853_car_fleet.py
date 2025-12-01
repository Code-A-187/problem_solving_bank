from typing import List


def car_fleet(target: int, position: List[int], speed: List[int]) -> int:

    times = [(target - pos)/speed for pos, speed in sorted(zip(position, speed), reverse=True)]

    stack = []

    for current_time in times:
        if not stack or current_time > stack[-1]:
            stack.append(current_time)
        
    return len(stack)

print(car_fleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]))
print(car_fleet(target = 10, position = [3], speed = [3]))
print(car_fleet(target = 100, position = [0,2,4], speed = [4,2,1]))