#pivotをリストの先頭としたときのクイックソートの実装
# def simple_qsort(lst):
#     if len(lst) <=1:
#         return lst
#     pivot = lst[0]

#     lst1 = [x for x in lst[1:] if x < pivot]
#     lst2 = [x for x in lst[1:] if x == pivot]
#     lst3 = [x for x in lst[1:] if x > pivot]

#     return simple_qsort(lst1) + lst2 + simple_qsort(lst3)

#リストの長さが奇数の場合は中心にある数値を、偶数の場合はリスト後半の先頭の数値をピボットとして用いる(問題集のやり方)
def simple_qsort(lst):
    if len(lst) <= 1:
        return lst
    
    # ピボットの選択を修正
    if len(lst) % 2 == 1:
        # 奇数の場合は中心の要素
        pivot_index = len(lst) // 2
    else:
        # 偶数の場合は後半の先頭要素
        pivot_index = len(lst) // 2
    pivot = lst[pivot_index]

    # ピボットを除外してリストを分割
    lst1 = [x for i, x in enumerate(lst) if x < pivot and i != pivot_index]
    lst2 = [x for i, x in enumerate(lst) if x == pivot]
    lst3 = [x for i, x in enumerate(lst) if x > pivot and i != pivot_index]

    return simple_qsort(lst1) + lst2 + simple_qsort(lst3)