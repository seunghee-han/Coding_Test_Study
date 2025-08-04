#### sol1 ####

# def find_max_num(array):
#     for num in array:
#         is_max_num = True
#         for compare_num in array:
#             if num < compare_num:
#                 is_max_num=False
#         if is_max_num:
#             return num

#### sol2 ####
def find_max_num(array):
    max_num = array[0]
    for num in array:
        if max_num < num:
            max_num = num
    return max_num

print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))
