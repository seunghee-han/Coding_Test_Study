def find_max_plus_or_multiply(array):
    plus_or_multiply_sum = 0  #대입 연산
    for num in array:               #N의 길이만큼 반복
        if num <=1 or plus_or_multiply_sum <= 1:  # 비교
            plus_or_multiply_sum += num  # 대입
        else:
            plus_or_multiply_sum *= num
    return plus_or_multiply_sum

# 최악인경우 O(N)
result = find_max_plus_or_multiply
print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))