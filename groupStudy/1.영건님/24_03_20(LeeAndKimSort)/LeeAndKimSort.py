# 참고 각각의 문제의 답을 구분하기 위해서 print( ,'\n\n')를 사용


## 문제 ##
# 아래 names 문자열을 이용해서 1 ~ 4 번 문제 풀면됩니다!

names = "김영건,손흥민,박지성,나윤호,홍명보,심주찬,나윤호,유현준,김영건,표민,김하영,김영건,정소현,윤혜린,이환희,이영표,유현준,손흥민,정소현".split(",")

# 1 김씨와 이씨 성을 가진 사람은 각각 몇명인지 출력
# >> list - lambda식 이용
ReturnLambdaLee = lambda names: [names[i] for i in range(len(names)) if names[i][0] == '이' ]
ReturnLambdaKim = lambda names: [names[i] for i in range(len(names)) if names[i][0] == '김' ]
print('이씨 성을 가진 사람 = ',ReturnLambdaLee(names))
print('김씨 성을 가진 사람 = ',ReturnLambdaKim(names),'\n\n')


#2 김영건 이름이 몇개 들어있는지 출력
# >> lambda식 이용
count =0
ReturnLambda = lambda names: [names[i] for i in range(len(names)) if names[i] == '김영건']
print('"김영건"이라는 이름',len(ReturnLambda(names)),'개 존재','\n\n')


#3 중복을 제거 후 출력
sl = list(set(names))
print('중복을 제거 후 출력 = ',sl,'\n\n')


#4 중복 제거 한 이름을 오름차순으로 출력
sl = sorted(list(set(names)))
print(sl)

