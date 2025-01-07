# 문제
# 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.

# 출력
# N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.



'''
N = int(input())
n = 2

if N == 1:
    print()
else:
    while N > 1:
        if N % n == 0:            
            print(n)
            N = N // n
        else:
            n += 1
'''





#2025.01.07
'''  내가 짠 코드 (메모리 : 32412KB / 시간 : 1416ms)
N = int(input())

i = 2

if N == 1:
    print()
else:
    while N > 1:
        if N % i == 0:
            print(i)
            N //= i
        else:
            i += 1
'''


''' GPT가 짠 코드 (메모리 : 34536KB / 시간 : 40ms)
import math

N = int(input())
i = 2  # 첫 번째 소인수

if N == 1:
    print()
else:
    while i * i <= N:  # i를 sqrt(N)까지만 확인
        while N % i == 0:  # i로 나누어떨어지면 출력
            print(i)
            N //= i
        i += 1 if i == 2 else 2  # 2 이후에는 홀수만 검사
                                 # i가 2면 +1로 i를 3으로 만든다는 얘기
                                 # i가 만약 3이면 +2로 5로 만들어 계속해서 홀수로만 검사하겠다는 뜻

    if N > 1:  # 남은 N이 1보다 크면 그것도 소인수
        print(N)
'''