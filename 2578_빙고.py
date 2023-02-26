# 문제
# 빙고 게임은 다음과 같은 방식으로 이루어진다.

# 먼저 아래와 같이 25개의 칸으로 이루어진 빙고판에 
# 1부터 25까지 자연수를 한 칸에 하나씩 쓴다

# 다음은 사회자가 부르는 수를 차례로 지워나간다. 
# 예를 들어 5, 10, 7이 불렸다면 이 세 수를 지운 뒤 빙고판의 모습은 다음과 같다.

# 차례로 수를 지워가다가 같은 가로줄, 세로줄 또는 대각선 위에 있는 
# 5개의 모든 수가 지워지는 경우 그 줄에 선을 긋는다.

# 이러한 선이 세 개 이상 그어지는 순간 "빙고"라고 외치는데, 
# 가장 먼저 외치는 사람이 게임의 승자가 된다.

# 철수는 친구들과 빙고 게임을 하고 있다. 
# 철수가 빙고판에 쓴 수들과 사회자가 부르는 수의 순서가 주어질 때, 
# 사회자가 몇 번째 수를 부른 후 철수가 "빙고"를 외치게 되는지를 
# 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄부터 다섯째 줄까지 빙고판에 쓰여진 수가 
# 가장 위 가로줄부터 차례대로 한 줄에 다섯 개씩 빈 칸을 사이에 두고 주어진다.
# 여섯째 줄부터 열째 줄까지 사회자가 부르는 수가 
# 차례대로 한 줄에 다섯 개씩 빈 칸을 사이에 두고 주어진다. 
# 빙고판에 쓰여진 수와 사회자가 부르는 수는 
# 각각 1부터 25까지의 수가 한 번씩 사용된다.

# 출력
# 첫째 줄에 사회자가 몇 번째 수를 부른 후 
# 철수가 "빙고"를 외치게 되는지 출력한다.

# 2578 빙고

import sys
def check(num):               # 불린 수를 0으로 체크 할 check 함수
    for n in range(5):
        for m in range(5):
            if bingo[n][m] == num:
                bingo[n][m] = 0
                return

def bin(bingo):             # 빙고가 됐는지 확인 할 bin 함수
    x_cnt = 0
    reverse_x_cnt = 0
    total_cnt = 0

    for n in range(5):    
        row_cnt = 0
        for m in range(5):
            if bingo[n][m] == 0:
                row_cnt += 1
                if row_cnt == 5:
                    total_cnt += 1
                    row_cnt = 0
            else:
                break    
            
        col_cnt = 0
        for m in range(5):
            if bingo[m][n] == 0:
                col_cnt += 1
                if col_cnt == 5:
                    total_cnt += 1
                    col_cnt = 0
            else:
                break

        if bingo[n][n] == 0:
            x_cnt += 1
            if x_cnt == 5:
                total_cnt += 1
                x_cnt = 0

        if bingo[n][4-n] == 0:
            reverse_x_cnt += 1
            if reverse_x_cnt == 5:
                total_cnt += 1
                reverse_x_cnt = 0
    
    return total_cnt 
   


lst = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]  # 입력을 받을 리스트
bingo = lst[0:5]        # lst에서 1~5번째 줄 bingo에 저장
call = sum(lst[5:], [])          # lst에서 6~10번째 줄 call에 저장
count = 0               # 빙고 선이 몇 개 그어지는지 count
call_count = 0          # 사회자가 몇 번째 수를 부르는지 count

for num in call:        
    call_count += 1
    check(num)
    count = bin(bingo)
    if count >= 3:
        print(call_count)
        break



