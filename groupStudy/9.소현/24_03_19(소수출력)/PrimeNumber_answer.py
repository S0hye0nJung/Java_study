# 문제에 대한 답
num =int(input("숫자를 입력하세요 >> "))
for i in range(2, num+1):
    # if(i==2):
    #     print(i)
    for j in range(2, i+1):
        if(i == j):
            print(i)  
        elif(i%j == 0):
            break;
        
    



