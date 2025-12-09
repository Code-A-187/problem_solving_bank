# The isBadVersion API is already defined.
# def isBadVersion(version: int) -> bool:


def fisrt_bad_version(n: int) -> int:
    start, end = 1, n

    while start < end:
        mid = (end  + start)//2

        if isBadVersion(mid):
            end = mid
            
        else:
            start = mid + 1
        
        return start
    return start

