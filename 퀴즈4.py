# 학점 변환기 함수. 점수 구간에 해당하는 학점이 아래와 같이 정의 되어있다
# score를 입력 받아 학점으로 환산하여 반환하는 함수를 작성하여라

def g(a):
    c = ""
    if 81 <= a <= 100 :
        c = "A"
    elif a<=80 and a>=61 :
        c = "B"
    elif a<=60 and a>=41 :
        c = "C"
    elif a<=40 and a>=21 :
        c = "D"
    elif a<=20 and a>=0 :
        c = "E"
    else:
        c= "올바른 점수를 입력하세요"
    return c


d = int(input("점수를 입력해주세요. : "))

print(g(d))