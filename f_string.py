##f-string

scores = [
    {'name':'영수','score':70},
    {'name':'영희','score':65},
    {'name':'기찬','score':75},
    {'name':'희수','score':23},
    {'name':'서경','score':99},
    {'name':'미주','score':100},
    {'name':'병태','score':32}
]

for s in scores:
    name = s['name']
    score = s['score']
    ##print(name+'의 점수는 '+str(score)+'점 입니다.')  ##string 형변환을 어디에서든 사용해 숫자열을 문자열로 바꾸어 주어야 한다1
    print(f'{name}의 점수는 {score}점입니다.') ##f_string을 사용시 훨씬 간편하게 문자열을 사용할 수 있다.

##혹은
'''
for s in scores:
    name = s['name']
    score = str(s['score'])  ##string 형변환을 어디에서든 사용해 숫자열을 문자열로 바꾸어 주어야 한다2
    print(name+'의 점수는 '+score+'점 입니다.'
'''