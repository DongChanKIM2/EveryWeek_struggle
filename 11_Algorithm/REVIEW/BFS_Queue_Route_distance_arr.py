def search():
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                return i, j


def bfs(x, y):
    global count
    queue = []
    queue.append((x, y))
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue:
        count += 1
        current_x, current_y = queue.pop(0)
        for direction in range(4):
            nx = current_x + dx[direction]
            ny = current_y + dy[direction]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if arr[nx][ny] == 3:
                return distance[current_x][current_y]
            if arr[nx][ny] == 1:
                distance[nx][ny] = distance[current_x][current_y] + 1
                arr[nx][ny] = 2
                queue.append((nx, ny))
    return arr


n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
distance = [[0] * n for _ in range(n)]
# count = 0
x, y = search()
print(bfs(x, y))
print(distance)