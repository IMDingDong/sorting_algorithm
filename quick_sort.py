def quick_sort(arr):
    if len(arr) > 1:
        pivot = arr[len(arr)-1]
        left, mid, right = [], [], []
        for i in range(len(arr)-1):
            if arr[i] < pivot:
                left.append(arr[i])
            elif arr[i] > pivot:
                right.append(arr[i])
            else:
                mid.append(arr[i])
        mid.append(pivot)
        return quick_sort(left) + mid + quick_sort(right)
    else:
        return arr


numbers = [2, 3, 1, 4]
sorted_numbers = quick_sort(numbers)
print(sorted_numbers)
