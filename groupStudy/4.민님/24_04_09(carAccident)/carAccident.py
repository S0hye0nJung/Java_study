import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family']='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

data1 = pd.read_csv('D:/sohyeon/05.python/data/2014년 졸음운전 교통사고.csv',encoding='euc-kr') 
data2 = pd.read_csv('D:/sohyeon/05.python/data/2015년 졸음운전 교통사고.csv',encoding='euc-kr') 
data3 = pd.read_csv('D:/sohyeon/05.python/data/2016년 졸음운전 교통사고.csv',encoding='euc-kr') 



# 1. 2014년부터 2016년까지의 졸음운전 교통사고 발생 횟수의 총합과 평균 구하기
# 각 연도별 발생 횟수의 총합과 평균 구하기
# 2014년
data1Sum = data1['사고(건)'].sum()
data1Avg = data1['사고(건)'].sum()/len(data1['사고(건)']) 
print(f'2014년의 졸음운전 교통사고 발생 횟수 총합 = {data1Sum}')
print(f'2014년의 졸음운전 교통사고 발생 횟수 월평균 = {data1Avg:.2f}\n')

# 2015년
data2Sum = data2['사고(건)'].sum() 
data2Avg = data2['사고(건)'].sum()/len(data2['사고(건)']) 
print(f'2015년의 졸음운전 교통사고 발생 횟수 총합 = {data2Sum}')
print(f'2015년의 졸음운전 교통사고 발생 횟수 월평균 = {data2Avg:.2f}\n')

#2016년
data3Sum = data3['사고(건)'].sum()
data3Avg = data3['사고(건)'].sum()/len(data3['사고(건)']) 
print(f'2016년의 졸음운전 교통사고 발생 횟수 총합 = {data3Sum}')
print(f'2016년의 졸음운전 교통사고 발생 횟수 월평균 = {data3Avg:.2f}\n')

# 2014~2016년 총합과 평균
totalDataSum = data1Sum + data2Sum + data3Sum
totalDataAvg = totalDataSum/3
print(f'2014년부터 2016년까지의 졸음운전 교통사고 발생 횟수의 총합 = {totalDataSum}')
print(f'2014년부터 2016년까지의 졸음운전 교통사고 발생 횟수의 평균 = {totalDataAvg}\n')




# 2. 각 연도별 졸음운전 교통사고 발생 건수의 추이 시각화하기
# 각 연도별 사고 발생 건수 추이 시각화
dataCount = [data1Sum, data2Sum, data3Sum]
years = ['2014','2015','2016']
plt.bar(years, dataCount, color ='orange')
plt.xlabel('연도')
plt.ylabel('교통사고 발생건수')
plt.title('2014~2016년 교통사고 발생건수 추이')
plt.show()




# 3. 졸음운전 교통사고 발생 건수가 가장 많은 연도와 해당 연도의 월별 사고 발생 추이 시각화하기
# 위의 시각화된 그래프를 보면 2015년도가 가장 많이 교통사고가 발생한 년도임을 알 수 있다.
months = ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월']
accidents = list(data2['사고(건)'])
plt.plot(months, accidents, color ='green', marker='o')
plt.xlabel('월별')
plt.ylabel('교통사고 발생건수')
plt.title('2015년 교통사고 발생건수 추이')
plt.xticks(range(len(months)), [f'{max_accident_year} {month}' for month in months], rotation=45)
plt.show()






