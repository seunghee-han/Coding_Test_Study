input = [4, 6, 2, 9, 1]
# 0은 이미 정렬되었다로 시작
# 1과 0 비교
# 2번째가 1번째와 0번째와 비교
# 출력되어야하는순서 1 -> 2,1 -> 3,2,1 -> ~

#얘는 정렬이 잘되어있으면 잘하면 O(N)이걸릴수도있음
def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        for j in range(i):
            if array[i-j] < array[i-j-1]:
                array[i - j], array[i - j-1] = array[i - j-1], array[i-j]
            else:
                break
    return array

insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [4, 5, 7, 7, 8] / 현재 풀이 값 = ",insertion_sort([5,8,4,7,7]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",insertion_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",insertion_sort([100,56,-3,32,44]))