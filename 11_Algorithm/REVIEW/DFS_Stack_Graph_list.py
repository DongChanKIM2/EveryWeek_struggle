def dfs(start, end):
    visited = []
    stack = [start]
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.append(current)
            # 딕셔너리 내부의 리스트 '값'들을 더해줘야 하므로 리스트 append가 아니라 +로 해야함(제일 중요)
            stack += reversed(not_arr[current])
    return visited


v, e = map(int, input().split())
not_arr = {i+1: [] for i in range(v)}
for _ in range(e):
    x, y = map(int, input().split())
    not_arr[x].append(y)
    not_arr[y].append(x)
start, end = map(int, input().split())
print(dfs(start, end))

# TEST CASE
# 6 5
# 1 2
# 2 3
# 3 4
# 3 5
# 1 6
# 1 6