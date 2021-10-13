# ヒープ
# 配列中の添字がkである頂点の左右の子頂点の、配列中の添字がそれぞれ、2*k+1,2*k+2
# 配列中の添字がkである頂点の親頂点の、配列中の添字が、(k-1)/2

class Heap:
    heap = []

    # 挿入
    def push(self, x):
        self.heap.append(x)
        i = int(len(self.heap) - 1)
        while i > 0:
            p = (i - 1) // 2  # 親の場所を計算
            if self.heap[p] >= x:  # 親より小さかったら終了
                break
            self.heap[i] = self.heap[p]  # 判定場所に親の数値を設定
            i = p
        self.heap[i] = x  # 最後に挿入する数値を設定

    # 削除
    def pop(self):
        if not self.heap:
            return  # 空だったら終了
        x = self.heap[-1]  # 最後の値を持ってくる
        print(x)
        self.heap.pop(-1)  # 先頭の親を削除
        # print(self.heap)
        i = 0
        while i * 2 + 1 < int(len(self.heap)):
            c1 = i * 2 + 1
            c2 = i * 2 + 2
            # c2の長さがheapの長さのうちに入っていること、かつ、c2の値がc1の値より大きい場合
            if c2 < int(len(self.heap)) and self.heap[c2] > self.heap[c1]:
                # c1へc2の場所を設定。大きい値の方に行く
                c1 = c2
            if self.heap[c1] <= x:  # xが大きかったら親として設定する
                break
            self.heap[i] = self.heap[c1]
            i = c1

        self.heap[i] = x  # 最後に子に設定

    # 最大値の取得
    def top(self):
        return self.heap[0] if self.heap else -1


if __name__ == '__main__':
    heap = Heap()
    heap.push(5)
    heap.push(9)
    heap.push(2)
    heap.push(10)
    heap.push(8)
    heap.push(11)
    heap.push(1)

    print(heap.heap)

    print(heap.top())
    heap.pop()
    print(heap.heap)
