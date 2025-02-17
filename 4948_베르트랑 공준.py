# 문제
# 베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.

# 이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.

# 예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. (11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)

# 자연수 n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오. 

# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 케이스는 n을 포함하는 한 줄로 이루어져 있다.

# 입력의 마지막에는 0이 주어진다.

# 출력
# 각 테스트 케이스에 대해서, n보다 크고, 2n보다 작거나 같은 소수의 개수를 출력한다.


'''
import sys

while True:       
    n = int(sys.stdin.readline())

    if n >= 1:

        check_lst = [0] * (2*n +1)
        for i in range(n+1):
            check_lst[i] = 1

        for i in range(2, int((n*2) ** 0.5)+1):
            for j in range(i*2, (n*2)+1, i):
                check_lst[j] = 1
        count = 0
        for k in range(n, (2*n)+1):
            if check_lst[k] == 0:
                count += 1
        print(count)   
        
    else:
        break
'''




#2025.02.17

import sys

MAX_N = 123456      #n의 범위가 1 <= n <= 123456
MAX_LIMIT = 2 * MAX_N

#에라토스테네스의 체로 소수를 미리 구함함
is_prime = [True] * (MAX_LIMIT + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(MAX_LIMIT ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX_LIMIT + 1, i):
            is_prime[j] = False

#누적합 배열로 소수 개수를 빠르게 찾도록 최적화화
prime_count = [0] * (MAX_LIMIT + 1)

for i in range(1, MAX_LIMIT + 1):
    prime_count[i] = prime_count[i-1] + (1 if is_prime[i] else 0)

#입력 처리 및 결과 출력
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    print(prime_count[2*n] - prime_count[n])


