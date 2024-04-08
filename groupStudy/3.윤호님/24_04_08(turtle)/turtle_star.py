# 문제2. 오각별 그리기
# 오각별의 특징을 잘생각해서 구현하기
# hint) 오각별에서 삼각형 꼭대기의 각은 72도! 
# hint) forward() / left() / right() 사용
import turtle
t2 = turtle.Turtle()
t2.shape('turtle')

# for i in range(5):# 총5번 반복
#     t2.forward(100)
#     t2.right(60)
  
for i in range(5):# 총5번 반복
    t2.forward(100)
    t2.right(72)
    t2.forward(100)
    t2.left(144)
turtle.done() # 일반적으로 한 번에 하나의 거북이 창만 열 수 있습니다. 
#이미 열린 창이 닫히지 않고 남아 있으면 새로운 거북이 객체를 생성할 수 없습니다.
#따라서 종료해야함
 
