n, m = map(int, input().split())
l = list(map(int, input().split()))
l1 = list(map(int, input().split()))
res = 0
for i in range(len(l)):
    if len(l) - i + 1 >= len(l1) - res + 1:

        if l[i] == l1[res] and res == 0:
            res += 1
        else:
            if l[i] == l1[res]:
                res += 1
            else:
                res = 0
    else:
        break
if res == len(l1):
    print("Yes")
else:
    print("No")