def find_nth_number(N):
    count = 0
    num = 1
    
    while True:
        if num % 3 != 0 and num % 5 != 0:
            count += 1
            if count == N:
                return num
        num += 1

N = int(input())
result = find_nth_number(N)
print(result)