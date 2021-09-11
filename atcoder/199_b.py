
N = int(input())

a = map(int, input().split())
b = map(int, input().split())


a_max = max(a)
b_min = min(b)

if a_max <= b_min:
    print(b_min - a_max + 1)
else:
    print(0)
