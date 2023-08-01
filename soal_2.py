def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    found_indices = []

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            found_indices.append(mid)
            # Pencarian di sebelah kiri
            left_idx = mid - 1
            while left_idx >= 0 and arr[left_idx] == target:
                found_indices.append(left_idx)
                left_idx -= 1
            # Pencarian di sebelah kanan
            right_idx = mid + 1
            while right_idx < len(arr) and arr[right_idx] == target:
                found_indices.append(right_idx)
                right_idx += 1
            return found_indices
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None

# Data array
data = [19, 40, 10, 90, 2, 50, 60, 50, 1]

# Test Case
test_cases = [1, 50, 100]

for target in test_cases:
    result = binary_search(data, target)
    if result:
        print(f"Input: {target}\nOutput: Angka {target} ada di indeks ke {', '.join(map(str, result))}")
    else:
        print(f"Input: {target}\nOutput: Angka {target} tidak ada dalam array")
