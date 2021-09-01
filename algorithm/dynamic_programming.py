# 動的計画法
# print('Dynamic programming')


# AtCoder Educational DP Contest A Flag 1
# n = 7
# h = [2, 9, 4, 5, 1, 6, 10]

# dp = [0] * 7  # dp配列を作成

# for i in range(n):
#     if i == 1:
#         # nが1の時はh[1]との差がdp[0]に入る
#         dp[i] = abs(h[i] - h[i - 1])
#     else:
#         # 1つ前からの移動と2つ前からの移動の絶対値の最小をdp[i]に入れる
#         dp[i] = min(dp[i - 1] + abs(h[i] - h[i - 1]), dp[i - 2] + abs(h[i] - h[i - 2]))
    
#     # for文が終わる時、dpリストが満たされる

# print(dp[n - 1])



# ナップザック問題
# N個の品物があり、i(0,1,...N)番目の品物の重さはweight_i,価値はvalue_iで与えられます。
# このN個の品物から、重さの総和がWを超えないようにmいくつか選びます。
# 選んだ品物の価値の総和として考えられる最大値を求めてください（W,wight_i>0）

# weights = [2, 1, 3, 2, 1, 3, 5]
# values = [3, 2, 6, 1, 3, 85]

# n = len(weights)

# W = 15 # 重さの基準（重さの総和が超えないようにする）

# dp = [[0] * (W+1) for i in range(n)]

# for i in range(n-1):
#     for w in range(W):
#         # i番目の品物を選ぶ場合
#         if w - weights[i] >= 0:
#             # print(dp[i+1][w])
#             # print(dp[i][w-weights[i]] + values[i])
#             # print(max(dp[i+1][w], dp[i][w-weights[i]] + values[i]))
#             dp[i+1][w] = max(dp[i+1][w], dp[i][w-weights[i]] + values[i])
#         # i番目の品物を選ばない場合
#         else:
#             dp[i+1][w] = dp[i][w]

# print(dp)

# 編集距離
# ２つの文字列S,Tが与えられます。Sに以下の３通りの操作を繰り返す施すことでTに変換したいものとします。
# そのような一連の捜査のうち、操作回数の最小値を求めてください、なおこの最小値をSとTとの編集距離と呼びます。
# 変更：S中の文字を１つ選んで任意の文字に変更する。
# 削除：S中の文字を一つ選んで削除する。
# 挿入：S中の好きな箇所に好きな文字を１文字挿入する。

def chmin(a, b):
    if a > b:
        a = b

S = "logistic"
T = "algorithm"

INF = 10*100
print(INF)

dp = [[INF]*(len(T)+1) for _ in range(len(S)+1)]
dp[0][0] = 0
for i in range(len(S)+1):
    for j in range(len(T)+1):
        # 変更処理
        if i > 0 and j > 0:
            if S[i-1] == T[j-1]:
                dp[i][j]= min(dp[i][j], dp[i-1][j-1])
            else:
                dp[i][j]= min(dp[i][j], dp[i-1][j-1] + 1) # dpテーブルを斜め方向移動
        # 削除操作
        if i>0: dp[i][j]= min(dp[i][j], dp[i-1][j] + 1) # dpテーブルを列方向移動

        # 挿入操作
        if j>0: dp[i][j]= min(dp[i][j], dp[i][j-1] + 1) # dpテーブルの行方向移動

print(dp)
print(dp[len(S)][len(T)])

# 区間分割の仕方を最適化する問題
# N個の要素が１列に並んでいて、これをいくつかの区間に分割したいものとします。
# 各区間[i, r)にはスコアcl,rがついているとします。
# KをN以下の性の整数としてK+1個の整数t0,t1,...tkを、0= t0<t1<...[tk-1, tk)を満たすように取った時
# 区間分割[t0, t1),[t1, t2),...[tk-1, tk)のスコアを
# ct0t1 + ct1t2,...ct-1tk
# によって定義します。N要素の区間分割の仕方を全て考えた時の、考えられるスコアの最小値を求めてください

