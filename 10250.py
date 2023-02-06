T = int(input())

for t in range(T):

    H, W, N = map(int, input().split())
    
    Y = N % H
    X = N // H + 1
    if Y == 0:
        Y = H
        X = X -1    

    print(Y*100 + X)