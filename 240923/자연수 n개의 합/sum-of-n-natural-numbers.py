n = int(input())
ans = 0
def go(n):
    return (n*(n+1))*1/2
for i in range(int(n**(0.5))-1, 141421356):
    if go(i) <= n:
        ans = i
    else:
        break
print(ans)