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

weights = [2, 1, 3, 2, 1, 3, 5]
values = [3, 2, 6, 1, 3, 85]

n = len(weights)

W = 15 # 重さの基準（重さの総和が超えないようにする）

dp = [[0] * (W + 1) for _ in range(n + 1)]
# print(dp)

for i in range(n+1):
    for w in range(W):

        print(i,w)
        # i番目の品物を選ぶ場合
        if w - weights[i] >= 0:
            dp[i+1][w] = max(dp[i+1][w], dp[i][w-weights[i]] + values[i])
        # i番目の品物を選ばない場合
        dp[i + 1][w] = dp[i][w]

print(dp)