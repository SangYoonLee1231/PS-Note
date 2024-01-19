from collections import deque

# 입력값 받기
n, m, v = tuple(map(int, input().split()))

connected_lst = [
    list(map(int, input().split()))
    for _ in range(m)
]

# 변수 추가 선언
graph_lst = [[] for _ in range(n + 1)]

visited = [False for _ in range(n + 1)]

for elem in connected_lst:
    start, end = elem
    graph_lst[start].append(end)
    graph_lst[end].append(start)

# 정렬
for elem in graph_lst:
    elem.sort()


# dfs
def dfs(curr_n):
    for elem in graph_lst[curr_n]:
        if not visited[elem]:
            print(elem, end=" ")
            visited[elem] = True
            dfs(elem)


# bfs
def bfs():
    while q:
        curr_n = q.popleft()
        for elem in graph_lst[curr_n]:
            if not visited[elem]:
                print(elem, end=" ")
                visited[elem] = True
                q.append(elem)


# dfs
print(v, end=" ")
visited[v] = True
dfs(v)

# before bfs
print()
visited = [False for _ in range(n + 1)]
q = deque()

# bfs
print(v, end=" ")
visited[v] = True
q.append(v)
bfs()
