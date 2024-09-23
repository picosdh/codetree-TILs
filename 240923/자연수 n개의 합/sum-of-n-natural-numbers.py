n = int(input())
ans = 0
def go(n):
    return (n*(n+1))*1/2
for i in range(n**(0.5), 141421356):
    if go(i) <= n:
        ans = i
    else:
        break
print(ans)