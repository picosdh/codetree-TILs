def max_n(s):
    n = 0
    total = 0
    while True:
        n += 1
        total += n
        if total > s:
            return n - 1

s = int(input())
result = max_n(s)
print(result)