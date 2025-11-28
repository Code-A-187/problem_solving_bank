from typing import List


def asteroid_collision(asteroids: List[int]) -> List[int]:
    astro_state = []

    for asteroid in asteroids:
        if asteroid > 0:
            astro_state.append(asteroid)
        else:
            while astro_state and astro_state[-1] > 0:
                    if abs(asteroid) > astro_state[-1]:
                        astro_state.pop()
                    elif abs(asteroid) < astro_state[-1]:
                        break
                    else:
                        astro_state.pop()
                        break
            else:
                astro_state.append(asteroid)
    
    return astro_state

print(asteroid_collision([5,10,-5]))
print(asteroid_collision([8,-8]))
print(asteroid_collision([10,2,-5]))
print(asteroid_collision([3,5,-6,2,-1,4]))