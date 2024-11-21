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
def simple_qsort(lst, split_count=0):
    if len(lst) <= 1:
        return lst, split_count
    
    # ピボットの選択
    if len(lst) % 2 == 1:
        pivot_index = len(lst) // 2
    else:
        pivot_index = len(lst) // 2
    pivot = lst[pivot_index]

    # リストを分割
    lst1 = [x for i, x in enumerate(lst) if x < pivot and i != pivot_index]
    lst2 = [x for i, x in enumerate(lst) if x == pivot]
    lst3 = [x for i, x in enumerate(lst) if x > pivot and i != pivot_index]

    # 分割の詳細を出力
    if len(lst) > 1:
        print(f"分割直後のリスト: {lst1 + lst2 + lst3}")
        print(f"左側のリスト: {lst1}")
        print(f"ピボットのリスト: {lst2}")
        print(f"右側のリスト: {lst3}")
        print(f"使用したピボット: {pivot}")
        print("---")  # 見やすさのための区切り線

    # 再帰的にソート
    sorted_lst1, count1 = simple_qsort(lst1, split_count)
    sorted_lst3, count2 = simple_qsort(lst3, count1)
    
    return sorted_lst1 + lst2 + sorted_lst3, count2 + 1

# メイン処理
def run_quicksort(lst):
    print(f"入力リスト: {lst}")
    print("---")
    sorted_lst, split_count = simple_qsort(lst)
    print(f"分割回数: {split_count}")
    print(f"ソート後のリスト: {sorted_lst}")
    return sorted_lst

run_quicksort([3, 8, 2, 9, 1, 7, 4, 6, 5])