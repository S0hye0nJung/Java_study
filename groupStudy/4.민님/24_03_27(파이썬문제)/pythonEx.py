######################################## 문제 및 정답 ########################################

# # 1번) 데이터 리스트를 plot 메서드를 이용해 line,bar,barh, pie 그래프를 그리시오
import pandas as pd
data = [1, 4, 3, 9, 2, 6, 7]

s = pd.Series(data)
s.plot(kind = 'line')
s.plot(kind = 'bar')
s.plot(kind = 'barh')
s.plot(kind = 'pie')



# # 2번) 다음 중에 넘파이를 사용하여 행렬의 전치(transpose)를 구하는 함수는 무엇인가요?
# a) np.transpose()
# b) np.transpose_matrix()
# c) np.matrix_transpose()
# d) np.matrixTranspose()

# 정답 : a) np.transpose()



# # 3번) 다음 중에 주어진 2차원 배열의 행과 열의 개수를 확인하는 함수는 무엇인가요?
# a) np.size()
# b) np.dimensions()
# c) np.shape()
# d) np.count()

# 정답 : c) np.shape()



# # 4번) 다음 중에 넘파이를 사용하여 모든 원소가 0인 3x3 행렬을 생성하는 함수는 무엇인가요?
# a) np.zero_matrix(3, 3)
# b) np.zeros((3, 3))
# c) np.create_matrix(3, 3)
# d) np.empty((3, 3))

# 정답 : b) np.zeros((3, 3))



# # 5번) 다음 중에 주어진 행렬의 열끼리의 합을 구하는 함수는 무엇인가요?
# a) np.sum(axis=0)
# b) np.add_rows()
# c) np.row_sum()
# d) np.sum_rows()

# 정답 : a) np.sum(axis=0)



# # 6번) 다음 중에 두 행렬의 요소별 곱셈을 수행하는 함수는 무엇인가요?
# a) np.multiply()
# b) np.dot_product()
# c) np.elementwise_multiply()
# d) np.multiply_elements()

# 정답 : a) np.multiply()



