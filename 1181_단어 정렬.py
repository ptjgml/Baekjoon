# 문제
# 알파벳 소문자로 이루어진 N개의 단어가 들어오면 
# 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

# 길이가 짧은 것부터
# 길이가 같으면 사전 순으로
# 단, 중복된 단어는 하나만 남기고 제거해야 한다.

# 입력
# 첫째 줄에 단어의 개수 N이 주어진다. 
# (1 ≤ N ≤ 20,000) 둘째 줄부터 N개의 줄에 걸쳐 
# 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다.
# 주어지는 문자열의 길이는 50을 넘지 않는다.

# 출력
# 조건에 따라 정렬하여 단어들을 출력한다.


# import sys
# N = int(input())

# lst = []
# length_lst = [0] * N
# for i in range(N):
#     word = input()
#     word_length = len(word)
#     lst.append((word, word_length))

# for i in N:
#     lst.sort(key = lambda x : lst[i][1])




import sys
N = int(input())

lst = []
for i in range(N):
    word = input()
    lst.append(word)

sort_set = list(set(lst))

sort_set.sort()     # 알파벳 순으로 정렬
sort_set.sort(key = lambda x : len(x))  # 길이 순으로 정렬

for word in sort_set:
    print(word)
