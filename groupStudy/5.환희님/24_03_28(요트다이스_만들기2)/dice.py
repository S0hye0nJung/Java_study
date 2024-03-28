### 1번
# Small Straight : 이어지는 주사위 눈이 4개 이상일 때. 고정 15점. ex) 1 2 3 4 6, 1 3 4 5 6
import random

dice1 = int(random.random()*3+1)
dice2 = int(random.random()*3+1)
dice3 = int(random.random()*3+1)
dice4 = int(random.random()*3+1)
dice5 = int(random.random()*3+1)
point = 0

if (dice2 == dice1 + 1) and (dice3 == dice2 + 1) and (dice4 == dice3 + 1) :
    point += 15
elif (dice3 == dice2 + 1) and (dice4 == dice3 + 1) and (dice5 == dice4 + 1):
    point += 15


print(dice1,dice2,dice3,dice4,dice5)
print(point)




### 2번
# Large Straight : 이어지는 주사위 눈이 5개일 때. 고정 30점. ex) 1 2 3 4 5, 2 3 4 5 6

dice1 = int(random.random()*3+1)
dice2 = int(random.random()*3+1)
dice3 = int(random.random()*3+1)
dice4 = int(random.random()*3+1)
dice5 = int(random.random()*3+1)
point = 0

if (dice2 == dice1 + 1) and (dice3 == dice2 + 1) and (dice4 == dice3 + 1) and (dice5 == dice4 + 1):

    point += 30

print(dice1,dice2,dice3,dice4,dice5)
print(point)
