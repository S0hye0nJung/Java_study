# < 문제 >
### 1. 각 코드에서 일어난 ERROR의 원인을 서술하시오. (튜플)
#### 1). 
t = 1,2,'a','b'
print(t[0])
del t[0]
print(type(t), t)
# TypeError: 'tuple' object doesn't support item deletion
# 튜플은 del기능(삭제) 없음 => immutable자료형이라서


#### 2). 
t[0] = 'hong' 
print(type(t), t)
# TypeError: 'tuple' object does not support item assignment
# 튜플은 리스트처럼 변경하는 기능 없음 => immutable자료형이라서


#### 3).
def minmax(nums):
    min_val = min(nums)
    max_val = max(nums)
    return min_val, max_val
    
lower, upper = minmax([4,5,2,3,1,6,7])
print(type(lower), lower)
print(type(upper), upper)
print()
lower, upper, other = minmax([4,5,2,3,1,6,7]) 
# ValueError: not enough values to unpack (expected 3, got 2)
# unpacking시에 동수로 해야함


#### 4). indexing
t = 1,2,'a','b'
print(t[])
# SyntaxError: invalid syntax. Perhaps you forgot a comma?
# 값을 넣어서 인덱싱해야하는데, 빈값이라 에러
print(t[1])
print(t[-1])




### 2. 코드 채워넣기 : 회귀분석

import statsmodels.api as sm
from scipy import stats

X = [1,2,3,4,5]
y = [6,7,8,9,10]
A = stats.linregress(X, y)
print(type(A), A)

# * 다음 빈칸을 채우세요.
print(f'기울기 = {A.slope}')
print(f'편향 = {A.intercept}')
print(f'R2 = {A.rvalue}')
print(f'피어슨값 = {A.pvalue}')




### 3. 해당하는 그림의 코드 입력하기 

#### 1.) 다중분류
import mglearn 
from sklearn.datasets import make_blobs
* mglearn 모듈과 scikit-learn의 make_blobs 함수를 임포트, 클러스터링 알고리즘의 실험이나 군집 데이터 시각화 
* ​make_blobs : scikit-learn의 datasets 모듈에 포함된 함수 -> 가상의 데이터셋을 생성
 - make_blobs 함수가 받는 인자
    n_samples: 생성할 전체 데이터 포인트 수
    n_features: 특성(feature) 수, 즉 차원
    centers: 클러스터 중심의 수
    ...

X, y = make_blobs(n_samples=100, random_state=42)
mglearn.discrete_scatter(X[:,0], X[:,1], y)
plt.xlabel('A_LINE')
plt.ylabel('B_LINE')
plt.legend(['a_side', 'b_side', 'c_side'])
plt.show()



#### 2.) 이미지 데이터셋 : 올리베티 얼굴 이미지
import numpy as np
from sklearn.datasets import fetch_olivetti_faces
olivetti = fetch_olivetti_faces()
def imgshow(N, M, img, cmap):
    fig = plt.figure(figsize=(8,5))
    plt.subplots_adjust(top=1, bottom=0, hspace=0, wspace=0.05)
    img_list = np.random.choice(range(len(img.data)), N * M) 
    for i in range(N):
        for j in range(M):
            k = img_list[i*M+j]           
            ax = fig.add_subplot(N, M, i*M+j+1)
            ax.imshow(img.images[k], cmap=cmap)
            ax.grid(False)
            ax.xaxis.set_ticks([])
            ax.yaxis.set_ticks([])
            plt.title(img.target[k])
    plt.tight_layout()
    plt.show()

np.random.seed(42)
imgshow(3,5,olivetti,'gray')


#### 3.) sklearn
import warnings
warnings.filterwarnings('ignore')
%matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'D2Coding'
plt.rcParams['axes.unicode_minus'] = False
from sklearn.datasets import load_digits
import seaborn as sns

digits = load_digits()
idx = int(input('숫자이미지의 인덱스를 입력하세요!! => '))
sns.heatmap(digits.images[idx], annot=True, fmt="2.0f", cbar=True, xticklabels=True, yticklabels=True, cmap='YlGnBu')
plt.title(f"MNIST handwrite digit image {idx} = {digits.target[idx]}")
plt.show()
