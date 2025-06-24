N, M = map(int, input().split())
J = int(input())

basket = [1, M]  # 바구니의 현재 왼쪽, 오른쪽 끝
move = 0

for _ in range(J):
    apple = int(input())
    
    if basket[0] <= apple <= basket[1]:
        continue  # 현재 바구니 범위에 있으면 이동 X
    elif apple < basket[0]:
        dist = basket[0] - apple  # 왼쪽으로 이동해야 하는 거리
        basket[0] -= dist
        basket[1] -= dist
        move += dist
    else:  # apple > basket[1]
        dist = apple - basket[1]  # 오른쪽으로 이동해야 하는 거리
        basket[0] += dist
        basket[1] += dist
        move += dist

print(move)
