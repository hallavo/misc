
# A friendly note from the author:
#
# I wrote this implementation of merge sort as an
# exercise. Please use a library function for your
# real-world sorting needs.

def merge(left, right):
    leftlen = len(left)
    rightlen = len(right)
    iLeft = 0
    iRight = 0
    result = [0 for i in range(0,leftlen+rightlen)]
    # This part is ugly... What would a functional merge look like?
    # Pattern-matching and recursion?
    # TO DO: Make it pretty
    for i in range(0,leftlen+rightlen):
        if iLeft < leftlen and iRight >= rightlen:
            result[i] = left[iLeft]
            iLeft += 1
        elif iRight < rightlen and iLeft >= leftlen:
            result[i] = right[iRight]
            iRight += 1
        elif iLeft < leftlen and left[iLeft] < right[iRight]:
                result[i] = left[iLeft]
                iLeft += 1
        elif iRight < rightlen:
            result[i] = right[iRight]
            iRight += 1
    return result


def split(start,end):
    if start == end:
        return start
    else:
        mid = end / 2
        return (start,mid), (mid,end)
    

def mergesort(arr):
    l = len(arr)
    if l == 1:
        return arr
    left, right = split(0,l)
    lsorted = mergesort(arr[ left[0]  :  left[1] ])
    rsorted = mergesort(arr[ right[0] : right[1] ])
    return merge(lsorted,rsorted)



arr = (6,5,3,1,2,7,9,3,7,44,8,98,2,7,9,3,7,44,8,98,2,7,9,3,7,44,8,98,2,7,9,3,7,44,8,98,2,7,9,3,7,44,8,98,2,7,9,3,7,44,8,98,8,7,2,4)

print(mergesort(arr))
