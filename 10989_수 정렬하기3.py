# 문제
# N개의 수가 주어졌을 때,
#  이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 
# 둘째 줄부터 N개의 줄에는 수가 주어진다. 
# 이 수는 10,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.


'''
<틀린 코드>
import sys
N = int(input())
lst = [0] * N

for i in range(N):
    lst[i] = int(sys.stdin.readline())

lst.sort()
for j in lst:
    print(j)
    
- 리스트를 이용하면 메모리 초과가 나므로 
- 딕셔너리를 이용하여 최대한 적은수를 저장해놓고
- 해당 수가 입력된 수를 count 하여 출력한다.
'''

import sys
N = int(input())
dic = {}

for i in range(N):
    num = int(sys.stdin.readline())
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1

dic_keys = sorted(dic.keys())

for j in dic_keys:
    for k in range(dic[j]):
        print(j)


