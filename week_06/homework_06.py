## 출력 포맷 형식으로 전체 자릿수 지정 프로그램 ##
print("="*49)
print("■ 202345050 컴시과 1학년 B반 차혜진 9주차 실습2")
print("■ 정수, 실수, 문자열을 입력받아")
print("■ 출력 포맷 형식으로 전체 자릿수 지정 프로그램")
print("-"*49)
jungsu=eval(input("정수를 입력하세요 => "))
silsu=eval(input("\n실수를 입력하세요 => "))
munja=(input("\n문자를 입력하세요 => "))
#- 정수 데이터 타입 출력 형식 지정 -#
print("\n>>정수 데이터 타입 출력 형식")
print("|%d|"%jungsu)
print("|%5d|" %jungsu)
print("|%-5d|" %jungsu)
print("|%+5d|" %jungsu)
print("|%05d|" %jungsu)
print("-"*49)
#- 실수 데이터 타입 출력 형식 지정 -#
print(">>실수 데이터 타입 출력 형식")
print("|%f|" %silsu)
print("|%10.1f|" %silsu)
print("|%10.3f|" %silsu)
print("|%-10.3f|" %silsu)
print("|%+10.3f|" %silsu)
print("|%010.3f|" %silsu)
print("-"*49)
#- 문자열 데이터 타입 출력 형식 지정 -#
print(">>문자열 데이터 타입 출력 형식")
print("|%s|" %munja)
print("|%8s|" %munja)
print("|%-8s|" %munja)
print("="*49)