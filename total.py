'''
# n과 m

def per(idx, M):
    if idx == M:
        for i in stack:
            print(i, end=' ')
        print()
        return

    for i in range(N):
        if visited[i] == False:
            stack.append(lst[i])
            visited[i] = True
            per(idx+1, M)
            visited[i] = False
            stack.pop()

N, M = map(int, input().split())

lst = list(range(1, N+1))
length = len(lst)
visited = [False] * length
stack = []

per(0, M)
'''


# 개미
w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

total_p = p+t
total_q = q+t
result_p = 0
result_q = 0

if (total_p // w) % 2 == 0:
    result_p = 0 + (total_p % w)
else:
    result_p = w - (total_p % w)

if (total_q // h) % 2 == 0:
    result_q = 0 + (total_q % h)
else:
    result_q = h - (total_q % h)

print(result_p, result_q)




























