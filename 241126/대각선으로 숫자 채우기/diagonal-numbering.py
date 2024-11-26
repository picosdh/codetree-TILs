n, m = map(int, input().split())
l = [[0 for _ in range(n)]for _ in range(m)]
plus = 0
k = 0
for i in range(n):
    l[0][i] = 1 + plus
    plus += 1 + k
    k += 1
for i in range(1, m):
    for j in range(n):
        if j != n-1:
            l[i][j] = l[i-1][j+1] + 1
        else:
            l[i][j] = l[i-1][j] + n - i + 1
for i in range(m):
    print(*l[i], end=' ')
    print()