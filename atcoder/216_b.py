import sys
input = sys.stdin.readline

N = int(input())

list = [input().split() for i in range(N)]
isExist = False
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if list[i][0] == list[j][0] and list[i][1] == list[j][1]:
            isExist = True
            break

if isExist:
    print("Yes")
else:
    print("No")