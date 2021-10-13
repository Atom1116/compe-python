
S = input()
for i in range(10):
    T = "0" * i + S
    if T == T[::-1]:
        print("Yes")
        exit()
print("No")


# N = list(input())
# N = list(map(int, N))

# cnt_left_zero = 0

# N.reverse()

# for n in N:
#     if n == 0:
#         cnt_left_zero += 1

# for i in range(cnt_left_zero):
#     N.append(0)

# is_ok = False
# half_index = len(N) // 2

# if len(N) % 2 == 0:
#     back = N[half_index:]
#     back.reverse()
#     is_ok = N[:(half_index)] == back
# else:
#     back = N[(half_index + 1):]
#     back.reverse()
#     is_ok = N[:(half_index)] == back

# print('Yes' if is_ok else 'No')

# for n in N[::-1]:

# is_zero = True
# cnt_same = 0

# for n in N[::-1]:

#     if is_zero:
#         if n == '0':
#             cnt += 1
#         else:
#             is_zero = False

#     if n == N[-1]:
#         cnt_same += 1

# if N[-1] != '0' and cnt_same != len(N):
#     print('No')
# elif cnt == 0:
#     print('No')
# else:
#     print('Yes')
