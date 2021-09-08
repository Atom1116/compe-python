

# S = input()

# c_c = S.count('c')
# h_c = S.count('h')
# o_c = S.count('o')
# k_c = S.count('k')
# u_c = S.count('u')
# d_c = S.count('d')
# a_c = S.count('a')
# i_c = S.count('i')

# print(c_c, h_c, o_c, k_c, u_c, d_c, a_c, i_c)

# cnt = c_c * h_c * o_c * k_c * u_c * d_c * a_c * i_c # 総数

# print(cnt%(10**9 + 7))


# 動的計画法（DP）で解く
S = input()
chokudai = 'chokudai'

dp = [[0] * (len(chokudai) + 1) for _ in range(len(S) + 1)]
# print(dp)
for i in range(len(S) + 1):
    for j in range(len(chokudai) + 1):
        if j == 0:
            dp[i][j] = 1
        elif i == 0:
            dp[i][j] = 0
        elif S[i - 1] != chokudai[j - 1]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]


# print(dp)
print(dp[len(S)][8] % (10 ** 9 + 7))

# chchokudai
# [[1, 0, 0, 0, 0, 0, 0, 0, 0],
#  [1, 1, 0, 0, 0, 0, 0, 0, 0],
#  [1, 1, 1, 0, 0, 0, 0, 0, 0],
#  [1, 2, 1, 0, 0, 0, 0, 0, 0],
#  [1, 2, 3, 0, 0, 0, 0, 0, 0],
#  [1, 2, 3, 3, 0, 0, 0, 0, 0],
#  [1, 2, 3, 3, 3, 0, 0, 0, 0],
#  [1, 2, 3, 3, 3, 3, 0, 0, 0],
#  [1, 2, 3, 3, 3, 3, 3, 0, 0],
#  [1, 2, 3, 3, 3, 3, 3, 3, 0],
#  [1, 2, 3, 3, 3, 3, 3, 3, 3]]

# S = input()
# T = "chokudai"
# dp = [[0 for _ in range(8+1)] for _ in range(len(S)+1)]

# for i in range(len(S)+1):
#     for j in range(8+1):
#         if j == 0:
#             dp[i][j] = 1
#         elif i == 0:
#             dp[i][j] = 0
#         elif S[i-1] != T[j-1]:
#             dp[i][j] = dp[i-1][j]
#         else:
#             dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

# print(dp[len(S)][8] % (10**9+7))
