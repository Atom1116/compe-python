import sys
input = sys.stdin.readline

N = int(input())

S = ''

while N > 0:

    if N%2 != 0:
        S = 'A' + S
        N -= 1 # aの魔法の処理
    else:
        # 偶数の場合
        S = 'B' + S
        N //=2 # bの魔法の処理
        # N /=2 こちらだとWA
print(S)

# import sys
# sys.setrecursionlimit(10**8) #再帰関数の呼び出し制限

# 幅優先探索
# def dfs(S, sum_magic, magic):

#     if len(S) == 121:
#         return
     
#     if magic == 0:
#         # aの魔法の処理
#         sum_magic += 1
#         S += 'A'
#     else:
#         # bの魔法の処理
#         sum_magic *= 2
#         S += "B"

#     if sum_magic == N:
#         print(S)
#         sys.exit()
    
#     dfs(S, sum_magic, 0) # aの魔法
#     dfs(S, sum_magic, 1) # bの魔法

# if N == 0:
#     # 0であればbの魔法のみの解答をする
#     print('B')
#     sys.exit()

# dfs('', 0, 1)