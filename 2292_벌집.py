# 육각형으로 이루어진 벌집이 있다. 
# 그림에서 보는 바와 같이 중앙의 방 1부터 시작해서 이웃하는 방에 돌아가면서 
# 1씩 증가하는 번호를 주소로 매길 수 있다. 
# 숫자 N이 주어졌을 때, 벌집의 중앙 1에서 N번 방까지 최소 개수의 방을 지나서 갈 때 
# 몇 개의 방을 지나가는지(시작과 끝을 포함하여)를 계산하는 프로그램을 작성하시오. 
# 예를 들면, 13까지는 3개, 58까지는 5개를 지난다.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 1,000,000,000)이 주어진다.

# 출력
# 입력으로 주어진 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나는지 출력한다.


# 1   1
#         +5
# 2   6
#         +6  
# 3   12
#         +6
# 4   18
#         +6
# 5   24
# 6

# [1]   1
# [2,3,4,5,6,7] 6
# [8,9,10,11,12,13,14,15,16,17,18,19]   12
# [20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37]       18


'''
import sys
N = int(sys.stdin.readline())
end = 1
n = 1
if N == 1:
        print(1)
else:
        while True:
                length = 6*(n)
                start = end+1
                end = start + length -1
                if N <= end:
                        result = n+1
                        print(result)
                        break
                else:
                        n += 1
'''




#2024.12.23

N = int(input())

check = [1]
result = 0

while True:
    if N > check[-1]:
        check.append(check[-1] + 6*len(check))
    else:
        result = len(check)
        break
   
print(result)


