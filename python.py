# 문자, 숫자, 불리안 자료형
print('hello world')
print("안녕하세요") 
print(10)
print(True)
print(False)

# 변수 선언
envelope1 = 10000
envelope2 = 20000
envelope3 = '파이팅'
print(envelope1)
print(envelope2)
print(envelope3)

# 변수 이름
name = '1'
Name = '분'
NAME = '파이썬'
print(name)
print(Name)
print(NAME)

# 형 변환 정수, 실수, 문자
int('2') 
float('1.5')
str(2)
num = int(float('2.5'))
print(num)

# 산술, 비교, 논리, 멤버 연산자
print(5+2) #더하기 
print(5-2) #빼기
print(5*2) #곱하기
print(5/2) #나누기
print(5%2) #나머지
print(5//2) #몫
print(5**2) #거듭 제곱
print(5>2) #크다
print(5>=2) #크거나 같다
print(5<2) #작다
print(5<=2) #작거나 같다
print(5==2) #같다
print(5!=2) #같지 않다
print(3<5 and 7<5) #둘다 참이면 Ture
print(3<5 or 7<5) #하나라도 참이면 Ture
print(not 3<5) #반전
print('c' in 'cat')
print('c' not in 'cat')

#불리안 형 변환 (참이면 Ture 거짓이면 False, 값이 있으면 Ture 없으면 False)
a = 'hello'
b = '     '
c = ''
print(bool(a))
print(bool(b))
print(bool(c))

d = 1
e = -2
f = 0

print(bool(d))
print(bool(e))
print(bool(f))

print(bool(None))

#주석
print('신랑 신부 입장')
# 걷기 시작하면
print('큰 박수 부탁드립니다')

print('신랑 신부 입장')
'''걷기 시작하고
 잠시 후에'''
print('큰 박수 부탁드립니다')

#인덱스
lang = 'PYTHON'
print(lang[0]) 
print(lang[5]) 
print(lang[-6]) 
print(lang[-1]) 
print(lang[1:6]) #인덱스 1 부터 6 직전까지
print(lang[1:]) #인덱스 1 부터 끝까지
print(lang[:4]) #처음부터 인덱스 4 직전까지
print(lang[:]) #처음부터 끝까지

snack = '꿀꽈배기'
two = '2개'
juseyo = snack + two
juseyo += '주세요'
print(juseyo)

num = 3
# num = num + 2 이걸 간소화 
# num += 2
# num -= 2
# num *= 2
# num /= 2
print(num)

snack = '''꿀꽈배기는
너무
맛있어요'''
print(len(snack))

#메소드
letter = 'how are YOU?'
print(letter.lower()) #모든 문자를 소문자로
print(letter.upper()) #모든 문자를 대문자로
print(letter.capitalize()) #첫 글자만 대문자로
print(letter.title()) #각 단어들의 첫 글자만 대문자
print(letter.swapcase()) #대소문자를 뒤바꿈
print(letter.split()) #문자열을 나눔
print(letter.count('how')) #몇번 쓰였는지
s = '나도고등학교'
print(s.startswith('나도')) #'?'로 시작하는지
print(s.endswith('초등학교')) #'?'로 끝나는지
s = '...나도고등학교...'
print(s.strip('.')) #앞뒤로 불필요한 부분을 제거
s = '나도고등학교'
print(s.replace('고등학교','고교')) #'?' 를 '2?'로 바꿈
print(s.find('학교'))  # '?'가 어디있는지 알려줌
print(s.center(10,'-')) #다른 문자들 사이에 가운데로

#문자열 출력
python = '파이썬'
java = '자바'
print(python+' '+java)#둘다 출력
print(python,java)#또는
print('개발 언어에는 '+python+','+java+' 등이 있어요')
print('개발 언어에는',python,',',java,'등이 있어요')

#문자열 포멧
print('개발 언어에는 {},{} 등이 있어요'.format(python,java))
print('개발 언어에는 {0},{1} 등이 있어요'.format(python,java))
print(f'개발 언어에는 {python},{java} 등이 있어요')

#탈출 문자 *큰 따옴표는 \'', 작은 따옴표는 \', 역슬래시는 \\, 줄바꿈은 \n
print('하지만\'나만 당할 순없지\'라는 생각에\"엄청쉽지\"라고 했다.')
print('C:\\Users\\Nadocoding')
snack = '꿀꽈배기는\n너무\n맛있어요'
print(snack)

#리스트
my_list = ['오예스','몽쉘','초코파이','초코파이','초코파이'] #중복 허용
your_list = [1,2,3.14,True,False,'아무거나']
empty_lsit = []
print(my_list[0])
print(my_list[0:2])
print('몽쉘'in my_list)
print(len(my_list))
my_list[1] = '몽쉘카카오'
print(my_list)
my_list.append('빅파이')
print(my_list)
my_list.remove('오예스')
print(my_list)
my_list.extend(your_list)
print(my_list)
#insert() 원하는 위치에 값 추가
#pop() 원하는 위치(또는 마지막)의 값 삭제
#clear() 모든 값 삭제
#sort() 값 순서대로 정렬
#reverse() 순서 뒤집기
#copy() 리스트 복사
#count() 어떤 값이 몇 개 있는지
#index() 어떤 값이 어디에 있는지

#튜플 패킹
my_tuple = ('오예스','몽쉘','초코파이','초코파이') #중복 허용
your_tuple = (1,2,3.14,True,False,'아무거나')
print(my_tuple[0])
print(my_tuple[0:2])
print('몽쉘'in my_tuple)
print(len(my_tuple))
#conut() 어떤 값이 몇 개 있는지
#index() 어떤 값이 어디에 있는지
#튜플 언패킹
numbers = (1,2,3,4,5,6,7,8,9,10)
(one,two,*others) = numbers #*은 리스트의 형태로 저장
(*others,nine,ten) = numbers
(one,*others,ten) = numbers

#세트 (중복X,순서X)
A = {'돈가스','보쌈','제육덮밥'}
B = {'짬뽕','초밥','제육덮밥'}
print(A.intersection(B)) #교집합
print(A.union(B)) #합집합
print(A.difference(B)) #차집합
my_set = {'돈가스','보쌈','제육덮밥'}
my_set.add('닭갈비') #값 추가
print(my_set)
my_set.remove('제육덮밥') #값 지우기
print(my_set)
my_set.clear() #모든 값 지우기
print(my_set)
del my_set #완전 삭제
#copy() 값 복사
#discard() 값 삭제(해당 값이 없어도 에러 발생X)
#isdisjoint() 다른 세트의 부분집합인지 여부
#issuperset() 다른 세트의 상위집합인지 여부
#update() 다른 세트의 값들을 더함

#딕셔너리 (key,value) 예)사전
person = {
    '이름':'나귀욤',
    '나이':7,
    '키':120,
    '몸무게':23
    }
print(person['이름'])
print(person['나이'])
print(person.get('별명'))
person['최종학력'] = '유치원' #새로 추가
person['키'] = 130 #수정
person.update({'키':130,'몸무게':26}) #여러 값을 수정
person.pop('몸무게') #값을 제거
person.clear() #모든 값을 제거
print(person.keys())
print(person.values())
print(person.items())
#fromkeys() 제공된 keys 를 통해 새로운 딕셔너리 생성 및 변환
#popitem() 마지막으로 추가된 데이터 삭제
#setdefault key 에 해당하는 value 반환, key 가 없다면 새로 만들고 default value 설정 및 반환

#총 정리          리스트         튜플           세트          딕셔너리
'''선언      lst = []          t = ()          s = {}     d = {key:val}
순서 보장           O            O               X               O
중복허용            O            O               X               X (key)
    접근        lst[idx]       t{idx}            X            d[key], d.get(key)
    수정            O            X               X            0 (value)
    추가         append()        X             add()         d[key] = val
                 insert()                     update()       update()
                 extend()    
    삭제         remvoe()        X            remove()        pop()
                  pop()                       discard()      popitem()
                  clear()                      pop()         clear()
                                               clear()'''
#여러 값들을 순서대로 관리해야 할때는 리스트
#값이 바뀔 일이 없거나, 바뀌면 안되면 튜플
#값의 존재 여부가 중요하거나 중복이 안될때는 세트
#key를 통해 효율적으로 데이터를 관리 하고싶을땐 딕셔너리

#튜플을 수정하는 방법
my_tuple = ('오예스','몽쉘')
my_list = list(my_tuple)
my_list.append('초코파이')
my_tuple = tuple(my_list)

#리스트의 중복을 제거하는 방법
my_list = ['오예스','몽쉘','초코파이','초코파이','초코파이']
my_set = set(my_list)
my_list = list(my_set) #세트는 순서가 보장되지 않기 때문에 순서가 중요하지 않은 곳에만 쓰기
my_list = ['오예스','몽쉘','초코파이','초코파이','초코파이']
my_dic = dict.fromkeys(my_list) #딕셔너리는 순서를 보장
print(my_dic)
my_list = list(my_dic)
print(my_list)

#if 만약 ~ 라면
today = '일요일'
if today == '일요일':
    print('게임 한 판')
print('공부 시작')
today = '화요일'
if today == '일요일':
    print('게임 한 판')
print('공부 시작')
today = '일요일'
if today == '일요일':
    print('게임 한 판')
else:
    print('폰 5분만')
print('공부 시작')
today = '화요일'
if today == '일요일':
    print('게임 한 판')
else:
    print('폰 5분만')
print('공부 시작')
#if(만약 ~ 라면), else(그렇지 않다면)

#elif 는 if 와 else 사이에 얼마든지 추가 가능
if today == '일요일':
    print('게임 한 판')
elif today == '토요일':
    print('폰 5분만')
else:
    print("물 한 잔")
print('공부 시작')

#if 중첩
yellow_card = 0
foul = False 
if foul:
    yellow_card+=1
    if yellow_card == 2:
        print('경고 누적 퇴장')
    else:
        print('휴..조심해야지')
else:
    print('주의')

#for 반복문
for x in range(10):
    print('팔 벌려 뛰기 해') 
for x in range(10):
    print(f'팔 벌려 뛰기 {x}회')
#range(start,stop,step) start 이상 stop 미만 step 만큼 증가
for x in range(1,10,2):
    print(x) 
my_list = [1,2,3]
for x in my_list:
    print(x)
my_tuple = (1,2,3)
for x in my_tuple:
    print(x)
person = {'이름':'나귀욤','나이':7,'키':120,'몸무게':23}
for v in person.values():
    print(v)
person = {'이름':'나귀욤','나이':7,'키':120,'몸무게':23}
for k in person.keys():
    print(k)
person = {'이름':'나귀욤','나이':7,'키':120,'몸무게':23}
for k,v in person.items():
    print(k,v)
fruit = 'apple'
for x in fruit:
    print(x)

#while (~하는 동안)
max = 25 #최대 허용 무게
weight = 0 #현재 캐리어 무게
item = 3 #각 짐의 무게

while weight + item <=max: #캐리어에 짐을 더 넣어도 되는지 확인
    weight += item
    print('짐을 추가합니다')
print(f'총 무게는 {weight}입니다')

#break
drama = ['시즌1','시즌2','시즌3','시즌4','시즌5']
for x in drama:
    if x == '시즌3':
        print('재미 없대, 그만 보자')
        break
    print(f'{x}시청')

#continue
['시즌1','시즌2','시즌3','시즌4','시즌5']
for x in drama:
    if x == '시즌3':
        print('재미 없대, 건너뛰자')
        continue
    print(f'{x}시청')

#들여쓰기 indent
'''
if 조건문:
for 반복문:
while 반복문:
def 함수:
try 예외:
class 클래스:
스페이스 4칸
'''

#List Comprechension
products = ['JOA-2020','JOA-2021','SIRO-2021','SIRO-2022']
recall = [] #리콜 대상 제품 리스트
for p in products:
    if p.startswith('SIRO'): #제품명이 SIRO로 시작하는가
        recall.append(p)
print(recall)
#간략화
recall = [p for p in products if p.startswith('SIRO')]
print(recall)

my_list = [1,2,3,4,5]
new_list = [x for x in my_list if x>3]
"""
(1) my_list 에서
(2) 3보다 큰 값들만
(3) 그대로 사용해서
(4) 새로운 리스트로 만들어 줘
"""

#모든 모델명 뒤에 SE (special Edition)을 붙여줘
prod_se = [p+'SE' for p in products]
print(prod_se)
#모든 모델명을 소문자로 바꿔줘
prod_lower = [p.lower() for p in products]
print(prod_lower)
#22년 제품만 뽑는데 뒤에 (최신형) 이라는 글자를 붙여줘
prod_new = [p+'(최신형)' for p in products if p.endswith('2022')]
print(prod_new)

#함수
def show_price(customer):
    print(f'사랑하는 {customer} 고객님')
    print('감성 커트 가격은 15000원 입니다')

customer1 = '나장발'
show_price(customer1)

customer2 = '나수염'
show_price(customer2)

def get_price(is_vip=False,is_birthday=False,is_membership=False,card=False,review=False,first_time=False):
    if is_vip == True:
        return 10000
    elif is_birthday == True:
        return 10000
    else:
        return 15000

price = get_price(True)
print(f'커트 가격은 {price} 원입니다')
price = get_price(review=True,is_birthday=True)
print({price})

def visit(today,*customers):
    print(today)
    for customer in customers:
        print(customer)

visit('2022년 6월 10일','나장발')

def secret():
    message = '이건 나만의 비밀'
    print(message)

message = '나는야 전역 변수'
print(message)

def no_secret():
    global message
    message = '오 진짜 전역 변수'

no_secret()
print(message)
'''
name = input('예약자분 성함이 어떻게 되나요?')
print(name)
num = int(input('총 몇 분이세요?'))
if num>4:
    print('죄송하지만 저희 식당은 최대 4분 까지만 예약 가능합니다')
print(num)
'''
f = open('list.txt','w',encoding='utf8') #쓰기 모드로 파일 열기
f.write('김xx\n')
f.write('정xx\n')
f.write('허xx\n')
f.close()

f = open('list.txt','r',encoding='utf8') #읽기 모드로 파일 열기
contents = f.read()
print(contents)
f.close()

f = open('list.txt','r',encoding='utf8') #한줄씩 읽기
for line in f:
    print(line, end='')
f.close()

#with

with open('list.txt','w',encoding='utf8')as f:
    f.write('김xx\n')
    f.write('정xx\n')
    f.write('허xx\n')

with open('list.txt','r',encoding='utf8')as f:
    contents = f.read()
    print(contents)

#class
name = '까망이'
resolution = 'FHD'
price = 200000
color = 'black'
'''
class BlackBox:
    pass

b1 = BlackBox()
b1.name = '까망이'
print(b1.name)
print(isinstance(b1,BlackBox))

b2 = BlackBox()
print(b2.name)
'''
class BlackBox():
    def __init__(self,name,price):
        self.name = name #멤버 변수
        self.price = price #멤버 변수
class VideoMaker:
    def make(self):
        print('추억용 여행 영상 제작')
class MailSender:
    def send(self):
        print('메일 발송')

class TravelBlackBox(BlackBox,VideoMaker,MailSender):
    def __init__(self,name,price,sd):
        super().__init__(name,price)
        self.sd = sd

    def set_travel_mode(self,min):
        print(f'{self.name} {min} 분 동안 여행 모드 ON')



b1 = TravelBlackBox('까망이',200000,64)
b1.make()
b1.send()
b2 = TravelBlackBox('하양이',100000,64)
b2.set_travel_mode(20)
print(b2.name,b2.price)

class AdvancedTravelBlackBox(TravelBlackBox):
    def set_travel_mode(self,min):
        print(str(min)+'분 동안 여행 모드 ON')
        self.make()
        self.send()
        
b1 = TravelBlackBox('까망이',200000,64)
b1.set_travel_mode(20)
b2 = AdvancedTravelBlackBox('하양이',100000,64)
b2.set_travel_mode(15)
'''
#pass
class BlackBox:
    def __init__(self):
        pass
    def record(self):
        pass
    def stop(self):
        pass
    def format(self):
        pass
for i in range(10):
    pass
while True:
    pass
if 3<5:
    pass
def my_func():
    pass 
'''

#예외 처리와 에러 (구글 참고 python exceptions)
num1 = 3
num2 = '0'
try:
    result = num1/num2
    print(f'연산 결과는 {result}입니다')
except ZeroDivisionError:
    print('0 으로 나눌 수 없어요')
except TypeError:
    print('값의 형태가 이상해요')
except Exception as err:
    print('에러가 발생했어요',err)
else:
    print('정상 동작했어요')
finally:
    print('수행 종료')

#모듈 (하나의 파이썬 파일 .py) (구글 참고 list of python modules)
import nadocoding.goodjob as goodjob #모든 기능을 이용가능
goodjob.say()

from nadocoding.goodjob import say #필요한것들만 이용
say()

import random
my_list = ['가위','바위','보']
print(random.choice(my_list))

import nadocoding.goodjob
nadocoding.goodjob.say()

from nadocoding import goodbye
goodbye.bye()

from nadocoding import goodbye,goodjob
goodbye.bye()
goodjob.say()