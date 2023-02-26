# 문제
# 루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.
#
# 출력
# 첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.

def dfs(v):
    stack.append(1)
    stack.append(v)

    while stack:
        for k in connect[v]:
            if parent[k] == 0:
                parent[k] = v
                stack.append(k)

        v = stack.pop()

N = int(input())

connect = [[] * (N+1) for _ in range(N+1)]
parent = [0] * (N+1)
stack = []

for i in range(N-1):
    one, two = map(int, input().split())
    connect[one].append(two)
    connect[two].append(one)

for j in connect[1]:
    parent[j] = 1
    dfs(j)

for k in range(2, N+1):
    print(parent[k])


