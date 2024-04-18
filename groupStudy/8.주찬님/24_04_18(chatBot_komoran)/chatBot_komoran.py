from konlpy.tag import Komoran
from gensim.models import Word2Vec

# < Word2Vec 모델훈련을 이용해 단어간의 유사확률을 출력하기  >
text = "엄마는 항상 인생은 상자와 같은 거라고 말씀하셨어요.그걸 집기 전에는 알 수 없는 거라고."

#  형태소 분석 후 명사 단어만 추출
# 객체 생성
komoran = Komoran()

# 1) 문장에서 형태소 추출
morphs = komoran.morphs(text)
print(morphs, '\n')

# 2) 품사를 태그
pos = komoran.pos(text)
print(pos, '\n')

# 3) 태깅된 형태소에서 명사만 추출
nouns = komoran.nouns(text)
print(nouns, '\n')

# Word2Vec 모델 훈련
model = Word2Vec(sentences=[nouns], vector_size=100, window=5, min_count=1, sg=0)

# '인생'와 가장 유사한 3개의 단어와 유사확률을 출력하는 코드 완성하기
print("가장 유사한 단어 => ", model.wv.most_similar("인생", topn=3))
