
N = int(input())

ans = 0

while True:
    if 2**ans > N:
        break

    ans += 1

print(ans-1)