A, B, C, D = map(int, input().split())
if B >= C * D:
    print('-1')
    exit()

cnt = 0
while True:
    cnt += 1
    if (A + B * cnt) <= (C * D * cnt):
        print(cnt)
        break
