def quicksort(arr):
    if len(arr) <= 1:
        return arr
    minimum_arr, middle, maximum_arr = [], [], []
    pivot = arr[len(arr) // 2]
    for num in arr:
        if num < pivot:
            minimum_arr.append(num)
        elif num > pivot:
            maximum_arr.append(num)
        else:
            middle.append(num)
    return quicksort(minimum_arr) + middle + quicksort(maximum_arr)


t = int(input())
for tc in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr = quicksort(arr)
    print('#{}'.format(tc+1), end=' ')
    for i in range(5):
        print(arr[n-i-1], end=' ')
        print(arr[i], end=' ')
    print()



    # print('#{} {}'.format(tc+1, count))

    # print('#{} {}'.format(tc+1, maximum-minimum))

