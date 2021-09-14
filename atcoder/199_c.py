
N = int(input())
S = list(input())
Q = int(input())

# TAB = [list(map(int, input())) for _ in range(Q)]

flag = False

# FLIP

for i in range(Q):
    t, a, b = map(int, input().split())
    if t == 1:
        if flag:
            if a > N - 1:
                a -= N
            else:
                a += N
            if b > N - 1:
                b -= N
            else:
                b += N
        tmp = S[a - 1]
        S[a - 1] = S[b - 1]
        S[b - 1] = tmp
    else:
        flag = not flag  # 反転

if flag:
    S = S[N:] + S[:N]  # 文字列の前後半入れ替え

print(''.join(S))


# N = int(input())
# S = input()
# Q = int(input())

# TAB = [list(map(int, input().split())) for _ in range(Q)]

# for i in range(Q):
#     if TAB[i][0] == 1:
#         # A番目とB番目の文字を入れ替え
#         tmp_list = list(S)
#         tmp_data = tmp_list[TAB[i][1] - 1]
#         tmp_list[TAB[i][1] - 1] = tmp_list[TAB[i][2] - 1]
#         tmp_list[TAB[i][2] - 1] = tmp_data
#         S = "".join(tmp_list)
#     else:
#         # N前半文字と後半文字を入れ替え
#         S = S[N:] + S[:N]

# print(S)
