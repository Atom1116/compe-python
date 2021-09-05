
# x = input()
# x_list = []
# for i in range(len(x)):
#     x_list.append(int(x[i]))

# # x_list = map(int, input().split())
# x_list = list(map(lambda x: x +20 if x == 0 else x+10, x_list))
# isWeek = False
# print(x_list)
# if x_list[0] == x_list[1] and x_list[0] == x_list[2] and x_list[0] == x_list[3]:
#     isWeek = True
# else:
#     if x_list[0]+1 == x_list[1] and x_list[1]+1 and x_list[2] and x_list[2]+1 and x_list[3]:
#         isWeek = True


# print('Week' if isWeek else 'Strong')

X = input()
x1, x2, x3, x4 = map(int, [x for x in X])
# print(x1, x2, x3, x4)
if x1==x2 and x1==x3 and x1==x4:
    print('Weak')
    exit()

is_x12 = ((x1+1) % 10) == x2
is_x23 = ((x2+1) % 10) == x3
is_x34 = ((x3+1) % 10) == x4

if is_x12 and is_x23 and is_x34:
    print('Weak')
    exit()

print('Strong')