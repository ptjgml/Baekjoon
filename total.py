def check(one):
    global result
    slide = [0] * N
    # print('slide : ', slide)
    for i in range(N-1):
        if abs(one[i] - one[i+1]) > 1:
            result -= 1
            return

        elif i > 0 and ((one[i-1] > one[i] and one[i] > one[i+1]) or (one[i-1] < one[i] and one[i] < one[i+1])):
            if L != 1:
                result -= 1
                return

        elif i > 0 and L == 1 and (one[i-1] > one[i] and one[i] < one[i+1]):
                result -= 1
                return

        # elif i > 0 and L > 1 and one[i-1] != one[i] and one[i] != one[i+1]:
        #     result -= 1
        #     return

        elif one[i] != one[i+1]:
            if one[i] > one[i+1]:
                if one[i+1:i+L+1].count(one[i+1]) >= L:
                    for j in range(i+1, i+L+1):
                        if slide[j] == 1:
                            result -= 1
                            return
                        slide[j] = 1
                    continue
                else:
                    result -= 1
                    return
            else:
                if one[i-L+1 : i+1].count(one[i]) >= L:
                    for j in range(i-L+1, i+1):
                        if slide[j] == 1:
                            result -= 1
                            return
                        slide[j] = 1

                    continue
                else:
                    result -= 1
                    return


N, L = map(int, input().split())
map_lst = [list(map(int, input().split())) for _ in range(N)]

result = 2*N
for ii in range(N):
    row = map_lst[ii]
    # print('row : ', row)
    check(row)
#     print('result : ', result)
#     print()
# print(result)
#
# print()
for b in range(N):
    col = []
    for a in range(N):
        col.append(map_lst[a][b])
    # print('col : ', col)
    check(col)
    # print('result : ', result)

print(result)