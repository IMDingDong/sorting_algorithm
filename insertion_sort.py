def insertion_sort(arr):
    i = 1
    for i in range(i, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key


numbers = [2, 3, 1, 4]
insertion_sort(numbers)
print(numbers)
