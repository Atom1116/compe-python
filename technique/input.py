
# 高速化（inputよりも10倍はやい）
import sys
input = sys.stdin.readline


# 入力が1行かつ区切りなしの場合

# 文字列が一つの場合
S = input()
# 数字が一つの場合
N = int(input())

print(S, N)

# 入力が1行で区切りありの場合
L, R = input().split()

print(L, R)
L, R = map(int, input().split())

print(L, R)


# List にしたい時
list1 = input().split()

list2 = list(map(int, input().split()))

print(list1, list2)

# タプルにしたい時
lst3 = tuple(input().split())
# intの場合
lst4 = tuple(map(int,input().split()))

# 出力して確認 
print(type(lst3), lst3, type(lst4), lst4) 



# 事前に入力される行数がわかる時
# sample
# N M    # Nが列,Mが行
# P1 Y1
# :
# PM YM

# 2 3
# 1 32
# 2 63
# 1 12

# 文字列
N, M = map(int, input().split())
P = [input().split() for i in range(M)]
# 数字
N, M = map(int,input().split()) 
P = [list(map(int,input().split())) for i in range(M)]

print(P)
