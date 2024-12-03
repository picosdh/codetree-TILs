def go(n, l):
    cnt = 0
    for i in range(n):
        for j in range(n):
            cnt += l[i, j]
    return cnt
n = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
maxV = 0
for i in range(n-2):
    for j in range(n-2):
        if maxV <= def(l[i:][j:]):
            maxV = def(l[i:][j:])
print(maxV)