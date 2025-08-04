#### sol1 ####

def is_number_exist(number, array):
    for element in array: #array의 길이만큼 연산 실행
        if number == element: # 비교 연산 1번 실행
            return True        #시간복잡도는 N만큼 걸림
    return False

# 빅오-> 최악인 경우
# 빅오메가 -> 최선의 경우

# #### sol2 ####

# def is_number_exist(number, array):
#     if number in array:
#         return True
#     else:
#         return False


result = is_number_exist
print("정답 = True 현재 풀이 값 =", result(3, [3,5,6,1,2,4]))  #운이 좋은경우 시간복잡도가 1
# -> 최선의 경우에는 1만큼의 연산 필요

print("정답 = True 현재 풀이 값 =", result(4, [3,5,6,1,2,4]))  #운이 좋지 않은 경우
# -> 최악의 경우에는 시간복잡도가 N

print("정답 = Flase 현재 풀이 값 =", result(7, [6,6,6]))
print("정답 = True 현재 풀이 값 =", result(2, [6,9,2,7,1888]))
