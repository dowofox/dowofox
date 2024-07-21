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
ticker = "btc_krw"
ticker = ticker.upper()
print(ticker)
#42
ticker = "BTC_KRW"
ticker = ticker.lower()
print(ticker)
#43
문자열 = "hello"
문자열 = 문자열.capitalize()
print(문자열)
#44
file_name = "보고서.xlsx"
file = file_name.endswith('xlsx')
print(file)
#45
file_name = '보고서.xlsx'
file = file_name.endswith(('xlsx','xls'))
print(file)
#46
file_name = "2020_보고서.xlsx"
print(file_name.startswith("2020"))
#47
a = "hello world"
print(a.split())
#48
ticker = "btc_krw"
print(ticker.split('_'))
#49
date = "2020-05-01"
print(date.split("-"))
#50
data = "039490    "
print(data.rstrip())
#51
movie_rank = ['닥터 스트레인지','스플릿','럭키']
print(movie_rank)
#52
movie_rank.append('배트맨')
print(movie_rank)
#53
movie_rank.insert(1,'슈퍼맨')
print(movie_rank)
#54
movie_rank.remove('럭키')
print(movie_rank)
#55 (x)
del movie_rank[2]
del movie_rank[2]
print(movie_rank)
#56
lang1 = ['C','C++','JAVA']
lang2 = ['Python','Go','C#']
langs = lang1+lang2
print(langs)
#57
nums = [1,2,3,4,5,6,7]
print('max:',max(nums))
print('min:',min(nums))
#58 (x)
nums = [1,2,3,4,5]
print(sum(nums))
#59
cook = ['피자','김밥','만두','양념치킨','족발','피자','김치만두','쫄면','소시지','라면','팥빙수','김치전']
print(len(cook))
#60
nums = [1,2,3,4,5]
average = sum(nums)/len(nums)
print(average)
#61
price = ['20100728',100,130,140,150,160,170]
print(price[1:])
#62
nums = [1,2,3,4,5,6,7,8,9,10]
print(nums[::2])
#63
print(nums[1::2])
#64 (x)
nums = [1,2,3,4,5]
print(nums[::-1])
#65 (x)
interest = ['삼성전자','LG전자','Naver']
print(interest[0],interest[2])
#66 (x)
interest = ['삼성전자','LG전자','Naver','SK하이닉스','미래에셋대우']
print(" ".join(interest))
#67
print("/".join(interest))
#68
print('\n'.join(interest))
#69
string = "삼성전자/LG전자/Naver"
interest = string.split('/')
print(interest)
#70 (x)
data = [2,4,3,1,5,10,9]
data.sort()
print(data)
#71
my_variable = ()
print(type(my_variable))
#72
movie_rank = ("닥터 스트레인지","스플릿","럭키")
print(movie_rank)
#73
nums = (1)
print(type(nums))
#74
t = (1,2,3)
#t[0] = 'a'  #튜플은 원래 값을 바꿀수없다
print(t)
#75
t = 1,2,3,4
print(type(t))
#76
t = ('a','b','c')
t = ('A','b','c')
print(t)
#77
interest = ('삼성전자','LG전자','SK Hynix')
data = list(interest)
print(data,type(data))
#78
data1 = tuple(data)
print(data1,type(data1))
#79
temp = ('apple','banana','cake')
a,b,c = temp
print(a,b,c)
#80
data = tuple(range(2,100,2))
print(data)