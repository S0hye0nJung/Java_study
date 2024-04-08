#만약 터틀종료후 오류발생하면 창을 다시열어서 다시실행하기
# 문제1. 거북이생성 및 사각형 그리기
import turtle
t1 = turtle.Turtle()
t1.shape('turtle')

for i in range(4):
    t1.forward(200)
    t1.left(90)
turtle.done()
