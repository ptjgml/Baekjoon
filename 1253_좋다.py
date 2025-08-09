# 문제
# N개의 수 중에서 어떤 수가 다른 수 두 개의 합으로 나타낼 수 있다면
# 그 수를 “좋다(GOOD)”고 한다.
#
# N개의 수가 주어지면 그 중에서 좋은 수의 개수는 몇 개인지 출력하라.
#
# 수의 위치가 다르면 값이 같아도 다른 수이다.
#
# 입력
# 첫째 줄에는 수의 개수 N(1 ≤ N ≤ 2,000),
# 두 번째 줄에는 i번째 수를 나타내는 Ai가 N개 주어진다.
# (|Ai| ≤ 1,000,000,000, Ai는 정수)
#
# 출력
# 좋은 수의 개수를 첫 번째 줄에 출력한다.
#
# 예제 입력 1
# 10
# 1 2 3 4 5 6 7 8 9 10
# 예제 출력 1
# 8

N = int(input())
num_lst = list(map(int, input().split()))
num_lst.sort()

cnt = 0

for idx in range(N):
    num = num_lst[idx]
    start, end = 0, N-1

    while start < end:
        if num_lst[start] + num_lst[end] == num:
            if idx == start:
                start += 1
            elif idx == end:
                end -= 1
            else:
                cnt += 1
                break

        else:
            if num_lst[start] + num_lst[end] > num:
                end -= 1
            else:
                start += 1

print(cnt)
















