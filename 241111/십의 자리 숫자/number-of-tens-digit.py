l = list(input().split())
cnt= [0 for i in range(9)]
for i in range(len(l)-1):
    if len(l[i]) == 3:
        cnt[int(l[i][1])-1] += 1
    elif len(l[i]) == 2:
        cnt[int(l[i][0])-1] += 1
for i in range(9):
    print(f"{i+1} - {cnt[i]}")