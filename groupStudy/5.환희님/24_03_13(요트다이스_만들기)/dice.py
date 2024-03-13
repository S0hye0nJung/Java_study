#1) 4 of a Kind : 주사위를 굴려 동일한 주사위 눈이 2개 이상일 때. point에 주사위 눈 3개의 총합 추가.

import random
import math

dice1 = int(random.random()*3+1)
dice2 = int(random.random()*3+1)
dice3 = int(random.random()*3+1)
point = 0

if (dice1 == dice2) or (dice1 == dice3) or (dice3 == dice2) :
    point = dice1 + dice2 + dice3


print(dice1,dice2,dice3)
print(point)



#2) Yacht : 주사위를 굴려 동일한 주사위 눈이 3개 이상일 때. point에 30점 추가.

dice1 = int(random.random()*3+1)
dice2 = int(random.random()*3+1)
dice3 = int(random.random()*3+1)
point = 0

if (dice1 == dice2) and (dice2 == dice3) :
    point += 30

print(dice1,dice2,dice3)
print(point)
