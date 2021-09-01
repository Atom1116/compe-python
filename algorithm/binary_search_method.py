# 2分探索法

N = 8
a = [3,5,6,10,14,17,21,39]


# 目的の値keyの添字を返す
def binary_search(key):
    left, right = 0, len(a)-1

    while right >=left:
        mid = left + (right-left)//2
        if a[mid] == key: return mid
        elif a[mid] > key: right = mid -1
        elif a[mid] < key: left = mid +1
    
    return -1

print(binary_search(10))
print(binary_search(3))