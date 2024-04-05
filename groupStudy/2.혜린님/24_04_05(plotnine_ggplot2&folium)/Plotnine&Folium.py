# 서울시 공공도서관 위치를 지도에 출력해보는 예제
# 한글처리
import matplotlib.pyplot as plt
import numpy as np
import warnings
import csv
import pandas as pd

# 데이터시각화 tool
from plotnine import * # r의 ggplot2 시각화패키지를 python에서도 사용
import folium
import re

plt.rcParams['font.family'] = 'D2Coding'
plt.rcParams['axes.unicode_minus'] = False
warnings.filterwarnings('ignore')

library = pd.read_csv('./data/서울시 공공도서관 현황정보.csv',delimiter=',', encoding='cp949')
display(library.head())

# 구별 도서관 개수 확인
library['구명'].value_counts()


# 1) scatter, library => 시각화(위치)
library.plot.scatter(x='경도', y='위도')
plt.show()



# 2) plotnine, ggplot2
(ggplot(library)
    + aes(x='경도', y='위도', color ='구명')
    + geom_point()
    + theme(text=element_text(family='D2coding'))
)



# 3) folium으로 시각화
lng = library.위도.mean()
lat = library.경도.mean()
m =folium.Map(location=[lng,lat], width=300)

# 팝업 내용은 library_info로 팝업 창의 너비는 300으로 해주세요!
for lib in library.index:
    library_info = (library.loc[lib, '도서관명'] + '-' + library.loc[lib, '주소'] + 
                        '전화번호 : ' + str(library.loc[lib, '전화번호']) + 
                        '운영시간 : ' + str(library.loc[lib, '운영시간']) + 
                        '정기 휴관일 : ' + str(library.loc[lib, '정기 휴관일']))
    icon_color ='blue'
    folium.CircleMarker(
        location=[library.loc[lib,'위도'],library.loc[lib,'경도']],
        radius=6,
        popup= library_info,
        color =icon_color,
        fill = True,
        fill_color ='green',
        fill_opacity =0.6,
        tooltip ='클릭하시면 해당 도서관 정보를 보실 수 있습니다:)'
    ).add_to(m)   
m

