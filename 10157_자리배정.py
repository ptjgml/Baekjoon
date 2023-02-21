C, R = map(int, input().split())
K = int(input())

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

lst = [[0]*R for _ in range(C)]
lst[0][0] = 1

if K > (C*R):
    result = 0

else:
    row = 0
    col = 0
    i = 0
    count = 1

    while True:        
        if count == K:
            result = (row+1, col+1)
            break

        newR = row + di[i]
        newC = col + dj[i]

        if 0 > newR or newR >= C or newC < 0 or newC >= R or lst[newR][newC] == 1:
            i = (i+1) % 4

        else:        
            row = row + di[i]
            col = col + dj[i]
            lst[row][col] = 1
            count += 1   
        

print(result[0], result[1])


















