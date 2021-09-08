
N, X = map(int, input().split())
a = map(int, input().split())

tmp = []
for i, j in enumerate(a):
    if (i + 1) % 2 == 0:
        tmp.append(j - 1)
    else:
        tmp.append(j)

print('Yes' if X >= sum(tmp) else 'No')
