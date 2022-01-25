'''
시퀸스 내장 함수

1. enumerate() 함수
  : 리스트와 함께 사용하여, 
    (index,튜플)의 형태로 반환하는 함수
    
ex) for item in enumerate(['a', 'b' , 'c'])
    print(item)

    (결과)
    (0,'a')
    (1,'b')
    (2,'c')
    
2. range() 함수
    : 전달받은 값에 따라서 특정 범위에 데이터를 반환하는 함수
    
    i) range(끝)
    : 0부터 끝에 지정한 번호까지 정수를 생성
    ii) range(시작, 끝)
    : 시작부터 끝 사이의 모든 정수를 생성
    iii) range(시작, 끝, 단계)
    : 시작부터 끝 사이 수들을 단계의 크기만큼 생성
    
3. len() 함수
 : 함수의 전달된 객체의 길이(개수)를 반환하는 함수
 ex) li = [1,2,3,4]
    len(li)  --> 4
    
4. sorted() 함수
 : 반복가능한 객체를 오름차순으로 정렬한 결과 반환하는 함수
 ex) li = [10,3,9,2,5]
    sorted(li) --> [2,3,5,9,10]
    
5. zip() 함수
 : 여러 개의 반복가능한 객체들을 튜플로 묶어서 반환하는 함수
 ex) names  = ['c언어', '파이썬', 'JAVA']
     scores = [100, 90, 80]
     zip(names, scores)
    --> ('c언어', '100'),
        ('파이썬', 90),
        ('JAVA', 80),   
'''

#C언어, 파이썬, JAVA
#0,1,2

prog = ['c언어', '파이썬', 'JAVA']
for item in enumerate(prog) :
    print(item)
    
for i in range(10):
  print(i, end = ' ')
  
print()
for i in range(1,11):
  print(i, end = ' ')
  
print()

for i in range(1,20,2):
    print(i, end= ' ')
    
print()

for i in range(2,21,2):
    print(i, end = ' ')
    
li = ['월','화','수','목','금','토','일'] 
print(li)
print('li 의 요소의 개수 : {}' .format(len(li)))

scores = [100, 90, 65, 80, 70]
print(scores)
print(sorted(scores))

names = ['s1', 's2','s3','s4','s5']

for student in zip(names, scores):
    print(student)