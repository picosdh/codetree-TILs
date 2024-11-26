n, m = map(int, input().split())
l = [[0 for _ in range(m)]for _ in range(n)]
plus = 0
lp = 0
for i in range(m):
    if (1 + plus) - lp <= n:
        l[0][i] = 1 + plus
        lp = 1 + plus
        plus += 1 + i
    else:
        l[0][i] = lp + n
        lp += n
for i in range(1, n):
    for j in range(m):
        if j != m-1:
            l[i][j] = l[i-1][j+1] + 1
        elif i + 1 == n and j + 1 == m:
            l[i][j] = l[i][j-1] + 1
        else:
            l[i][j] = l[i-1][j] + abs(m - n) + i
for i in range(n):
    print(*l[i], end=' ')
    print()