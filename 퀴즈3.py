#문자 메세지 길이 판별 함수.
# 문자메세지 길이에 따라 문자 요금이 결정되는 프로그램을 작성하시오. 메세지의 길이가 20이하면 50원이며,
# 20을 초과하면 100원이다. 사용자로부터 문자메세지를 입력 받아서 문자 요금을 반환하는 코드를 작성하시오.

def g(a):
    b = len(a)
    if 20 >= b :
        c = 50
    if 20 < b :
        c = 100

    result = c
    return result


m = input("문자 메세지를 보내주세요.")

print(g(m))

# 1. 문자 메세지의 길이 파악

# 5. 함수로 만들어서 요금을 반환
# def find_len(x):
#     result = 0
#     if len(x) <= 20 :
#         result = 50
#     # 3. 문자의 길이 > 20, 100원
#     if len(x) > 20 :
#         result = 100
#     return result
#     text = input("문자메세지를 입력해주세요. : ")
#     var = find_len(text)
#     print(var)