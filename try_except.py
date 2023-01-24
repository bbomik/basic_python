##try-except 서버에서 에러를 잡을 때 주로 사용
##예외를 너무 많이 허용하게되면 데이터가 오염될 수 있음

people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby'},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]

for person in people:
    try:
        if person["age"] > 20: ##파이썬은 ' , " 구분없이 사용 가능
            print(person["name"])
    except:
        print(person["name"],'에러입니다.')