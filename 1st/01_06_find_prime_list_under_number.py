# 소수 나열하기
input = 20

#### sol1 ####
# def find_prime_list_under_number(number):
#     prime_list=[]
#     for i in range(2,number+1):
#         for n in range(2,i):
#             if n % i ==0:
#                 result.append(n)
#
#     return prime_list



#### sol2 ####
def find_prime_list_under_number(number):
    prime_list = []

    for n in range(2, number + 1):
        for i in prime_list:
            if i * i <= n and n % i == 0:
                break
        else:
            prime_list.append(n)

    return prime_list

result = find_prime_list_under_number(input)
print(result)
