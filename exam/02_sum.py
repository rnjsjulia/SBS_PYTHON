'''정수 하나를 입력받아
1부터 입력받은 수 까지의 합계를 구하는 프로그램을 완성하시오.
입력예시 N : 10
출력예시 합계 : 55'''

print("입력 :")
i = int(input())

sum = 0
for n in range(1,i+1):
    sum = sum + n
    
print( 'sum:', sum)
