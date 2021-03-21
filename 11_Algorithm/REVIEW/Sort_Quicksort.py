def quicksort(arr):
    if len(arr) <= 1:
        return arr
    minimum_arr, equal, maximum_arr = [], [], []
    pivot = arr[len(arr) // 2]
    for num in arr:
        if num < pivot:
            minimum_arr.append(num)
        elif num > pivot:
            maximum_arr.append(num)
        else:
            equal.append(num)
    # return quicksort(maximum_arr) + equal + quicksort(minimum_arr)
    return quicksort(minimum_arr) + equal + quicksort(maximum_arr)


t = int(input())
for tc in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print('#{} {}'.format(tc+1, quicksort(arr)[-1] - quicksort(arr)[0]))
