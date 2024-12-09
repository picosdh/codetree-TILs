def count_happy_sequences(n, m, grid):
    def is_happy(sequence, m):
        count = 1
        for i in range(1, len(sequence)):
            if sequence[i] == sequence[i - 1]:
                count += 1
                if count >= m:
                    return True
            else:
                count = 1
        return False
    happy_count = 0
    for row in grid:
        if is_happy(row, m):
            happy_count += 1
    for col in range(n):
        column = [grid[row][col] for row in range(n)]
        if is_happy(column, m):
            happy_count += 1

    return happy_count
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
print(count_happy_sequences(n, m, grid))
