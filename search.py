def linear_search(arr, target):
    for i in arr:
        if i == target:
            return True
    return False

def binary_search_with_trace(arr, target):
    left = 0
    right = len(arr) - 1
    comparisons = []
    count = 0
    
    while left <= right:
        # 偶数長の場合は後半の先頭を中心とする
        if (right - left + 1) % 2 == 0:
            mid = (left + right) // 2 + 1
        else:
            mid = (left + right) // 2
            
        count += 1
        comparisons.append(arr[mid])
        
        if arr[mid] == target:
            return comparisons, count
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return comparisons, count

# 使用例
arr = [2, 5, 12, 24, 31, 38, 43, 48, 57, 69, 88, 93, 99]
target = 31
comparisons, count = binary_search_with_trace(arr, target)
print(f"比較した数字: {comparisons}")
print(f"比較回数: {count}")