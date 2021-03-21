def dfs(start, end):
    stack = [start]
    visited[start] = 1
    # Stack 즉 안 가본곳이 남아 있으면 갈때까지 while문 수행
    while stack:
        # 현재 위치
        current = stack.pop()
        print(current)
        for i in range(v):
            if visited[i] == 0 and graph[current][i] == 1:
                stack.append(i)
                visited[i] = 1
        # 내림차순 꼴로 진행하고 싶으므로 reverse 처리
        stack.reverse()
    return visited


# 점 6개 간선 5개의 Graph 를 그려보자
v, m = map(int, input().split())
graph = [[0]*v for _ in range(v)]
for _ in range(m):
    # 입력받고 index 맞춰주기
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    # 인접행렬 Graph
    graph[x][y] = 1
    graph[y][x] = 1
# 재귀함수(DFS) 방식은 방문기록 visited 를 함수 외부에 배치해야 초기화가 안됨
visited = [0] * v
# 출발, 도착 지점 설정
start, end = map(int, input().split())
start -= 1
end -= 1
print(dfs(start, end))

# TEST CASE
# 6 5
# 1 2
# 2 3
# 3 4
# 3 5
# 1 6
# 1 6