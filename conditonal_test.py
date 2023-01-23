##조건문 연습문제

num_list = [1, 2, 3, 6, 3, 2, 4, 5, 80, 2, 4]

##1. 짝수만 출력하는 함수 만들기

for num in num_list:
    if num%2==0:
        print(num)

print('::::::::::::::::::::::')
##2. 짝수의 개수 출력하기

cnt = 0
for num in num_list:
    if num%2==0:
        cnt += 1  ##동일 cnt = cnt+1
print(cnt)

print('::::::::::::::::::::::')
##3. 모든숫자 더하기

sum=0
for num in num_list:
    sum += num  ##동일 sum = sum + num
print(sum)

print('::::::::::::::::::::::')
##4. 자연수 중 가장 큰 숫자 구하기

max=0
for num in num_list:
    if max < num:
        max = num
print(max)

