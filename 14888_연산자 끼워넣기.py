import sys
def per(idx):
    global min_result
    global max_result
    if idx == (N-1):
        result = cal(per_result)
        if result < min_result:
            min_result = result
        if result > max_result:
            max_result = result
        return

    else:
        for i in range(N-1):
            if visited[i] == False:
                per_result.append(cal_lst[i])
                visited[i] = True
                per(idx+1)
                per_result.pop()
                visited[i] = False

def cal(per_result):
    resultV = A_lst[0]
    a = 0
    for num in range(1, N):
        for i in range(a, N-1):
            if per_result[i] == '+':
                resultV += A_lst[num]
                break

            elif per_result[i] == '-':
                resultV -= A_lst[num]
                break
            elif per_result[i] == '/':
                if resultV < 0:
                    resultV = abs(resultV)
                    resultV //= A_lst[num]
                    resultV = -(resultV)
                    break
                else:
                    resultV //= A_lst[num]
                    break
            elif per_result[i] == 'x':
                resultV *= A_lst[num]
                break
        a += 1

    return resultV


N = int(sys.stdin.readline())
A_lst = list(map(int, sys.stdin.readline().split()))
cal_input_lst = list(map(int, sys.stdin.readline().split()))
cal_lst = []
for i in range(4):
    if cal_input_lst[i] > 0:
        for j in range(cal_input_lst[i]):
            if i == 0:
                cal_lst.append('+')

            if i == 1:
                cal_lst.append('-')

            if i == 2:
                cal_lst.append('x')

            if i == 3:
                cal_lst.append('/')


per_result = []
visited = [False] * (N-1)
min_result = 1e9
max_result = -1e9
per(0)

print(max_result)
print(min_result)
