# https://en.wikipedia.org/wiki/HTML 위의 사이트에서 각 종 태그를 불러오는 예제입니다~
import urllib.request as req
from bs4 import BeautifulSoup as bs
html = req.urlopen('https://en.wikipedia.org/wiki/HTML')
soup = bs(html, 'html.parser')


# 1. span 태그에서 'vector-dropdown-label-text' 클래스인 text 출력 - finsAll() or find_all() 사용
#     출력문
#     Main menu
#     Personal tools
#     Toggle the table of contents
#     133 languages
#     English
#     Tools
print('1번 답')
texts = soup.find_all('span', {'class':'vector-dropdown-label-text'})
for text in texts:
    print(text.string)
print()



# 2. 위의 출력문에서 'b'를 포함 한 text 출력 - if문 or for문 사용
#       출력문 - Toggle the table of contents
print('2번 답')
texts = soup.find_all('span', {'class':'vector-dropdown-label-text'})
for text in texts:
    if 'b' in text.string:
        print(text.string)
print()



# 3. 위의 출력문에서 'a'를 포함하지 않는 text 출력 - if문 or for문 사용
#       출력문 - English
#               Tools
print('3번 답')
texts = soup.find_all('span', {'class':'vector-dropdown-label-text'})
for text in texts:
    if 'a' not in text.string:
        print(text.string)
print()



# 4. html의 모든 클래스명에서 'vector' 가 포함된 모든 클래스명 출력
print('4번 답')
for tag in soup.find_all(class_=True):
    classes = tag.get('class')
    for clas in classes:
        if 'vector' in clas:
            print(clas)
print()



# 5. 위 출력문에서 15글자 이하인 text만 출력 - if문 작성
print('5번 답')
for tag in soup.find_all(class_=True):
    classes = tag.get('class')
    for clas in classes:
        if 'vector' in clas:
            if len(clas) <=15:
                print(clas)
