# 문제
# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

# 1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
# 2. X가 2로 나누어 떨어지면, 2로 나눈다.
# 3. 1을 뺀다.

# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 
# 연산을 사용하는 횟수의 최솟값을 출력하시오.

# 입력
# 첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.

# 출력
# 첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.


def three(N):
    count = 0
    if N % 3 == 0:
        count = 1
        N = N // 3
    else:
        N = N -1
        count += 1
    if dp[N] != 0:
        count += dp[N]
    else:
        return count
    return count
        
def two(N):
    count = 0
    if N % 2 == 0:
        count = 1
        N = N // 2
    else:
        N = N -1
        count += 1
    if dp[N] != 0:
        count += dp[N]
    else:
        return count
    return count

import sys
N = int(sys.stdin.readline())
dp = [0] * (N+1)
dp[1] = 0

for i in range(2, N+1):
    dp[i] = min(dp[i-1]+1, two(i), three(i))

print(dp[N])



