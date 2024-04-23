# Auto MPG 데이터셋 이용하기
import pathlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# 데이터 셋 다운 (그대로 실행 하면 됨)
dataset_path = keras.utils.get_file("auto-mpg.data", "http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data")
dataset_path

# pandas를 이용해 데이터 읽기 (여기까지 그대로 실행해서 출력해주세요)
column_names = ['MPG','Cylinders','Displacement','Horsepower','Weight',
                'Acceleration', 'Model Year', 'Origin']
raw_dataset = pd.read_csv(dataset_path, names=column_names,
                      na_values = "?", comment='\t',
                      sep=" ", skipinitialspace=True)

dataset = raw_dataset.copy()
dataset.tail()
# (여기까지 그대로 실행해서 출력해주세요)



# 데이터 정제
# 문제 1 - 데이터셋에 누락된 데이터 삭제해주세요

dataset = dataset.dropna()



# 문제 2 - Origin 열을 삭제 후 Origin 값을 바탕으로 USA, Europe, Japan 컬럼을 만들어주세요
# ex)
# USA의 Origin 값 = 1
# Europe의 Origin 값 = 2
# Japan의 Origin 값 = 3

origin = dataset.pop('Origin')

dataset['USA'] = (origin == 1)*1.0
dataset['Europe'] = (origin == 2)*1.0
dataset['Japan'] = (origin == 3)*1.0



# 문제 3 - 산점도 행렬(pairplot) 생성
# MPG, Cylinders, Displacement, Weight 열만 선택해 산점도 생성
# "커널 밀도 추정 그래프" 그리세요

train_dataset = dataset.sample(frac=0.8,random_state=0)
sns.pairplot(train_dataset[['MPG', 'Cylinders', 'Displacement', 'Weight']], diag_kind="kde")



# 문제 4 - 데이터 조사

train_stats = train_dataset.describe()
train_stats = train_stats.transpose() # 보기 쉽게 데이터의 행 열 바꿔주세요
train_stats
