##함수만들기:기본문자열 출력
def hello():
    print('안녕!')
    print('좋은날씨야!')

hello()


##함수만들기:사칙연산
def sum(a,b):
    print('더하기를 하셨네요!')
    return a+b

result = sum(1,2)
print(result)

def bus_rate(age):
    if age > 65:
        print('무료입니다.')
    elif age > 20:
        print('성인입니다.')
        return 1200
    else:
        print('청소년입니다.')
        return 750

my_rate = bus_rate(60)
print(my_rate)

##퀴즈
##주민등록번호를 입력받아 성별을 출력하는 함수 만들기

##내가푼 답
def gerder_chk(g_num):
    gerder = g_num.split('-')[1]
    if gerder[:1]=='1':
        print('남자입니다.')
    elif gerder[:1]=='2':
        print('여자입니다.')
    elif gerder[:1]=='3':
        print('2000년 이후 남자입니다.')
    elif gerder[:1]=='4':
        print('2000년 이후 여자입니다.')
    else:
        print('주민등록번호를 다시 확인해 주세요.')

gerder_chk('950302-2702813')

##강의 답
def check_gender(pin):
    num=pin.split('-')[1][:1]
    if int(num)%2==0:
        print('여성입니다.')
    else:
        print('남성입니다.')

check_gender('150101-1012345')
check_gender('150101-2012345')
check_gender('150101-4012345')