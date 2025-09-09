# 문제
# 기다란 벤치 모양의 식탁에 사람들과 햄버거가 아래와 같이 단위 간격으로 놓여 있다. 사람들은 자신의 위치에서 거리가
# $K$ 이하인 햄버거를 먹을 수 있다.
#
# 햄버거	사람	햄버거	사람	햄버거	사람	햄버거	햄버거	사람	사람	햄버거	사람
# 1	2	3	4	5	6	7	8	9	10	11	12
# 위의 상태에서
# $K = 1$인 경우를 생각해보자. 이 경우 모든 사람은 자신과 인접한 햄버거만 먹을 수 있다. 10번의 위치에 있는 사람은 11번 위치에 있는 햄버거를 먹을 수 있다. 이 경우 다음과 같이 최대 5명의 사람이 햄버거를 먹을 수 있다.
#
# 2번 위치에 있는 사람: 1번 위치에 있는 햄버거
# 4번 위치에 있는 사람: 5번 위치에 있는 햄버거
# 6번 위치에 있는 사람: 7번 위치에 있는 햄버거
# 9번 위치에 있는 사람: 8번 위치에 있는 햄버거
# 10번 위치에 있는 사람: 11번 위치에 있는 햄버거
# 12번 위치에 있는 사람: 먹을 수 있는 햄버거가 없음
#  
# $K = 2$인 경우에는 6명 모두가 햄버거를 먹을 수 있다.
#
# 2번 위치에 있는 사람: 1번 위치에 있는 햄버거
# 4번 위치에 있는 사람: 3번 위치에 있는 햄버거
# 6번 위치에 있는 사람: 5번 위치에 있는 햄버거
# 9번 위치에 있는 사람: 7번 위치에 있는 햄버거
# 10번 위치에 있는 사람: 8번 위치에 있는 햄버거
# 12번 위치에 있는 사람: 11번 위치에 있는 햄버거
# 식탁의 길이
# $N$, 햄버거를 선택할 수 있는 거리
# $K$, 사람과 햄버거의 위치가 주어졌을 때, 햄버거를 먹을 수 있는 사람의 최대 수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫 줄에 두 정수
# $N$과
# $K$가 있다. 그리고 다음 줄에 사람과 햄버거의 위치가 문자 P(사람)와 H(햄버거)로 이루어지는 길이
# $N$인 문자열로 주어진다.
#
# 출력
# 첫 줄에 햄버거를 먹을 수 있는 최대 사람 수를 나타낸다.
#
# 제한
#  
# $1 \le N \le 20,000$ 
#  
# $1 \le K \le 10$ 
# 예제 입력 1
# 20 1
# HHPHPPHHPPHPPPHPHPHP
# 예제 출력 1
# 8
# 예제 입력 2
# 20 2
# HHHHHPPPPPHPHPHPHHHP
# 예제 출력 2
# 7


'''
시간초과 풀이
N, K = map(int, input().split())
hp = list(input())

hamburger = []
people = []

for i, val in enumerate(hp):
    if val == 'P':
        people.append(i)
    else:
        hamburger.append(i)


people_ate = [False] * N
hamburger_dic = {idx: [] for idx, val in enumerate(hp) if val == 'H'}

cnt = 0

for h_idx in hamburger:
    for p_idx in people:
        if abs(h_idx - p_idx) <= K:
            hamburger_dic[h_idx].append(p_idx)


for key, value in hamburger_dic.items():
    if value:
        for v in value:
            if people_ate[v] == False:
                people_ate[v] = True
                cnt += 1
                break

print(cnt)
'''





#투포인터 사용(시간복잡도 O(N))
N, K = map(int, input().split())
hp = list(input())

hamburger = []
people = []

for i, val in enumerate(hp):
    if val == 'P':
        people.append(i)
    else:
        hamburger.append(i)

h = 0
p = 0

cnt = 0
while 0 <= h < len(hamburger) and 0 <= p < len(people):
    if abs(hamburger[h] - people[p]) <= K:
        cnt += 1
        h += 1
        p += 1

    elif people[p] < hamburger[h] - K:
        p += 1

    else:
        h += 1

print(cnt)







#한번 스캔(시간복잡도 O(NxK))
N, K = map(int, input().split())
arr = list(input().strip())
used = [False] * N

cnt = 0
for i, ch in enumerate(arr):
    if ch == 'P':
        left = max(0, i - K)
        right = min(N - 1, i + K)
        for j in range(left, right + 1):
            if arr[j] == 'H' and not used[j]:
                used[j] = True
                cnt += 1
                break

print(cnt)

















