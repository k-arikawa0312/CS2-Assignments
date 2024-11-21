def merge_sort(arr):
    def find_sublists(original_lists, target):
        return [i for i, sublist in enumerate(original_lists) if sublist == target]

    def update_lists(current_lists):
        result = []
        for lst in current_lists:
            if lst not in result:
                result.append(lst)
        return result

    def split_and_merge(arr, all_lists):
        if len(arr) <= 1:
            return arr, all_lists

        mid = (len(arr)+1) // 2
        left = arr[:mid]
        right = arr[mid:]

        indices = find_sublists(all_lists, arr)
        if indices:
            new_lists = all_lists.copy()
            for idx in indices:
                new_lists[idx:idx+1] = [left, right]
            all_lists = update_lists(new_lists)

        left, all_lists = split_and_merge(left, all_lists)
        right, all_lists = split_and_merge(right, all_lists)

        merged = []
        i = j = 0
        swap_occurred = False
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                swap_occurred = True

        merged.extend(left[i:])
        merged.extend(right[j:])

        new_lists = all_lists.copy()
        left_indices = find_sublists(new_lists, left)
        right_indices = find_sublists(new_lists, right)
        if left_indices and right_indices:
            min_idx = min(left_indices + right_indices)
            max_idx = max(left_indices + right_indices)
            new_lists[min_idx:max_idx+1] = [merged]
            all_lists = update_lists(new_lists)
            if swap_occurred:
                print(" ".join(f"({', '.join(map(str, lst))})" for lst in all_lists))

        return merged, all_lists

    print(f"({', '.join(map(str, arr))})")
    result, _ = split_and_merge(arr, [arr])
    return result

# テスト実行
arr = [10,2,5,8,1,4,3,7,9,6]
print("マージソートの実行過程:")
result = merge_sort(arr)