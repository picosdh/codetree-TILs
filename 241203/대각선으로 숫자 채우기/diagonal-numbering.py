n, m = tuple(map(int, input().split()))
arr = [[0 for _ in range(m)]for _ in range(n)]
cnt = 1
for i in range(m):
    row = 0
    col = i
    while 0 <= col and row < n:
        arr[row][col] = cnt
        row += 1
        col -= 1
        cnt += 1
for i in range(1, n):
    row = i
    col = m - 1
    while 0 <= col and row < n:
        arr[row][col] = cnt
        row += 1
        col -= 1
        cnt += 1
for i in range(n):
    for j in range(m):
        print(arr[i][j], end = ' ')
    print()