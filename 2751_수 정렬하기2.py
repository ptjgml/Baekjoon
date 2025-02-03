# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 
# 둘째 줄부터 N개의 줄에는 수가 주어진다.
# 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.


'''
import sys

N = int(sys.stdin.readline())
lst = []
for i in range(N):
    lst.append(sys.stdin.readline())

lst.sort()
for j in lst:
    print(j)   
'''    





#2025.02.03

import sys

N = int(sys.stdin.readline())

num_lst = list()

for i in range(N):
    num = int(sys.stdin.readline())
    num_lst.append(num)

num_lst.sort()

print(*num_lst, sep='\n')