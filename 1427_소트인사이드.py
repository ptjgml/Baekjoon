# 문제
# 배열을 정렬하는 것은 쉽다. 
# 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

# 입력
# 첫째 줄에 정렬하려고 하는 수 N이 주어진다. 
# N은 1,000,000,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.

# N = input()
# lst = []

# for i in N:
#     lst.append(i)

# for i in range(len(lst)-1,0,-1):
#     minV = int(lst[i])
#     for j in range(i+1):
#         if int(lst[j]) <= minV:
#             minV = int(lst[j])
#             minIdx = j
#     lst[minIdx], lst[i] = lst[i], lst[minIdx]


# num = ''.join(lst)
# print(num)




# 백준 2587 대표값2
import sys

lst = []
sumV = 0
avgV = 0
for i in range(5):
    num = int(sys.stdin.readline())
    lst.append(num)
    sumV += num

lst.sort()
print(int(sumV / 5))
print(lst[5//2])




