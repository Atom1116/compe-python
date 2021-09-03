import itertools

S, K = input().split()

# s = S.split()
s = []
for i in range(len(S)):
    s.append(S[i])
p = list(set(itertools.permutations(s))); # setで重複を削除
p.sort()

# for i in range(len(p)):
#     print(i, p[i])
print(''.join(p[int(K)-1]))



# # import sys
# # sys.stdin=open('Python\input.txt','r')
# # sys.stdout=open('Python\output.txt','w')

# from itertools import permutations

# s,ind=map(str,input().split())
# per=list(set(permutations(s)))
# per.sort()
# # print(per)
# print(''.join(per[int(ind)-1]))