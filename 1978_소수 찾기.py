# 문제
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 입력
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

# 출력
# 주어진 수들 중 소수의 개수를 출력한다.


'''
N = int(input())

num_lst = list(map(int, input().split()))
one = 0
for num in num_lst:
    count = 0
    if num > 1:
        for check in range(2, num):
            if num % check == 0:
                count = count + 1  
        if count == 0:
            one += 1
              

print(one)
'''



#2025.01.07

import math

N = int(input())
num_lst = list(map(int, input().split()))

for i in num_lst:
    if i == 1:
        N -= 1
    elif i == 2 or i == 3:
        continue
    else:
        for j in range(2, int(math.sqrt(i))+1):
            if i % j == 0:
                N -= 1
                break

print(N)

