n, m = map(int, input().split())
l = list(map(int, input().split()))
l1 = list(map(int, input().split()))
d = dict()
for i in range(n):
    d[l[i]] = i
cnt = d[l[0]]
for i in range(m):
    if d[l[i]] != cnt+1:
        print('No')
        exit()
    else:
        cnt += 1
print('Yes')