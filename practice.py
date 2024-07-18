#1
print('Hello World')
#2
print("Mary's cosmetics")
#3
print('신씨가 소리질렀다. "도둑이야".')
#4
print('C:\\Windows')
#5
print("안녕하세요.\n만나서\t\t반갑습니다.")
#6
print('오늘은','일요일')
#7
print('naver','kakao','sk','samsung',sep=';')
#8
print('naver','kakao','sk','samsung',sep = '/')
#9
print("first",end=""); print("second")
#10
print(5/3)
#11
삼성전자 = 50000
총평가금액 = 삼성전자*10
print(총평가금액)
#12
시가총액 = 298000000000000
현재가 = 50000
PER = 15.79
print(시가총액, type(시가총액))
print(현재가, type(현재가))
print(PER, type(PER))
#13
s = 'hello'
t = 'python'
print(s+'!',t)
#14
2+2*3 
#15
a = "132" 
print(type(a))
#16
num_str = "720"
print(int(num_str))
#17
num = 100
num_str = str(num)
print(num_str, type(num_str))
#18
num = "15.79"
num_float = float(num)
print(num_float)
#19
year = '2020'
year1 = int(year)
print(year1)
print(year1-1)
print(year1-2)
print(year1-3)
#20
air = 48584
air1 = air*36
print(air1,"원")
#21
letters = 'python'
print(letters[0],letters[2])
#22
license_plate = '24가 2210'
print(license_plate[-4:])
#23 (x)
string = '홀짝홀짝홀짝'
print(string[::2])
#24 (x)
string = 'PYTHON'
print(string[::-1])
#25 
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace("-"," ")
print(phone_number1)
#26
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace('-','')
print(phone_number1)
#27 (x)
url = "http://sharebook.kr"
url_split = url.split(".")
print(url_split[-1])
#28 (x)
lang = 'python'
lang = lang.replace('p','P')
print(lang)
#29
string = 'abcdfe2a354a32a'
string = string.replace('a','A')
print(string)
#30
string='abcd'
string = string.replace('b','B')
print(string)
#31
a = "3"
b = "4"
print(a+b)
#32
print("Hi"*3)
#33
print("-"*80)
#34
t1 = 'python'
t2 = 'java'
t3 = t1+' '+t2+' '
print(t3*4)
#35
name1 = '김민수'
age1 = 10
name2 = '이철희'
age2 = 13
print("이름: %s 나이: %d" % (name1,age1))
print("이름: %s 나이: %d" % (name2,age2))
#36
print("이름: {} 나이: {}".format(name1,age1))
print("이름: {} 나이: {}".format(name2,age2))
#37
print(f'이름: {name1} 나이: {age1}')
print(f'이름: {name2} 나이: {age2}')
#38
삼성주식수 = "5,969,782,550"
samsung = 삼성주식수.replace(",","")
samsung1 = int(samsung)
print(samsung1,type(samsung1))
#39
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])
#40
data = "   삼성전자   "
data1 = data.strip()
print(data1)
#41