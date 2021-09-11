N = int(input())
c = map(int, input().split())

c = sorted(c)  # cを昇順でソート

before = c[0]
tmp = before
ans = before
for i in range(1, len(c)):
    if before == c[i]:
        tmp -= 1
        ans *= tmp
    else:
        tmp = (tmp - 1) + (c[i] - before)
        ans *= tmp
        before = c[i]

print(ans % (10**9 + 7))


# N = int(input())
# C = sorted(map(int, input().split()))
# ans = 1
# for i in range(N):
#     ans = ans * max(0, C[i] - i) % 1000000007
# print(ans)
