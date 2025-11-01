from math import floor

# Binary search
def search(arr, target, start, end):
    if start > end:
        return False

    print(arr[slice(start, end + 1)])
    
    middle = floor((start + end) / 2)

    if arr[middle] == target:
        return True
    
    if arr[middle] > target:
        return search(arr, target, start, middle - 1)
    else:
        return search(arr, target, middle + 1, end)

arr  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
target = 2


maze = [
  [' ', '#', '#', '#', '#', '#', '#', '#', '#', ' '],
  [' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' '],
  ['#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#'],
  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' '],
  [' ', '#', ' ', '#', '#', ' ', '#', ' ', ' ', '#'],
  [' ', ' ', '#', ' ', '#', '#', ' ', ' ', '#', '#'],
  [' ', '#', '#', ' ', '#', ' ', ' ', '#', ' ', ' '],
  [' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' '],
  [' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', 'X'],
]


