# format() 메소드
# {}괄호 기호로 변수나 값이 표시될 위치(형식)을 
# 지정하여 출력하는 메소드

print(' 내 이름은 {}'.format('권수경'))

a = 10
b = 20
print(' a : {}, b : {} '.format(a, b))

print('b : {1}, a : {0}' .format(a, b))

print('b : {1}, a : {0},{0}' .format(a, b))

print('{0}하세요, 저는 권수경{1}, 과목은 파이썬{1} 다음에 봐요 {0}'.format('안녕', '입니다'))

tell,tel2,tel3 = '02', '222', '3333'
print('연락처 : {0}-{1}-{2}' .format(tell,tel2,tel3))

academy = 'SBS'
print('name : {name}' .format(name = academy))