def search():
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                return i, j


def bfs(x, y):
    queue = [(x, y)]
    while queue:
        print(queue)
        current_x, current_y = queue.pop(0)
        print(current_x, current_y)
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for i in range(4):
            nx = current_x + dx[i]
            ny = current_y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if arr[nx][ny] == 3:
                return 1111111111111
            if arr[nx][ny] == 1:
                queue.append((nx, ny))
                arr[nx][ny] = 2


n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
x, y = search()
print(bfs(x, y))
print(arr)

