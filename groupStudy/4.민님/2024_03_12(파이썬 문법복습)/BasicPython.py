# 참고) 다음 문제와 구분하여 보기 위해서 print함수에 (, end="\n\n") 추가함
#1)주어진 문자열에서 l이 몇 번 등장하는지 세시오(count)
print("1번 문제")
text = "hello world"
char = "l"
print(text.count(char), end="\n\n")


#2)문자열에서 공백을 모두 제거한 후에 결과를 출력하세요.(replace)
print("2번 문제")
text = "hello world"
print(text.replace(" ",""), end="\n\n")


#3)해당 문자열을 거꾸로 출력하세요.(reverse)
print("3번 문제")
text = "python"
## 1)
print(text[::-1], end="\n\n")

## 2)
text = "python"
text = " ".join(text).split(" ")
text.reverse()
print(text)


#4)주어진 리스트에서 중복된 항목을 제거하고, 결과를 출력하세요.(set)
print("4번 문제")
list = [1, 2, 2, 3, 4, 4, 5]
print(set(list), end="\n\n")


#5)주어진 리스트를 역순으로 정렬한 결과를 출력하세요.(reverse)
print("5번 문제")
list = [3, 1, 4, 1, 5, 9, 2] 
list.reverse()
print(list, end="\n\n")


#6)주어진 리스트에 있는 모든 숫자의 합을 계산하여 출력하세요.(sum)
print("6번 문제")
list = [1, 2, 3, 4, 5]
sum = list[0] + list[1] + list[2] + list[3] + list[4]  
print(sum, end="\n\n")


#7)해당 리스트의 최대값과 최소값을 출력하세요.(min,max)
print("7번 문제")
list = [5, 2, 7, 1, 9] 
print(min(list), max(list), end="\n\n")


#8)해당 리스트에 add리스트를 더하시오(extend)
print("8번 문제")
list = [1, 2, 3, 4, 5]
add = [9, 8, 7]
## 1)
print(list+add, end="\n\n")

## 2)
list.extend(add)
print(list, end="\n\n")


#9)숫자 4를 리스트 안에 있는 숫자1 뒤에 삽입하시오(insert)
print("9번 문제")
list = [1, 2, 3, 5]
list.insert(1,4)
print(list)
