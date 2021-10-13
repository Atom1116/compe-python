
# バブルソート
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(n - 1, i, -1):
            if array[j - 1] > array[j]:
                array[j], array[j - 1] = array[j - 1], array[j]
    return array


if __name__ == "__main__":
    dadas = [5, 3, 6, 3, 2, 76, 8, 4]

    print(bubble_sort(dadas))
