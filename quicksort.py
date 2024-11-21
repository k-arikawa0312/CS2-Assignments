def simple_qsort(lst):
    if len(lst) <=1:
        return lst
    pivot = lst[0]

    lst1 = [x for x in lst[1:] if x < pivot]
    lst2 = [x for x in lst[1:] if x == pivot]
    lst3 = [x for x in lst[1:] if x > pivot]

    return simple_qsort(lst1) + lst2 + simple_qsort(lst3)
