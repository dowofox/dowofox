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
print(python+''+java)