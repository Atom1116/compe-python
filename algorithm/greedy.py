# 貪欲法
# 後先考えず、「その場での最善」を選択することを繰り返す方法論

# コイン問題
# 500,100,50,5,1円玉がそれぞれ、a0,a1,a1,a3,a4枚あります。
# これらをもいいてXエンを払いたいとします。
# ここで支払いに用いつコインの合計枚数をなるべく少なくしたいと考えています。
# 最小で何枚のコインで支払うことができるでしょうか。
# ただし、そのような支払い方が少なくとも1つは存在するものとします。

# X = 900
# value = [500, 100, 50, 10, 5, 1]

# # a = [int(input()) for _ in range(6) ]
# a = [5, 3, 1, 5, 3, 10]
# result = 0

# for i in range(6):
#     add = X // value[i] # Xをコインの金額で割り、制限がない場合のそのコインの量を算出

#     if add > a[i]: add = a[i] # 制限を越えたら、そのコインの最大値を設定

#     X -= value[i] * add # 結果を反映
#     result += add

# print(result)


# 区画スケジュール問題
# N個の仕事があり、i(=0,1,...N-1)番目の仕事は時刻siに開始し、時刻tiに終了します
# これらの中から自分が行う仕事をできるだけ多く選びたいとします
# ただし時刻が重なっている複数の仕事を選ぶことはできません
# 最大で何この仕事をこなすことができるでしょうか

# 3 5
# 4 7
# 9 10
# 1 2
# 3 5

# N = 5

# # a = [list(map(int,input().split())) for _ in range(N)]
# a = [list(map(int, input().split())) for _ in range(N)]
# print(a)
# a = sorted(a, key=lambda x: x[1])
# print(a)
# result = 0
# current_end_time = 0

# for i in range(N):
#     if a[i][0] < current_end_time: continue # もっとも

#     result += 1
#     current_end_time = a[i][1]

# print(result)