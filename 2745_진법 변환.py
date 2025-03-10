# 문제
# B진법 수 N이 주어진다. 이 수를 10진법으로 바꿔 출력하는 프로그램을 작성하시오.
#
# 10진법을 넘어가는 진법은 숫자로 표시할 수 없는 자리가 있다. 이런 경우에는 다음과 같이 알파벳 대문자를 사용한다.
#
# A: 10, B: 11, ..., F: 15, ..., Y: 34, Z: 35
#
# 입력
# 첫째 줄에 N과 B가 주어진다. (2 ≤ B ≤ 36)
#
# B진법 수 N을 10진법으로 바꾸면, 항상 10억보다 작거나 같다.
#
# 출력
# 첫째 줄에 B진법 수 N을 10진법으로 출력한다.

'''
num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

N, B = input().split()
N = ''.join(reversed(N))
B = int(B)
result = 0

for i in range(len(N)-1, -1, -1):
    sum = num.index(N[i]) * (B**i)
    result += sum

print(result)
'''


#2024.12.23

alpha = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 
 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 
 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35}

N, B = input().split()
N = list(N)
reverse_N = N[::-1]
B = int(B)

result = 0

for i in range(len(N)):
    if reverse_N[i].isalpha():
        num = alpha[reverse_N[i]]
    else:
        num = int(reverse_N[i])
    result += num * pow(B, i) 

print(result)




