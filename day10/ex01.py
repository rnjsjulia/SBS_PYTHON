'''
    파일 입출력
    
    - 텍스트 파일 생성하기
'''
# 파일 저장 경로
path = 'C:/SBS_HSH/SBS_PYTHON/SBS_PYTHON/Day10/'
    
# 파일 열기 : open(파일명, 모드, 옵션)
file = open(path + 'hello.txt', 'wt', encoding='UTF-8')

# 파일 내에서 출력  : write()
file.write('안녕하세요')
file.write('\n')
file.write('파일 입출력 내용을 학습합니다.')
print('파일이 생성되었습니다.')

file.close()



