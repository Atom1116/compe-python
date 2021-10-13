# 挿入ソート
# def insertion_sort(array):
#     n = len(array)
#     for i in range(1, n):
#         tmp = array[i]  # 挿入する値を退避
#         j = i
#         while True:
#             if j != 0 and array[j - 1] > tmp:
#                 array[j] = array[j - 1]  # tmpより大きいものは後ろへずらす
#             else:
#                 break  # tmp以下になったら止める
#             j -= 1
#         array[j] = tmp  # 空いた位置に退避していた値を挿入
#     return array


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        # print(i)
        # print(j)
        ele = arr[i]
        print(arr)
        while arr[j] > ele and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = ele

    return arr


if __name__ == "__main__":
    dadas = [5, 3, 6, 3, 2, 76, 8, 4]

    for i in range(1, 8):
        print(i)
    print(insertion_sort(dadas))
