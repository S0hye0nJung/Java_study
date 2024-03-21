# [간단한 비밀번호 생성 프로그램]
# chars문자열에서 random으로 추출해서 비밀번호 생성
# 몇 개를 추출할 것인지는 입력받을 길이로 결정

# 여기에 random 모듈 import하기
import random
print('Welcome To Password Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%^&*().,?0123456789'

# 여기에 생성할 비밀번호의 갯수와 길이를 각각 number와 length라는 변수로 입력받는 코드 작성
number = int(input('몇 개의 비밀번호를 생성할까요? >>'))
length = int(input('몇 자리의 비밀번호를 생성할까요? >>'))


# 비밀번호 생성 - 이중 for문 사용
print('\n--Here are your passwords--')

  # 여기에 for문 작성
def mkPassword():
    str = ''
    for i in range(length):
        for j in random.choice(chars):
            str+= j
    print(str)
            
            
        

    
for i in range(number):
    mkPassword()
    

# ----------------------------------
# 출력 예시 - 길이가 10인 비밀번호를 8개 생성

# Welcome To Password Generator
# 생성할 비밀번호의 갯수 :  8
# 생성할 비밀번호의 길이 :  10

# --Here are your passwords--
# XnG,s?Ax2r
# v06hOvx(st
# 6)@ll%mKMm
# ^HCUV&w1gs
# v6r5QbDQBc
# Y39BJ5SJin
# ^JI9yb.R.w
# LaQ.rFt5G6
