f_festival = [0] * 101
s_festival = [0] * 65

# 첫 번째 페스티벌
cnt = 1
for prize, num in [(5000000, 1), (3000000, 2), (2000000, 3), (500000, 4), (300000, 5), (100000, 6)]:
    for _ in range(num):
        if cnt < len(f_festival):
            f_festival[cnt] = prize
            cnt += 1

# 두 번째 페스티벌
cnt = 1
for prize, num in [(5120000, 1), (2560000, 2), (1280000, 4), (640000, 8), (320000, 16)]:
    for _ in range(num):
        if cnt < len(s_festival):
            s_festival[cnt] = prize
            cnt += 1



T = int(input())

for t in range(T):
    first, second = map(int, input().split())
    print(f_festival[first] + s_festival[second])



