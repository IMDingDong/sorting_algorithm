def shell_sort(arr):
    size = len(arr)
    gap = size // 2
    while gap > 0:
        for i in range(gap, size):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap //= 2


numbers = [2, 3, 1, 4]
shell_sort(numbers)
print(numbers)
