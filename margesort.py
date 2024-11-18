def mergesort(lst):
    if len(lst) <= 1:
        return lst
    lst1 = lst[0:len(lst) // 2]
    lst2 = lst[len(lst) // 2:]
    left = mergesort(lst1)
    right = mergesort(lst2)
    return merge(left, right)

def merge(lst1, lst2):
    result = []
    i = 0
    j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            result.append(lst1[i])
            i += 1
        else:
            result.append(lst2[j])
            j += 1
    while i < len(lst1):
        result.append(lst1[i])
        i += 1
    while j < len(lst2):
        result.append(lst2[j])
        j += 1
    return result
