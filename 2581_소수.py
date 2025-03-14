# 문제
# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.

# 예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.

# 입력
# 입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.

# M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.

# 출력
# M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다. 

# 단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.


'''
M = int(input())
N = int(input())

check_lst = []
sumV = 0
for num in range(M, N+1):
    count = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                count += 1
                break
        if count == 0:
            sumV = sumV + num
            check_lst.append(num)

if len(check_lst) == 0:
    print('-1')

else:
    print(sumV)
    print(check_lst[0])
'''




#2025.01.07


import math

M = int(input())
N = int(input())

is_prime_lst = [True] * (N+1)
is_prime_lst[0] = is_prime_lst[1] = False

for i in range(2, int(math.sqrt(N)) + 1):
    if is_prime_lst[i]:
        for j in range(i*i, N+1, i):
            is_prime_lst[j] = False

prime_lst = [num for num in range(M, N+1) if is_prime_lst[num]]

if prime_lst:
    print(sum(prime_lst))
    print(prime_lst[0])
else:
    print(-1)
