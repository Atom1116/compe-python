# ビット全探索

# N個の異なる要素をいくつか選択するというケースにおいて、全パターン(2**N個）を検証すること。


# ビット演算子

# ビットシフト
a = 9
print(a, bin(a))
b = a << 1
print(b, bin(b))

c = b >> 1
print(c, bin(c))

# a = 1
# shift = a<<2
# print(bin(a))
# print(bin(shift))


# ビット全探索 例
product_list = ["A", "B"]

N = len(product_list)

for i in range(1<<N):
    print(i)

# 2**N個の数字を全て列挙
for i in range(1<<N):
    buy_list = []
    for j in range(N):
        # 2進数で1の場所を探す
        if i >> j & 1:
            buy_list.append(product_list[j])
    print(buy_list)


N = 3

for i in range(1<<N):
    s = ["0", "0", "0"]
    for j in range(N):
        if i >> j & 1:
            s[j] = "1"
    print("".join(s))