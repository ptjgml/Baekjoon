# 문제
# N개의 수가 주어졌을 때, 
# 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 
# 둘째 줄부터 N개의 줄에는 수가 주어진다. 
# 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 
# 수는 중복되지 않는다.

# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 
# 한 줄에 하나씩 출력한다.


# 오름차순 정렬 함수 만들어서 하는 법1
# import sys
# def minsort(lst, a):
#     for i in range(a):
#         minIdx = i
#         for j in range(i+1, a+1):
#             if lst[minIdx] > lst[j]:
#                 minIdx = j
#         lst[minIdx], lst[i] = lst[i], lst[minIdx]

#     return lst

# N = int(sys.stdin.readline())
# lst = [0] * N    

# for i in range(N):
#     num = int(input())
#     lst[i] = num
#     minsort(lst, i)

# for j in range(N):
#     print(lst[j])



# import sys
# N = int(sys.stdin.readline())
# lst = [0]* N

# for i in range(N):
#     lst[i] = int(sys.stdin.readline())


# for j in range(N-1, 0, -1):
#     maxV = max(lst[0:j])
#     maxV, lst[-1] = lst[-1], maxV
    



# ------------- sort 쓰는 법 ----------------
import sys
N = int(sys.stdin.readline())
lst = []

for i in range(N):
    lst.append(int(sys.stdin.readline()))

lst.sort()
for i in lst:
    print(i)

