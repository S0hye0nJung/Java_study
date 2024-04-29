# < 문제 >
# < 1 >
e = [1, 'a', [5,6,7,[7,8,9,[10,11,12]]], print, (), {}, {1}] 
# 1) print(e[2][3][3][1]) = 11

# 2) print(type(e[0]), type(e[1]), type(e[2]), type(e[3]), type(e[4]), type(e[5]), type(e[6])) =<class 'int'> <class 'str'> <class 'list'> <class 'builtin_function_or_method'> <class 'tuple'> <class 'dict'> <class 'set'>

# 3) print(e[0] + e[1]) = error인 이유? => 정수 타입과 str타입은 더할 수없어서




# < 2 >
a = [1,2,3,4,5,]
# 1) print(a[0:], a[:5]) = [1, 2, 3, 4, 5] [1, 2, 3, 4, 5]

# 2) print(type('12345'[0:2]), '12345'[0:2]) = <class 'str'> 12




# < 3 >
# 다차원슬라이싱 - 중첩된 list자료형의 슬라이싱
a = [1,2,3,['a','b','c'],4,5]
# 1) print(a[2:5]) = [3, ['a', 'b', 'c'], 4]

# 2) print(a[3:4]) = [['a', 'b', 'c']]

# 3) print(a[3:4][2]) = 무슨error? => index범위를 넘어섬




# < 4 >
a = [1,2,3]
a[1:2] = ['x', 'y', 'z']
# print(a) = [1, 'x', 'y', 'z', 3]




# < 5 >
sample = 'show how to index into sequences'.split()
# 1) print(sample[::2]) = ['show', 'to', 'into']

# 2) print(sample[::-2]) = ['sequences', 'index', 'how']




# < 6 >
c = ['x','z','y', 1,4,3,2]
c.sort() # int와 str사이에서 sort불가 => 에러 발생




# < 7 >
a = [1,2,'a',3,'a','b']
# 1) print(a.index('a', 3)) = 4

# 2) print(a.index('a', 3, 1000)) = 4




# < 8 >
a = [1,2,3,4]
# print(a.pop(), a) = 4 [1, 2, 3]




# < 9 >
a = [1,2,3]
# 1) a.append([4,5])
a.append([4,5])
# print(a) = [1, 2, 3, [4, 5]]

# 2) a.extend([4,5])
a.extend([4,5])
# print(a) = [1, 2, 3, [4, 5], 4, 5]

# 3) a.extend('hello')
a.extend('hello')
# print(a) = [1, 2, 3, [4, 5], 4, 5, 'h', 'e', 'l', 'l', 'o']

# 4) a.extend({'name':'홍길동', 'age':1000}) # dict 자료형, key만 확장
a.extend({'name':'홍길동', 'age':1000}) 
# print(a) = [1, 2, 3, [4, 5], 4, 5, 'h', 'e', 'l', 'l', 'o', 'name', 'age']
