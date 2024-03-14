# 참고 문제 답을 구분하기 위해서 print( ,end='\n\n')를 사용

# 문제1) 다음 코드를 실행해보고 오류가 발생하는 원인은?
t = (1, 2, 3)
# t[0] = 'a'
# Traceback (most recent call last):
#   File "<pyshell#46>", line 1, in <module>
#     t[0] = 'a'
# TypeError: 'tuple' object does not support item assignment
print('1번 문제')
print('답 : tuple은 immutable자료형이기 때문에 오류 발생', end ='\n\n')



# 문제2) 다음 튜플을 리스트로 변환하시오
print('2번 문제')
interest = ('삼성전자', 'LG전자', 'SK Hynix')
l =list(interest) 
print(type(l), l, end='\n\n')

  

# 문제3) 1 부터 99까지의 정수 중 짝수만 저장된 튜플을 생성하시오 
 #예시: (2, 4, 6, 8 ... 98)
print('3번 문제')
l = []
for i in range(2,99,2):
    l.append(i)
tu =tuple(l)
print(tu, end ='\n\n')



# 문제4) 다음 아이스크림 이름과 희망 가격을 딕셔너리로 구성하시오
# 이름	희망 가격
# 메로나 	1000
# 폴라포 	1200
# 빵빠레 	1800
print('4번 문제')
icecream = {'메로나':1000, '폴라포':1200, '빵빠레':1800}
print(icecream, end='\n\n')


# 문제5) 다음의 딕셔너리에서 values 값으로만 구성된 리스트를 생성하시오
print('5번 문제')
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
l = list(icecream.values())
print(l)
