
targets = [[1, 2], [1, 8], [4, 6], [2, 7], [1, 9]]
# targetss = targets.sort(key = lambda x : x[0])
targets = sorted(targets, key=lambda x : x[0])
print(targets)
