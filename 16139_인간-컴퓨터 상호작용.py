# 문제
# 승재는 인간-컴퓨터 상호작용에서 생체공학 설계를 공부하다가 키보드 자판이 실용적인지 궁금해졌다. 이를 알아보기 위해 승재는 다음과 같은 생각을 했다.
#
# '문자열에서 특정 알파벳이 몇 번 나타나는지 알아봐서 자주 나타나는 알파벳이 중지나 검지 위치에 오는 알파벳인지 확인하면 실용적인지 확인할 수 있을 것이다.'
#
# 승재를 도와 특정 문자열
# $S$, 특정 알파벳
# $\alpha$와 문자열의 구간
# $[l,r]$이 주어지면
# $S$의
# $l$번째 문자부터
# $r$번째 문자 사이에
# $\alpha$가 몇 번 나타나는지 구하는 프로그램을 작성하여라. 승재는 문자열의 문자는
# $0$번째부터 세며,
# $l$번째와
# $r$번째 문자를 포함해서 생각한다. 주의할 점은 승재는 호기심이 많기에 (통계적으로 크게 무의미하지만) 같은 문자열을 두고 질문을
# $q$번 할 것이다.
#
# 입력
# 첫 줄에 문자열
# $S$가 주어진다. 문자열의 길이는
# $200,000$자 이하이며 알파벳 소문자로만 구성되었다. 두 번째 줄에는 질문의 수
# $q$가 주어지며, 문제의 수는
# $1\leq q\leq 200,000$을 만족한다. 세 번째 줄부터
# $(q+2)$번째 줄에는 질문이 주어진다. 각 질문은 알파벳 소문자
# $\alpha_i$와
# $0\leq l_i\leq r_i<|S|$를 만족하는 정수
# $l_i,r_i$가 공백으로 구분되어 주어진다.
#
# 출력
# 각 질문마다 줄을 구분해 순서대로 답변한다.
# $i$번째 줄에
# $S$의
# $l_i$번째 문자부터
# $r_i$번째 문자 사이에
# $\alpha_i$가 나타나는 횟수를 출력한다.


# 50점 풀이
import sys
S = sys.stdin.readline()
q = int(sys.stdin.readline())

for i in range(q):
    a,start, end = sys.stdin.readline().split()
    print(S[int(start):int(end)+1].count(a))



# 100점 풀이
import sys
input = sys.stdin.readline

s = input().rstrip()
arr = [[0]*26]
arr[0][ord(s[0])-97] = 1
for i in range(1,len(s)):
    arr.append(arr[-1][:])
    arr[i][ord(s[i])-97] += 1

for _ in range(int(input())):
    c,start,end = list(input().split())
    start,end = map(int,[start,end])
    if start == 0:
        print(arr[end][ord(c)-97])
    else:
        print(arr[end][ord(c)-97]-arr[start-1][ord(c)-97])