def bfs(start, end):
    # visited = []
    visited = [0] * (v+1)
    queue = [start]
    while queue:
        current = queue.pop(0)
        # if current not in visited:
        #     queue += not_arr[current]
        #     visited.append(current)
        if visited[current] == 0:
            queue += not_arr[current]
            visited[current] = 1
    return visited


v, e = map(int, input().split())
not_arr = {i+1: [] for i in range(v)}
for _ in range(e):
    n, m = map(int, input().split())
    not_arr[n].append(m)
    not_arr[m].append(n)
start, end = map(int, input().split())
print(bfs(start, end))
