def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    left = merge_sort(arr[:len(arr)//2])
    right = merge_sort(arr[len(arr)//2:])

    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    if i == len(left):
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    elif j == len(right):
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
    return arr


numbers = [2, 3, 1, 4]
sorted_numbers = merge_sort(numbers)
print(sorted_numbers)
