##조건문 if ~ else

money = 1000

if money > 3800:
    print('택시를 타자!') ##파이썬 문법에서는 들여쓰기가 중요함. :다음에 오는 들여쓰기 여부에 따라 해당조건문에 해당되는지 여부가 달라진다.
elif money > 1200: ##elif는 여러개 사용가능
    print('버스를 차자!')
else:
    print('걸어가자')


print('그럼 뭘 타지?') ##들여쓰기를 맞게 해주지 않으면 상단의 조건문과 상관없이 동작함


##반복문 for

fruits = ['사과', '배', '감', '수박', '딸기']

for fruit in fruits: ##fruit라는 변수에 fruits의 값들을 담아서
    print(fruit) ##출력한다

##반복문 for 코드스피넷
##나이 출력하기
people = [ ##people이라는 list에
    {'name': 'bob', 'age': 20}, ##dictionary가 들어있음
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby', 'age': 57},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]

for person in people:
    name = person['name']
    age = person['age']
    if age > 20:
        print(name, ' : ', age)


##enumerate 요소의 순서를 적어주는 문
for i, person in enumerate(people):
    name = person['name']
    age = person['age']
    print(i,')', name, ' : ', age)

##enumerate 요소의 순서의 활용 break
for i, person in enumerate(people):
    name = person['name']
    age = person['age']
    if i > 5:
        break ##break문 활용 : 츨력값이 많을 때 일부만 출력하고자할때 활용가능
    print(i,')', name, ' : ', age)

