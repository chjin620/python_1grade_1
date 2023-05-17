##------------------------------------------
##문자열 슬레이싱(4-16)
##------------------------------------------
a="Python Programming"
print("-"*80)
print("'Python Programming'에서 [:2] 출력 : ",a[:2])
print("-"*80)
print("'Python Programming'에서 [3:] 출력 : ",a[3:])
print("-"*80)
print("'Python Programming'에서 [:] 출력 : ",a[:])

##------------------------------------------
##문자열 나누기(4-17)
##------------------------------------------
a="20230815Monday"
year=a[:4]
month=a[4:6]
day=a[6:8]
week=a[8:]
print("-"*80)
print("'20230815Monday'에서 년도 출력 : ",year)
print("-"*80)
print("'20230815Monday'에서 월 출력 : ",month)
print("-"*80)
print("'20230815Monday'에서 날짜 출력 : ",day)
print("-"*80)
print("'20230815Monday'에서 요일 출력 : ",week)
print("-"*80)
print("문자열을 연결하여 출력 : ",year+"년 "+month+"월 "+day+"일 "+week)

##------------------------------------------
##문자열에서 틀린 철자 고치기(4-18)
##------------------------------------------
a="Sprce"
print("-"*80)
print("'sprce'에서 틀린 철자 앞에 있는 문자열 출력 : ",a[:2])
print("-"*80)
print("'sprce'에서 틀린 철자 뒤에 있는 문자열 출력 : ",a[3:])
print("-"*80)
print("'sprce'에서 틀린 철자 r을 a로 치환하여 전체 문자열 출력 : ",a[:2]+"a"+a[3:])

##------------------------------------------
##문자열관련 함수(4-19~4-26)
##------------------------------------------
##Count 함수 (4-19)
##------------------------------------------
a="Spacezone"
print("-"*80)
print("'Spacezone' 에서 'e'의 개수 출력 : ",a.count('e'))

##------------------------------------------
##Find 함수 (4-20)
##------------------------------------------
a="I can do it"
print("-"*80)
print("'I can do it' 에서 'a'의 포지션 출력 : ",a.find('a'))
print("-"*80)
print("'I can do it' 에서 'do'의 포지션 출력 : ",a.find('do'))
print("-"*80)
print("'I can do it' 에서 없는 문자의 포지션 출력 : ",a.find('s'))

##------------------------------------------
##Index 함수 (4-21)
##------------------------------------------
a="Have a good time"
print("-"*80)
print("'Have a good time' 에서 'a'의 포지션 출력 : ",a.index('a'))
print("-"*80)
print("'Have a good time' 에서 'me'의 포지션 출력 : ",a.index('me'))

##------------------------------------------
##Strip 함수 (4-22)
##------------------------------------------
a=" power "
print("-"*80)
print("' power ' 에서 왼쪽과 오른쪽에 있는 공백을 모두 제거 : ",a.strip())
print("-"*80)
print("' power ' 에서 왼쪽에 있는 공백을 모두 제거 : ",a.lstrip())
print("-"*80)
print("' power ' 에서 오른쪽에 있는 공백을 모두 제거 : ",a.rstrip())

##------------------------------------------
##upper,lower 함수 (4-23)
##------------------------------------------
a="Speed Zone"
print("-"*80)
print("'Speed Zone' 을 대문자로 변환하여 출력 : ",a.upper())
print("-"*80)
print("'Speed Zone' 을 소문자로 변환하여 출력 : ",a.lower())

##------------------------------------------
##join 함수 (4-24)
##------------------------------------------
a="/"
print("-"*80)
print("'asdf'를 '/'를 사용하여 구분되도록 출력 : ",a.join('asdf'))
a=" or "
print("-"*80)
print("'asdf'를 'or'를 사용하여 구분되도록 출력 : ",a.join('asdf'))
##------------------------------------------
##replace 함수 (4-25)
##------------------------------------------
a="speed zone"
print("-"*80)
print("'speed zone'에서 'speed' 를 'power'로 대체하여 출력 : ",a.replace("speed","power"))
##------------------------------------------
##slit 함수 (4-26)
##------------------------------------------
a="One Two Three"
print("-"*80)
print("'One Two Three'에서 문자열을 공백으로 구분하여 출력 : ",a.split( ))
a="spring:summer:fall:winter"
print("-"*80)
print("'spring:summer:fall:winter'에서 문자열을 ':'으로 구분하여 출력 : ",a.split(':'))
##------------------------------------------
##논리 데이터 타입 (4-27)
##------------------------------------------
a=(100<100)
print("-"*80)
print("a=(100<100)일 때 결과 : ",a)
b=(300==300)
print("-"*80)
print("b=(300==300)일 때 결과 : ",a)
c=True
print("-"*80)
print("c=True일 때 c의 타입 : ",type(c))