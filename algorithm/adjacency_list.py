# 隣接リスト

n, m = map(int, input().split())

# 重みなし隣接リスト
graph = [[] for _ in range(n)]
for _ in range(n):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1) # 有効グラフなら消す

print(graph)

# 重みあり隣接リスト
# graph_w = [[] for _ in range(n)]
# for _ in range(n):
#     u, v, w = map(int, input().split())
#     graph_w[u-1].append([v-1, w])
#     graph_w[v-1].append([u-1, w]) # 有効グラフなら消す
#
# print(graph_w)