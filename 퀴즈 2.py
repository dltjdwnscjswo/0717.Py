#구구단 함수를 작성하시오. 매개변수 입력에 따라 해당 구구단을 화면하면 출력하는 함수를 작성하시오.
# a = int(input("출력하려는 구구단 수를 넣어주세요."))
#
# for i in range(1,10) :
#     print(a,"X",i,"=",a*i)

def print_mel_table(x) :
    print(x, "단을 시작합니다.")
    for i in range (1,10) :
        print(x,"X",i,"=",x*i)


k = int(input("1부터 9까지의 수 중에서 입력하세요: "))
print_mel_table(k)