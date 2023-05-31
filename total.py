points = [0]*4
scores = []
for i in range(4):
    scores.append(list(map(int, input().split())))

for i in range(4):
    for j in range(i, 4):
        if i==j:
            continue
        else:
            if scores[i][j] > scores[j][i]:
                points[i] += 3
                points[j] += 0
            elif scores[i][j] == scores[j][i]:
                points[i] += 1
                points[j] += 1
            else:
                points[i] += 0
                points[j] += 3

print(*points)

