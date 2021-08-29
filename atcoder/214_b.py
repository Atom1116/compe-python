
S, T = map(int, input().split())

s_list = []

for i in range(S+1):
    for j in range(S+1):
        for z in range(S+1):
            if (i+j+z) <= S:
                s_list.append([i,j,z])

cnt = 0
for row in s_list:
    if (row[0]*row[1]*row[2]) <= T:
        cnt += 1

print(cnt)



# 別解
S, T = map(int, input().split())
count = 0
 
#  Sからa,bを引くことで、条件を減らす
for a in range(S+1):
  for b in range(S+1-a):
    for c in range(S+1-a-b):
      if a*b*c <= T:
        count += 1
 
print(count)