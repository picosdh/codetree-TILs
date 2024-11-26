n, m = map(int, input().split())
l = [[0 for _ in range(m)]for _ in range(n)]
plus = 0
k = 0
for i in range(m):
    l[0][i] = 1 + plus
    plus += 1 + k
    k += 1
for i in range(1, n):
    for j in range(m):
        if j != m-1:
            l[i][j] = l[i-1][j+1] + 1
        else:
            l[i][j] = l[i-1][j] + m - i + 1
for i in range(n):
    print(*l[i], end=' ')
    print()