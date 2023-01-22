## 리스트 : 0번째는 '사과', 1번째는 '수박', 2번째는 '포도', 3번째는 ....

a_list = ['사과', '배', '감']
print(a_list)

a_list2 = [2, '배', False, ['사과','감']]
print(a_list2[3][1])

a_list3 = [1,5,6,3,2]
a_list3.append(99) ## .append  배열추가
a_list3.append(100)
print(a_list3)

result = a_list3[-1] ## [-1]  마지막 값 출력 <<문자열에서도 사용가능
print(result)

result = a_list3[:3] ## [:3]  앞에서 3개 값만 잘라서 출력 <<문자열에서도 사용가능
print(result)

result = len(a_list3) ## len  길이구하기
print(result)

a_list3.sort() ## sort()  정렬(기본갑 오름차순)
print(a_list3)

a_list3.sort(reverse=True) ## sort(reverse=True)  정렬(내림차순)
print(a_list3)

result = (5 in a_list3) ## in  리스트 안에 있는 값 확인하기
print(result) ## 결과 True False로 표시

######################################################################################

## 딕셔너리 : key:value관계 >> 주민번호:이름 >> 000000-0000000:홍길동

a_dict = {'name':'bob', 'age':27}
## print(a_dict['name']) ## 결과  'name'의 값인 'bob'이 출력된다
result = a_dict['name']
print(result)

a_dict2 = {'name':'bob', 'age':27, 'friend':['영희','철수']} ## 리스트와 딕셔너리의 조합
result = a_dict2['friend'][1]
print(result)

a_dict2['height'] = 180 ## 딕셔너리 값 추가
print(a_dict2) ## 값이 추가된 결과를 볼 수 있음
print('height' in a_dict2) ## in  딕셔너리에 해당값이 포함되었는지 여부를 확인할 수 있음

######################################################################################

## 리스트와 딕셔너리 조합

people = [
    {'name':'bob', 'age':27},
    {'name':'john', 'age':30}
]
print(people[0]['name'])

## 코드스피넷 퀴즈
## smith의 science점수 출력
people2 = [
    {'name': 'bob', 'age': 20, 'score':{'math':90,'science':70}},
    {'name': 'carry', 'age': 38, 'score':{'math':40,'science':72}},
    {'name': 'smith', 'age': 28, 'score':{'math':80,'science':90}},
    {'name': 'john', 'age': 34, 'score':{'math':75,'science':100}}
]

print(people2[2]['score']['science'])



