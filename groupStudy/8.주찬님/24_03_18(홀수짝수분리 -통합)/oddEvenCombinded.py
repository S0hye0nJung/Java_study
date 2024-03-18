# 이 코드는 사용자로부터 5개의 값을 입력받습니다.
# 값이 홀수인 경우 a_data에 추가하고, 
# 짝수인 경우 b_data 추가하여 한개의
# 한개의 list로 통합하여 출력합니다.

# 오타를 찾고 코드를 완성해주세요 

a_data = [] 
b_data = {}

# 사용자로부터 입력을 받아 처리
for num in range(5):
    i = int(input("값을 입력하세요: "))   
    if i % 2 == 0: 
         key = f'{i}'
         b_data[key] = 1
        
    else: 
        a_data.append(i)
        

# 두개의 data가 합쳐짐
combined_data = a_data + list(b_data.keys())

# 결과 출력
print("결과:", combined_data)
