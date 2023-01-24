## 파이썬은 굉장히 직관적이기 때문에 간단하게 줄여서 코딩도 가능하다. 한줄 코딩하는 예제를 알아보자

##예제1 : if문
##기본형
num =3

if num%2 ==0:
    result ='짝수'
else:
    result ='홀수'

print(f'{num}은 {result}입니다.')

##응용형
num = 3

result = ('짝수' if num%2 == 0 else '홀수') ##직관적으로 한줄 코딩

print(f'{num}은 {result}입니다.')

##두 결과는 동일


##예제2 : for문
##기본형
