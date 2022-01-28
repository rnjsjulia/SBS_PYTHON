
'''
    파일 복사
    
    원본 파일 --> 변수 --> 복사본
      (읽기)               (쓰기)
    1. 원본 파일 읽기
    2. 1024Byte(1KB) 씩 읽어온다
    3. 1024Byte(1KB) 씩 저장한다
    4. 입력, 출력 close(종료)
    
    # 파일(20GB) --복사--> [버퍼](1KB) --> 생성
    # 버퍼 : 임시 저장 공간
    # 버퍼링? 
    # 1000MB        :1GB
    # 20 * 1000MB   : 20GB(20000MB)
    #20GB 처리하는  : 200초(3분 20초)
    # 1초 10억 bit 이상
    
    with
    : 파일 입출력 시, 자동으로 close() 함수를 호출한다.
    
    with open(파일경로, 모드) as 파일 객체:
        처리 코드
'''

path = 'C:/새 폴더/파이썬/SBS_PYTHON/SBS_PYTHON/day10/'
file = path+ 'hello.txt'
copy = path + 'hello(복사).txt'

buffer_size = 1024 #버퍼 용량:1024Byte(1KB)

with open(file, 'rb') as source:
    with open (copy, 'wb') as copyfile:
        while True:
            # 원본 파일을 버퍼용량만큼 읽어와서 buffer 에 저장
            # buffer 에는 1KB 만큼의 파일 데이터가 저장
            buffer = source.read(buffer_size)
            if not buffer:
                break
            # 1KB 씩 파일 생성
            copyfile.write(buffer)
print(copy)
print('파일이 복사되었습니다.')