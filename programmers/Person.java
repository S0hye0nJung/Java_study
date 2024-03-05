package programmers;



public class Person {
	private String name;
    private int age;
    private String tel;
    
    
    
	public Person(String name, int age, String tel) {
		this.name = name;
		this.age = age;
		this.tel = tel;
	}
	
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public int getAge() {
		return age;
	}
	public void setAge(int age) {
		this.age = age;
	}
	public String getTel() {
		return tel;
	}
	public void setTel(String tel) {
		this.tel = tel;
	}
	@Override
	public String toString() {
		return "이름 : " + name + "/ 나이 : " + age + " / 전화번호 : " + tel;
	}
    


	
	/*
	 * 
>> 1 입력 시

=========== 정보 추가 ===========
이름 입력 : 홍길동
나이 입력 : 50
전화번호 입력 : 010-5656-5465

(입력 완료 후 메뉴창 다시 출력)
정보가 저장되었습니다.
============ MENU ===========
1>정보추가 / 2>정보삭제 / 3>전체정보 보기 / etc>종료

>> 3 입력 시

=========== 전체 정보 ===========
[이름 : 홍길동 / 나이 : 50 / 전화번호 : 010-6565-5465]
[이름 : 손흥민 / 나이 : 31 / 전화번호 : 010-5412-3518]
[이름 : 김민재 / 나이 : 27 / 전화번호 : 010-5487-4102]
============ MENU ===========
1>정보추가 / 2>정보삭제 / 3>전체정보 보기 / etc>종료

>> 2 입력 시

=========== 정보 삭제 ===========
삭제할 대상의 이름을 입력하세요 : 홍길동
삭제 완료
============ MENU ===========
1>정보추가 / 2>정보삭제 / 3>전체정보 보기 / etc>종료


- 조건 및 참고사항
  · Person class에는 멤버변수 및 getter and setter만 입력    
    private String name
    private int age
    private String tel
    getName setName, getAge setName, getTel setTel

  · PersonMain에는 메뉴 구현
    (메뉴창은 똑같이 구현할 필요는 없습니다)


※ 개발자 코멘트 : 이번주도 화이팅 :)
	 * 
	 */
	
	
	
	

}
