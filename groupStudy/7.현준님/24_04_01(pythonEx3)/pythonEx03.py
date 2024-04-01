import pandas as pd
import numpy as np
# 1. 다음 데이터를 사용하여 DataFrame을 생성하세요.

data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 35, 42, 29],
        'City': ['New York', 'Paris', 'London', 'San Francisco']}
df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])
print('1번')
display(df)
print()



# 2. 위에서 생성한 데이터프레임에 'Gender' 열을 추가하고 각 행에 'Male' 또는 'Female' 값을 할당하세요.
print('2번')
df['Gender'] = ['Male','Female','Male','Female']
display(df)
print()



# 3. 위에서 생성한 데이터프레임의 인덱스를 'A', 'B', 'C', 'D'로 설정하세요.
print('3번')
df.index = ['A', 'B', 'C', 'D']
display(df)
print()



# 4. 위에서 생성한 데이터프레임에서 'Name' 열만 추출하여 출력하세요.
print('4번')
display(df['Name'])
print()



# 5. 위에서 생성한 데이터프레임에서 'Age' 열의 값이 30 이상인 행들만 필터링하여 출력하세요.
print('5번')
display(df[df['Age'] >=30])
print()



# 6. 다음 두 개의 데이터프레임을 병합하세요.
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})
print('6번')
df3 = pd.concat([df1, df2], ignore_index=True)
display(df3)
print()



# 7. 다음 데이터프레임을 'City' 열을 기준으로 그룹화하여 'Age' 열의 평균을 출력하세요.
df = pd.DataFrame({'City': ['Seoul', 'Busan', 'Seoul', 'Busan'],
                   'Age': [25, 30, 35, 40]})
print('7번')
display(df.groupby('City')['Age'].mean())
print()



# 8. 다음 데이터프레임을 'Age' 열을 기준으로 내림차순으로 정렬하세요.
df = pd.DataFrame({'Name': ['John', 'Anna', 'Peter', 'Linda'],
                   'Age': [28, 35, 42, 29],
                   'City': ['New York', 'Paris', 'London', 'San Francisco']})
print('8번')
df.sort_values(by='Age', inplace=True)
display(df)
print()



# 9. 다음 데이터프레임에서 결측값을 0 으로 채워넣으세요.
df = pd.DataFrame({'A': [1, np.nan, 3, np.nan],
                   'B': [np.nan, 5, np.nan, 8],
                   'C': [10, 11, 12, 13]})
print('9번')
df = df.fillna(0)
display(df)
print()



# 10. 다음 데이터프레임을 이용하여 'Date'를 인덱스로, 'City'를 컬럼으로 하여 피벗테이블을 생성하세요.
df = pd.DataFrame({'Date': ['2022-01-01', '2022-01-01', '2022-01-02', '2022-01-02'],
                   'City': ['Seoul', 'Busan', 'Seoul', 'Busan'],
                   'Value': [100, 200, 150, 250]})
print('10번')

pivot_df = df.pivot_table(index='Date', columns='City', values='Value')
display(pivot_df)




