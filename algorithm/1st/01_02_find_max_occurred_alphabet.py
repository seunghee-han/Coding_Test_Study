#### sol1 ####

# def find_max_occurred_alphabet(string):
#     alphabet=['a','b','c','d','e','f','g','h','i','j','k','l',
#               'm','n','o','p','q','r','s','t','u','v','w','x','y','z']
#
#     max_alpha = alphabet[0]
#     max_occ = 0
#     for alp in alphabet:
#         occ=0
#         for char in string:
#             if alp == char:
#                 occ += 1
#         if occ > max_occ:
#             max_alpha = alp
#             max_occ = occ
#     return max_alpha



#### sol2 ####

# isalpha()
# ord a -> 97
# chr 97 -> a

def find_max_occurred_alphabet(string):
    alphabet_num_array = [0]*26    # 빈도수 넣을 배열
    for char in string:
        if not char.isalpha():     # 알파벳인지 검사
            continue
        arr_index = ord(char)-ord('a')  # 문자를 인덱스로 치환
        alphabet_num_array[arr_index]+=1    # 빈도수 배열에 해당 값 넣기
    max_occurrence  = 0 #최대 빈도수
    max_alphabet_index  = 0 #최대 빈도수의 인덱스값
    for index in range(len(alphabet_num_array)):
        alpha_occ = alphabet_num_array[index]
        if max_occurrence < alpha_occ:
            max_occurrence = alpha_occ  
            max_alphabet_index = index   
    return chr(max_alphabet_index+ord('a')) # 인덱스를 문자로 치환

result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))

