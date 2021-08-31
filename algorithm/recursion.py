# 再帰・分割統治法

# 1-Nまでの総和を求める関数
# def func(n):
#     if n == 0:
#         return 0
#     return n + func(n - 1)

# ans = func(5)
# print(ans)

# ユークリッドの互除法
# 2つの整数 m,nの最大公約数を求めるアルゴリズム

# def GCD(m, n):
#     if n == 0:
#         return m
#     return GCD(n, m % n)

# print(GCD(51, 15))

# フィボナッチ数列
# F0 = 0
# F1 = 1
# Fn = FN_1 + Fn_2(N=2,3,...)

# def fibo(n):
#     print(f"fibo{n}を呼び出しました。")
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
    
#     result = fibo(n - 1) + fibo(n - 2)
#     print(f'{n}項目= {result}')

#     return result
# fibo(6)


# メモ化して動的計画法へ
# memo = [0] * 20
# def fibo(n):
#     global memo
#     # print(f"fibo{n}を呼び出しました。")
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
    
#     if memo[n]:
#         return memo[n]
    
#     memo[n] = fibo(n - 1) + fibo(n - 2)
#     # print(f'{n}項目= {memo[n]}')

#     return memo[n]
    
# fibo(6)
# print(memo)
# print(memo[6])


# 部分和問題を再帰関数を用いる全探索で解く
def func(i, w, a):
    # iが0の場合（これ以上、配列から値を差し引くことができなくなった場合）
    if i == 0:
        if w == 0: return True
        else: return False

    # a[i-1]を選ばない場合
    if func(i-1, w,a): return True
    # a[i-1]を選ぶ場合
    if func(i - 1, w - a[i - 1], a): return True

    # どちらもFalseの場合
    return False


n = 4 #　配列の長さ
w = 1 # 目標値
a = [3, 2, 6, 5] # 探索配列

print(func(n, w, a))


# TODO:P59　章末問題4.6を解く


    