# 문제
# 수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 
# 이 좌표에 좌표 압축을 적용하려고 한다.

# Xi를 좌표 압축한 결과 
# X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.

# X1, X2, ..., XN에 좌표 압축을 적용한 결과
# X'1, X'2, ..., X'N를 출력해보자.

# 입력
# 첫째 줄에 N이 주어진다.

# 둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.

# 출력
# 첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.

# 제한
# 1 ≤ N ≤ 1,000,000
# -109 ≤ Xi ≤ 109


'''
<문제 해석>
입력 받은 수를 오름차순 정렬 했을 때 
그 수의 인덱스 값을 출력하라

<틀린 코드>
import sys
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
new_lst = sorted(set(lst))  
index_lst = [0] * N
for i in range(N):
    index_lst[i] = new_lst.index(lst[i])

print(*index_lst)


 - 리스트를 이용하여 모든 수의 인덱스를 저장하면 시간이 너무 오래걸린다
 - 겹치는 수가 있을 수 있기 때문에 set를 이용하여 중복값을 제거 후
 - sort를 이용해 입력받은 수들을 정렬한다(중복값 빼고)
 - 딕셔너리에 정렬된 수들과 해당 수의 인덱스 값을 저장하고
 - 처음 입력받은 수들을 딕셔너리에서 key 값으로 찾으며 해당 key의 value 값을 출력한다
 
'''


import sys
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

new_lst = sorted(set(lst))

index_dic = {}
for i in range(len(new_lst)):
    index_dic[new_lst[i]] = i

for j in lst:
    print(index_dic[j], end=' ')


