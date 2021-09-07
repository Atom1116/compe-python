
n = int(input())
S = input()

for i in range(n):
    if S[i] == '1':
        print('Takahashi' if i%2 == 0 else "Aoki")
        break