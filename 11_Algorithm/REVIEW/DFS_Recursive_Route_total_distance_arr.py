def search():
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                dfs(i, j)


def dfs(x, y):
    global count
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if arr[x][y] == 1:
        arr[x][y] = 0
        count += 1
        distance_arr[x][y] = count
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
    print(arr)
    print(distance_arr)
    print(count)


n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
distance_arr = [[0]*n for _ in range(n)]
count = 0
search()


# tc
# 00000
# 00110
# 00000
# 01100
# 01110