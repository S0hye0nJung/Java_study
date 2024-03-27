################################  문제  ####################################
# 오늘 배운 파이썬으로 데이터베이스를 접속하고 조건별 출력 
# MySQLdb or sqlite3 사용
#데이터베이스 링크 =>./data/study.db
#데이터베이스 컬럼 id, name, age, addr
##데이터베이스 host = localhost / port= 3308 / db = study / users = root / password = 12345

#1. 조건 : name에 '영' 이라는 글자 그리고 age는 25이상인 데이터를 모두 출력
#2. 조건 :나이가 20세에서 30세 사이이고 주소가 '서울' 또는 '부산'인 사용자를 검색하며, 그 결과를 나이를 기준으로 내림차순으로 정렬하기

#####################################################################
#데이터베이스가 없기 떄문에 임시로 있다고 생각해서 오늘 배운 파이썬 코드 활용하면서 복습한다는 개념으로 코드 작성하기!!
# 2개의 코드가 나와야합니다.    // 메서드를 만들어서 작성

################################  풀이  ####################################
#조건1
import sqlite3

def mysql():
    conn = MySQLdb.connect(host='localhost',port='3308',db='study',user='root',password='12345')
    cursor = conn.connect()

    sql =  "SELECT id, name, age, addr FROM study WHERE name LIKE '%영%' AND age >= 25"
    cursor.execute(sql)

    names = cursor.fetchall()

    ##출력문
    for name in names:
        print(name)

cursor.close()
conn.close()


#조건2
# 나이가 20세에서 30세 사이이고 주소가 '서울' 또는 '부산'인 사용자를 검색하며, 그 결과를 나이를 기준으로 내림차순으로 정렬하기
import sqlite3

conn = sqlite3.connect('./data/study.db')
cursor = conn.cursor()


sql = "SELECT id, name, age, addr FROM study WHERE age BETWEEN ? AND ? AND addr IN (?, ?) ORDER BY age DESC"

cursor.execute(sql, (20,30,'서울','부산'))
ages = cursor.fetchall()

##출력문
for age in ages:
    print(age)

cursor.close()
conn.close()  
