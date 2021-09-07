
N, K = map(int, input().split())
c = list(map(int, input().split()))

cnt = 0

# 探索するリストを横にずらす
# つまり、最初を削除し、追加する

# for i in range(N - K + 1):
#     tmp = set()
#     for j in range(K):
#         tmp.add(c[i+j])
#
#     cnt = max(cnt, len(tmp))
#
# print(cnt)

search = []

# KとNが同じならその中の重複数が答え
if K == N:
    print(len(set(c)))
    exit()

# 最初の探索リストを作成
for i in range(K):
    search.append(c[i])

for i in range(K, N - K + 1):
    print(i)
    search.pop(0) # 最初を削除
    search.append()
