# 문제
# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.
#
# 출력
# 첫째 줄에 연결 요소의 개수를 출력한다.

import sys
sys.setrecursionlimit(10**6)

def dfs(u):
    for h in first[u]:
        if visited[h] == False:
            visited[h] = True
            dfs(h)

N, M = map(int, sys.stdin.readline().split())

first = [[] for _ in range(N+1)]
visited = [False] * (N+1)
cnt = 0
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    first[a].append(b)
    first[b].append(a)

for j in range(1, N+1):
    if visited[j] == False:
        visited[j] = True
        dfs(j)
        cnt += 1

print(cnt)