B_len = int(input())
B = list(map(int, input().split()))

A = [0] * B_len
A[0] = B[0]
s = A[0]

for i in range(1, B_len):
    A[i] = (B[i] * (i+1)) - s
    s += A[i]

print(*A, sep=' ')
