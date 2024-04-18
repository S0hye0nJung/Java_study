# 문제. 500명의 키와 몸무게, 비만도 라벨을 이용해 비만을 판단하는 모델을 만들어보자
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

# 오류처리
import warnings
warnings.filterwarnings('ignore')
%matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 한글처리
plt.rcParams['font.family'] = 'D2Coding'
plt.rcParams['axes.unicode_minus'] =False

# 1. 데이터 가져오기(힌트 : pandas와 matplotlib을 import해서 엑셀파일 불러오기)
df = pd.read_csv('./data/bmi_500.csv', index_col='Label')
print(df.head(), df.index.unique())

# 해당 데이터에는 4개의 컬럼과 6개의 레이블이 있음을 확인


# 2. 데이터 시각화하기
def scatter(label, color):
    t = df.loc[label]
    plt.scatter(t['Weight'], t['Height'], color=color, label=label)

scatter('Extreme Obesity', 'black')
scatter('Weak', 'blue')
scatter('Obesity', 'pink')
scatter('Overweight', 'red')
scatter('Extremely Weak', 'yellow')
scatter('Normal', 'green')

plt.legend()
plt.show()


# 3. 모델링 학습 및 평가 후 예측하기
df = pd.read_csv('./data/bmi_500.csv')

X = df.loc[:, 'Height' : 'Weight']
y = df.loc[:, 'Label']

X_train = X.iloc[:350, :]
X_test = X.iloc[350:, :]
y_train = y.iloc[:350]
y_test = y.iloc[350:]

model = KNeighborsClassifier(n_neighbors=10)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
res = metrics.accuracy_score(y_test, y_pred)
res


# 4. 원하는 값 입력해보기
model.predict([[176,80]])
