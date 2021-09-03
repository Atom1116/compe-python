# 2分探索法

# N = 8
# a = [3,5,6,10,14,17,21,39]


# # 目的の値keyの添字を返す
# def binary_search(key):
#     left, right = 0, len(a)-1

#     while right >=left:
#         mid = left + (right-left)//2
#         if a[mid] == key: return mid
#         elif a[mid] > key: right = mid -1
#         elif a[mid] < key: left = mid +1
    
#     return -1

# print(binary_search(10))
# print(binary_search(3))


inf = 10*10000

N = 3
K=10

a = [8, 5, 4]
b=[4, 1, 9]

# A:12

min_value = inf # 最小値を設定

b.sort() # ソート昇順

b.append(inf)

for i in range(N):
    fil = filter(lambda x: x >= K-a[i], b) # bリストの中から、規定値以上の値をフィルター
    # print(a[i])
    # print(K-a[i])
    # print(list(fil))
    min_value = min(min_value, list(fil)[0] + a[i])

print(min_value)


# 射撃王
