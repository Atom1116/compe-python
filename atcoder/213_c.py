
# H,W,N = map(int, input().split())

# data = [list(map(int, input().split())) for _ in range(N)]

# ans_list = [[[0]*N]*N]

# for i in range(N):
    

## 今回の問題は、「座標圧縮」と呼ばれる典型アルゴリズムの実装を要求している

# 座標圧縮が目標とすることは、2 4 7という数列に対して、小さい方から0,1,2と番号を振りなおす作業のことである。
# よって2 4 7に対して「座標圧縮をする」と0 1 2と変換される。
# 4 1 9であれば1 0 2になるし、4 3 3 1なら2 1 1 0となる。
# なんとなく何をしているかは分かると思うが、活用例が思いつかないと何のための操作か分からないかもしれない。

H,W,N=map(int,input().split())
X,Y=[],[]

for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

# 座標圧縮
# もともともっとも上にあった数のカードと二番目のカードの位置は入れ替わらないから座標圧縮で求められる
# Aたちの代償関係を保ったまま値を小さくする
Xdict = {x:i+1 for i, x in enumerate(sorted(list(set(X))))}
Ydict = {y:i+1 for i, y in enumerate(sorted(list(set(Y))))}

# print(Xdict)
# print(Ydict)

for i in range(N):
    print(Xdict[X[i]], Ydict[Y[i]])