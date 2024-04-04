# 아래에 링크에 접속하셔서 csv파일을 다운로드한 후, 문제를 풀어주세요:)
# 해당 데이터 다운 받기 : https://www.data.go.kr/data/15126554/fileData.do
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 한글 깨짐처리
from matplotlib import rc, font_manager
font_name = font_manager.FontProperties(fname ='./D2Coding-Ver1.3.2-20180524.ttf')\
                .get_name()
rc('font', family = font_name)
rc('axes', unicode_minus=False) # 음수값처리


# 데이터 불러오기(수업시간에 진행하는 것처럼 data파일 안의 excel파일에 다운로드를 하여 사용해주세요.)
datafile = pd.read_csv('./data/excel/한국언론진흥재단_뉴스빅데이터_연도 및 과목별 언론의 수능난이도 평가_20221231.csv', encoding='utf-8', delimiter=',')


# 데이터 확인
display(datafile)
print(type(datafile))

# 국어(korean)/수학(math)/ 영어(english) 과목 별로 따로 데이터를 저장하기
korean = 

display(korean)

math =  
display(math)

english = 
display(english)


# '보도 기사 수'가 많을 수록 난이도가 어렵다고 가정할때,  
# 1) 국어가 가장 어려웠던 연도와 가장 쉬웠던 연도의 정보를 구하라
# (해당 연도의 모든 정보 : 연도, 과목, 보도 기사 수, 언론의 추정 난이도 평균, 언론의 추정 난이도 표준편차에 대한 정보들)

# 출력문 예시)
#	  연도	과목	보도 기사 수	언론의 추정 난이도 평균	언론의 추정 난이도 표준편차
# 3	2014	국어	142	0.647887	0.573618


# 1-1) 국어가 가장 어려웠던 연도


# 1-2) 국어가 가장 쉬웠던 연도의 정보


# 2) 수학이 가장 어려웠던 연도와 가장 쉬웠던 연도의 정보를 구하라
# (해당 연도의 모든 정보 : 연도, 과목, 보도 기사 수, 언론의 추정 난이도 평균, 언론의 추정 난이도 표준편차에 대한 정보들)
# 2-1) 수학이 가장 어려웠던 연도


# 2-2) 수학이 가장 쉬웠던 연도의 정보


# 3) 영어가 가장 어려웠던 연도와 가장 쉬웠던 연도의 정보를 구하라
# (해당 연도의 모든 정보 : 연도, 과목, 보도 기사 수, 언론의 추정 난이도 평균, 언론의 추정 난이도 표준편차에 대한 정보들)
# 3-1) 국어가 가장 어려웠던 연도


# 3-2) 영어가 가장 쉬웠던 연도의 정보



