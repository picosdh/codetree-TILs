import sys
sys.setrecursionlimit(10**5)
def go(maxV, l):
    maxi = 0
    for i in range(len(l)):
        if l[i] >= maxV:
            if l[i] == maxV:
                pass
            else:
                maxi = i+1
                maxV = l[i]
    return maxi
n = int(input())
l = list(map(int, input().split()))
maxV = float("-INF")
a = 0
res = []

while True:
    res.append(go(maxV, l))
    a = go(maxV, l)
    l = l[0:go(maxV, l)-1]
    if a == 1:
        break
print(*res,  end=' ')
        