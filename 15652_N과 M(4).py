def per(idx, start):
    if idx == M:
        print(*result)
        return
    else:
        for i in range(start, N):
            result.append(lst[i])
            per(idx+1, i)
            result.pop()

N, M = map(int, input().split())
lst = list(range(1, N+1))
result = []
start = 0
per(0, start)


