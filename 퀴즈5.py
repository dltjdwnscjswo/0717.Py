#리스트 변수의 평균 값을 구하는 함수를 작성하시오. 리스트의 길이는 매번 달라질 수 있음에 유의하고,
# sum() 함수를 사용 할수 없다.

def my_sum (list):
    b = 0
    for a in list:
        b = b+a
    c = len(list)
    x = b/c
    return x


list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(my_sum(list3))
