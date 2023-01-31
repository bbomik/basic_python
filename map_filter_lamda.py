##map
##map을 이용해 age가 20보다 크면 '성인', 작으면 '청소년'으로 바꾸는 예제
import lamda as lamda

people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby', 'age': 57},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]
'''
def check_adult(person):
    ##기본형
    if person['age'] > 20:
        return '성인'
    else:
        return '청소년'

result = map(check_adult,people) ##people을 하나하나 돌면서 check_adult에다가 넣어라
print(list(result)) ##결과값을 다시 list로 묶음
'''
##결과 >>   ['청소년', '성인', '청소년', '청소년', '성인', '성인', '성인', '성인']

def chexk_adult2(person2):
    ##응용형
    return ('성인' if person2['age'] > 20 else '청소년')

result2 = map(lamda person2: ('성인' if person2['age'] > 20 else '청소년'), people)
