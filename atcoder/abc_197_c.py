import sys
input = sys.stdin.readline


N = int(input())
data_list = list(map(int, input().split()))


ans = 2**30+1



for i in range(1<<N):
    OR,XOR = 0, 0
    # 00111
    # 00110
    for j in range(N):
        OR = OR | data_list[j]
        if i >> j & 1:
            XOR = XOR ^ OR
            # 連続した区画のORを求めるので0にリセット
            OR = 0
    
    XOR = XOR ^ OR
    ans = min(ans, XOR)


print(ans)