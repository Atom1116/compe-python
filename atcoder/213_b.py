
N = int(input())
# a = [list(map(int, input()), ) for i, _ in enumerate(range(N))]

# a = [list(map(int, input().split())) for _ in range(N)]


a = list(map(int, input().split()))
a_tmp = []
for i in range(N):
    a_tmp.append([i+1, a[i]])

a_tmp.sort(key=lambda x: x[1])

print(a_tmp[-2][0])