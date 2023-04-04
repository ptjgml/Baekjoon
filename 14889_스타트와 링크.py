def per(idx, start):
    global result
    if idx == M:
        team_link = list(set(lst) - set(team_start))
        sum1 = cal(team_start)
        sum2 = cal(team_link)

        if result > abs(sum1 - sum2):
            result = abs(sum1 - sum2)

        return

    else:
        for i in range(start, N):
            team_start.append(lst[i])
            per(idx+1, i+1)
            team_start.pop()

def cal(team):
    sumV = 0
    for i in range(M):
        for j in range(M):
            if i!= j:
                sumV += (S_lst[team[i]-1][team[j]-1])
    return sumV

N = int(input())
M = N//2
lst = list(range(1, N+1))
S_lst = [list(map(int, input().split())) for _ in range(N)]
team_start = []
team_link = []
start = 0
result = 10000
per(0, start)
print(result)


