# 문제
# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
#
# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N이 주어진다. (1 ≤ N < 15)
#
# 출력
# 첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.
def per(idx):
    global cnt

    # if idx == N:
    #     cnt += 1
    #     return

    for i in range(N):
        if i not in p[0:idx] and (i-1 != p[idx-1] or i+1 != p[idx-1]):
            p[idx] = i
            if idx+1 == N:
                print('p : ', p)
                cnt += 1
                return
            per(idx+1)
            p[idx] = -99
        else:
            continue

        # print(p[idx])
        # print(p[0:idx])

        # res = check(p, idx)
        # if res == True:
        #     per(idx+1)
        #

# def check(p, idx):
#     for k in range(0, idx):
#         if p[idx] == p[k]:
#             return False
#     return True

N = int(input())

cnt = 0
p = [-99] * N

per(0)
print(cnt)
