def bfs(start, end):
    queue = [start]
    visited[start] = 1
    while queue:
        current = queue.pop(0)
        print(current)
        for i in range(v):
            if visited[i] == 0 and graph[current][i] == 1:
                queue.append(i)
                visited[i] = 1
    return visited


v, e = map(int, input().split())
graph = [[0]*v for _ in range(v)]
visited = [0] * v
for _ in range(e):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    graph[x][y] = 1
    graph[y][x] = 1
start, end = map(int, input().split())
start -= 1
end -= 1
print(bfs(start, end))

# TEST CASE
# 6 5
# 1 2
# 2 3
# 3 4
# 3 5
# 1 6
# 1 6