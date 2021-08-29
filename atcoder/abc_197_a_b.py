import sys

H, W, X, Y = map(int, input().split())
X -= 1
Y -= 1
P = [input() for i in range(H)]

count = 1

for i in range(1, X+1):
    if P[X-i][Y] == '.':
        count += 1
    else:
        break

for i in range(1, H-X):
    if P[X+i][Y] == '.':
        count +=1
    else:
        break

for i in range(1, Y+1):
    if P[X][Y-i] == '.':
        count+=1
    else:
        break

for i in range(1, W-Y):
    if P[X][Y+i] == '.':
        count+=1
    else:
        break

print(count)
# # x軸のチェック
# row = P[X-1]

# for i in range(W):
#     print(row[i])
#     if i == (Y-1):
#         continue
#     if row[i] != "#":
#         count += 1

# # y軸のチェック
# for i in range(H):
#     if i == (H-1):
#         continue

#     if P[i][Y-1] != "#":
#         count +=1

# print(count)