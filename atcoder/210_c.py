N, K = map(int, input().split())
c = list(map(int, input().split()))

search = [0] * 3 * (10**5)
tmp = []
# KとNが同じならその中の重複数が答え
if K == N:
    print(len(set(c)))
    exit()

for i in range(K):
    search[c[i]] += 1
    tmp.append(c[i])

ans = sum(search)

for i in range(N - K + 1):
    search[tmp[0]] -= 1
    search[c[K + i - 1]] += 1

    ans = max(ans, sum(search))

    tmp.pop(0)
    tmp.append(c[K + i - 1])

print(ans)

# # 最初の探索リストを作成
# for i in range(K):
#     search.append(c[i])

# # 初期値の設定
# cnt = len(set(search))

# for i in range(N - K + 1):
#     search.pop(0) # 最初を削除
#     search.append(c[K+i-1])

#     cnt = max(cnt, len(set(search)))

# print(cnt)
# # 7 3
# 1 2 5 4 4 5 3

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
