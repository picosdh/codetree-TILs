def can_make_k(values, k, m):
    count = 0
    for value in values:
        count += value // k
    return count >= m

def max_k(n, m, values):
    left, right = 1, max(values)
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        if can_make_k(values, mid, m):
            result = mid  # mid는 가능하므로 결과 업데이트
            left = mid + 1  # 더 큰 값을 찾기 위해 범위 조정
        else:
            right = mid - 1  # 가능한 값이 아니므로 범위 축소
            
    return result

# 입력 처리
n, m = map(int, input().split())
values = [int(input()) for _ in range(n)]

# 결과 출력
print(max_k(n, m, values))