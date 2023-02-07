# 문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

# # 일반적인 방법
# import sys
# M, N = map(int, sys.stdin.readline().split())

# if M > 1:
#     for num in range(M, N +1):
#         count = 0
#         for check in range(2, num):
#             if num % check == 0:
#                 count = 1
#                 break
#         if count == 0:
#             print(num)



# 에라토스테네스의 체 방법
import sys
M, N = map(int, sys.stdin.readline().split())

check_lst = [0] * (N +1)
check_lst[0] = 1
check_lst[1] = 1

for i in range(2, int(N ** 0.5)+1):
    for j in range(i*2, N+1, i):
        check_lst[j] = 1

for k in range(M, N+1):
    if check_lst[k] == 0:
        print(k)



