def search(arr):
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                return i, j


def dfs(x, y):
    global flag
    if x < 0 or y < 0 or x >= n or y >= n:
        return False
    if arr[x][y] == 3:
        flag = 1
    if arr[x][y] == 1 or arr[x][y] == 2:
        print(x, y)
        arr[x][y] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)


n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
flag = 0
x, y = search(arr)
print(dfs(x, y))
print(arr)
print(flag)


# 1. tc: 델타로만 해도 문제 없는 예시
# 100000
# 112111
# 001001
# 111001
# 010011
# 011113

# 2. tc: 델타로만 하면 문제 있는 예시
# 100000
# 112111
# 001001
# 111003
# 000000
# 000000
