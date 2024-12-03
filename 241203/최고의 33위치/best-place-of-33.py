def go(l):
    cnt = 0
    for i in range(3):
        for j in range(3):
            cnt += l[i][j]
    return cnt
n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
maxV = 0
for i in range(n-2):
    for j in range(n-2):
        nl = [[0 for _ in range(3)]for _ in range(3)] 
        for k in range(3):
            for o in range(3):
                nl[k][o] = l[i+k][j+o]
        if maxV <= go(nl):
            maxV = go(nl)
print(maxV)