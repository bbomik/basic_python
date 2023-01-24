##tuple : 순서가 있는 자료형이지만 불변형이다.(list와 똑같이 생겼으나 불변형)

a=('사과','감','배')

##a[2] = '수박' <<tuple은 불변형이어서 수정하려고 할 경우 에러가 발생됨

print(a)

##tuple의 주활용 예시
## people = [{'name':'bob','age':27},{'name':'john','age':30}]  <<이와 같은 list를
## people = [('bob',27),('john',30)]   <<이와 같은 tuple형태로 활용하여 사용한다.

##set : 집합
a = [1,2,3,4,3,2,3,4,5,8,7,1]

a_set = set(a) ##중복되는 것을 제거함
print(a_set)

aa = ['사과','감','배','수박','딸기']
bb = ['배','사과','포도','참외','수박']

aa_set = set(aa)
bb_set = set(bb)
print(aa_set & bb_set) ##교집합 &
print(aa_set | bb_set) ##합집합 |

##코드스니펫 : AB수업문제
##A수업에서 B수업과 중복되는 것을 뺀 나머지를 출력(차집합 구하기)
student_a = ['물리2','국어','수학1','음악','화학1','화학2','체육']
student_b = ['물리1','수학1','미술','화학2','체육']

a_stud_set = set(student_a)
b_stud_set = set(student_b)

print(a_stud_set - b_stud_set) ##차집합 -
print(a_stud_set ^ b_stud_set) ##여집합 ^
