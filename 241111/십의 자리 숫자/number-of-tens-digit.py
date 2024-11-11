l = list(input().split())
cnt= [0 for i in range(10)]
for i in range(len(l)):
    if l[i] == '0':
        break
    else:
        if len(l[i]) == 2:
            cnt[int(l[i][0])] += 1
for i in range(1,10):
    print(f"{i} - {cnt[i]}")