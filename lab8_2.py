import numpy as num

N = int(input("Введіть число N: "))
masiv = num.zeros((N, N), dtype=int)
x = 0
for a in range(N):
    for b in range(N):
        masiv[a][b] = pow(N, 2) - x
        x = x + 1
print(masiv)