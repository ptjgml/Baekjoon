# 문제
# 임한수와 임문빈은 서로 사랑하는 사이이다.
#
# 임한수는 세상에서 팰린드롬인 문자열을 너무 좋아하기 때문에,
# 둘의 백일을 기념해서 임문빈은 팰린드롬을 선물해주려고 한다.
#
# 임문빈은 임한수의 영어 이름으로 팰린드롬을 만들려고 하는데,
# 임한수의 영어 이름의 알파벳 순서를 적절히 바꿔서 팰린드롬을 만들려고 한다.
#
# 임문빈을 도와 임한수의 영어 이름을 팰린드롬으로 바꾸는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 임한수의 영어 이름이 있다. 알파벳 대문자로만 된 최대 50글자이다.
#
# 출력
# 첫째 줄에 문제의 정답을 출력한다. 만약 불가능할 때는 "I'm Sorry Hansoo"를 출력한다.
# 정답이 여러 개일 경우에는 사전순으로 앞서는 것을 출력한다.

name = list(input())
al_dic = {}

for i in range(len(name)):
    if name[i] in al_dic:
        al_dic[name[i]] += 1
    else:
        al_dic[name[i]] = 1

even = 0
odd = 0
al_lst = []
num_lst = []
word = ''
for al in al_dic.keys():
    if al_dic[al] % 2 == 0:
        even += 1
        al_lst.append(al)
        num_lst.append(al_dic[al]//2)
    else:
        odd += 1
        if al_dic[al] > 1:
            al_lst.append(al)
            num_lst.append((al_dic[al]-1)//2)
        word = al


# pel = ''
pel = []
if odd > 1:
    print('I\'m Sorry Hansoo')
    exit()
else:
    while len(al_lst) > 0:
        maxV = max(num_lst)
        maxIdx = num_lst.index(maxV)
        # pel += al_lst[maxIdx]
        pel.append(al_lst[maxIdx])
        num_lst[maxIdx] -= 1
        if num_lst[maxIdx] == 0:
            al_lst.pop(maxIdx)
            num_lst.pop(maxIdx)

# print(pel)
pel.sort()
pel = ''.join(pel)
reverse_pel = pel[::-1]

if len(word)>0:
    print(pel+word+reverse_pel)
else:
    print(pel+reverse_pel)



















# name = list(input())
# al_lst = []
# num_lst = []
#
# for i in range(len(name)):
#     if name[i] in al_lst:
#         num_lst[al_lst.index(name[i])] += 1
#     else:
#         al_lst.append(name[i])
#         num_lst[al_lst.index(name[i])] = 1
#
# even = 0
# odd = 0
# for num in range(len(num_lst)):
#     if num_lst[num] % 2 == 0:
#         even += 1
#     else:
#         odd += 1
#
# if odd > 1:
#     print('I\'m Sorry Hansoo')
#
# else:
#     print(al_lst)
#     print(num_lst)
