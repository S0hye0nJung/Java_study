# IMDB 영화 리뷰 데이터셋을 사용한 LSTM 예제

# 데이터셋은 긍정적인 리뷰는 1, 부정적인 리뷰는 0으로 레이블이 지정되어 있습니다.

import numpy as np
from keras.datasets import imdb
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Embedding, Bidirectional, LSTM

# 모델 특성 설정
max_features = 20000 # 단어의 최대 개수 즉, 데이터에서 가장 자주 등장하는 단어의 개수->20000으로 설정
maxlen = 100 # 시퀀스 길이 -> 100으로 설정
batch_size = 32

# 데이터 로드 및 train/test 셋으로 데이터 분할
(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=max_features)

# 시퀀스 패딩
# 리뷰의 길이가 다양하므로 sequence.pad_sequences() 함수를 사용하여 시퀀스를 일정한 길이
# 즉 ,위에서 설정한 최대 길이(maxlen)로 패딩합니다.
print('시퀀스 패딩 (samples x time)')
X_train = sequence.pad_sequences(X_train, maxlen=maxlen)
X_test = sequence.pad_sequences(X_test, maxlen=maxlen)
print('x_train shape:', X_train.shape)
print('x_test shape:', X_test.shape)

# 모델 구축
# 층 쌓는 순서
# 1. Sequential() 층
model = Sequential()

# 2. Embedding() 층
# 입력으로 들어온 각 정수를 고정된 차원의 벡터로 임베딩하는 층
# 이 층의 input_dim은 max_featurs로, output_dim은 128로, input_length는 maxlen으로 지정해서 작성해주세요.
model.add(Embedding(input_dim=max_features, output_dim=128, input_length=maxlen))

# 3. Bidirectional() 층
# 양방향 LSTM 층을 추가해주는 층
# 예시 : LSTM의 출력층을 32개로 하는 Bidirectional층은 Bidirectional(LSTM(32))라고 작성합니다.
# 이 층의 LSTM 출력층을 64로 지정해서 작성해주세요.
model.add(Bidirectional(LSTM(64)))

# 4. Dense() 층
# 완전 연결(fully connected) 층
# 이 층은 입력 데이터를 받아 각 뉴런에 대한 가중치를 적용하고 활성화 함수를 통해 출력층을 생성합니다.
# 이 층의 출력층의 개수는 1개, 활성함수는 sigmoid로 지정해주세요
model.add(Dense(1, activation='sigmoid'))

# model compile
# 옵티마이저는 adam, 손실함수는 binary_crossentropy로, metircs는 'accuracy'로 지정해주세요
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# 모델 학습
# 에포크는 10으로, validation_data는 x_test, y_test로 지정해주세요
model.fit(X_train, y_train, epochs=10, batch_size=batch_size, validation_data=(X_test, y_test))

# 모델 평가
# 손실율과 정확도를 출력해주세요 :D
loss, acc = model.evaluate(X_test, y_test, batch_size=batch_size)
print(f'평가결과(손실율)= {loss:.2f}')
print(f'평가결과(정확도)= {acc:.2f}')
