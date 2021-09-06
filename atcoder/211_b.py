
enpitsu = ['H', '2B', '3B', 'HR']
a = [input() for _ in range(4)]

# def my_index(l, x, default=False):
#     if x in l:
#         return l.index(x)
#     else:
#         return default

for i in range(4):
    # index = my_index(enpitsu, a[i], -1)
    # if index == -1:
    #     continue
    try:
        enpitsu.remove(a[i])
    except:
        continue


print('Yes' if len(enpitsu) == 0 else 'No')