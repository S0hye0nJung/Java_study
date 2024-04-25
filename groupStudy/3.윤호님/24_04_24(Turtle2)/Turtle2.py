# 저번에 했던 거북이을 기억하며 거북이를 이용해서 그림그리기 
# 모르면 구글링가능 
# ??? 안에 값을 넣으시면 됩니다!
###################################### 에러 날 수 있으니 따로 돌리기 ######################################
from turtle import *

speed(0)
colors = ['red','green','blue'] # 색깔
pensize(2)                      # 펜 사이즈
degree = 2                      # 각도 조절

for i in range(1,500):
    pencolor(colors[i%3])               # 선의 색깔을 3개를 반복해서 설정 
    forward(i)                # 거북이 이동거리
    left(90+degree)                # 각도 돌리기
mainloop() 


###################################### 에러 날 수 있으니 따로 돌리기 ######################################
from turtle import *
import turtle as t
 
n = 60                  # 원의 갯수
t.shape('turtle')          # 터틀 모양 설정
t.speed('fastest')          # 거북이 속도를 가장 빠르게 설정
for i in range(n):      # 반복 횟수
    t.circle(120)       # 반지름이 120인 원을 그림
    t.right(360 / n)    # 오른쪽으로 돌면서 그림 그리기
    
mainloop()
