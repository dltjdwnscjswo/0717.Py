# 판매가가 저장된 리스트가 있을 때 부가세가 포함된 가격을 리스트로 반환하는 함수를 작성하시오.
# numbers = [100,200,300]
# print(VAT(numbers))
# 출력 결과
# [110,220,300]
def c(numbers) :
    list = []
    for a in numbers :
        VAT = int(a * 1.1)
        list.append(VAT)
    return list

num = [100,200,300]
print(c(num))