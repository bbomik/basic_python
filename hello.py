print('hello python')


##사칙연산
a=11 ##변수선언 숫자, 문자, 소수점, 참/거짓 모두 선언가능
b=7

print(a+b)
print(a*b)
print(a/b)

## 제곱 구하기
print(a**b)

## 나머지 구하기
print(a%b)

## 참true 거짓false 구하기
aa=(3==2) ##같다는 =이 아닌 == 사용(=은 선언을 사용할때 사용)
print(aa)

## 문자열 다루기
first_name = 'bomi'  ## 문자열을 사용시 ' 나 " 를 사용해도 상관없다. 하지만 한쪽을 '사용시 끝나는 쪽도 동일하게 '을 사용해주어야 한다.
last_name = "kim"
print(first_name + last_name)

bb='a' ## a의 값 11을 가르키는 것이 아닌 문자열 a을 갖는다.
print(bb)
## print(a+bb) ## 숫자열과 문자열은 함께 계산할 수 없다. (에러남)

## 형변환
x = '2'
y = str(2)
print(x+y)

## len : 문자열 길이를 구하는 함수
text = 'abcdefghijk'
result = len(text)
print(result)

## 문자열 자르기 [ : ]
result = text[3:] ## 결과 defghijk : 3번째 이후부터 출력
print(result)

result = text[:3] ## 결과 abc : 3번째까지 출력
print(result)

result = text[3:7] ## 결과 3번째 부터 7번째 까지만 출력
print(result)

result = text[:] ## 결과 text값 복사
print(result)

## 문자열 자르기
myemail = 'abc@naver.com'
result_m = myemail.split('@')[1].split('.')[0] ## 결과 ['abc', 'naver.com'] 앞에서부터 0번째, 1번째 임
print(result_m)

## 문자열 활용 퀴즈
## spartar에서 앞 3글자 spa만 출력하기
quiz = 'spartar'
result_q = quiz[:3]
print(result_q)

## 02-123-4567에서 지역번호를 출력하기
quiz2 = '02-123-4567'
result_q2 = quiz2.split('-')[0]
print(result_q2)