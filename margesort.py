# def mergesort(lst):
#     if len(lst) <= 1:
#         return lst
#     lst1 = lst[0:len(lst) // 2]
#     lst2 = lst[len(lst) // 2:]
#     left = mergesort(lst1)
#     right = mergesort(lst2)
#     return merge(left, right)

# def merge(lst1, lst2):
#     result = []
#     i = 0
#     j = 0
#     while i < len(lst1) and j < len(lst2):
#         if lst1[i] < lst2[j]:
#             result.append(lst1[i])
#             i += 1
#         else:
#             result.append(lst2[j])
#             j += 1
#     while i < len(lst1):
#         result.append(lst1[i])
#         i += 1
#     while j < len(lst2):
#         result.append(lst2[j])
#         j += 1
#     return result
def merge_sort(arr):
    def find_sublists(original_lists, target):
        """与えられたリストを含む部分リストのインデックスを見つける"""
        return [i for i, sublist in enumerate(original_lists) if sublist == target]

    def update_lists(current_lists):
        """重複を除去して部分リストを更新"""
        result = []
        for lst in current_lists:
            if lst not in result:
                result.append(lst)
        return result

    def split_and_merge(arr, all_lists):
        if len(arr) <= 1:
            return arr, all_lists

        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # 現在の配列を分割して更新
        indices = find_sublists(all_lists, arr)
        if indices:
            new_lists = all_lists.copy()
            for idx in indices:
                new_lists[idx:idx+1] = [left, right]
            all_lists = update_lists(new_lists)
            print(" ".join(f"({', '.join(map(str, lst))})" for lst in all_lists))

        # 再帰的に分割とマージ
        left, all_lists = split_and_merge(left, all_lists)
        right, all_lists = split_and_merge(right, all_lists)

        # マージ
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])

        # マージ後のリストを更新
        new_lists = all_lists.copy()
        left_indices = find_sublists(new_lists, left)
        right_indices = find_sublists(new_lists, right)
        if left_indices and right_indices:
            # 左右のリストをマージ結果で置き換え
            min_idx = min(left_indices + right_indices)
            max_idx = max(left_indices + right_indices)
            new_lists[min_idx:max_idx+1] = [merged]
            all_lists = update_lists(new_lists)
            print(" ".join(f"({', '.join(map(str, lst))})" for lst in all_lists))

        return merged, all_lists

    # 初期状態を表示
    print(f"({', '.join(map(str, arr))})")
    
    # ソート実行
    result, _ = split_and_merge(arr, [arr])
    return result

# テスト実行
arr = [3, 8, 2, 1, 7, 4, 6, 5]
print("マージソートの実行過程:")
result = merge_sort(arr)