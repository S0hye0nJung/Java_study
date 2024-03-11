package programmers;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class PersonMain {

	//정보를 저장할 리스트 생성
	List<Person> list = new ArrayList<Person>();
	
public static void main(String[] args) {
	
		PersonMain personmain = new PersonMain();
		personmain.Info();
	

		}


public void Info() {
	System.out.println("============ MENU ===========\r\n"
			+ "1>정보추가 / 2>정보삭제 / 3>전체정보 보기 / etc>종료");

	//스위치문 case번호 직접 입력받기	
		Scanner sc = new Scanner(System.in);
		String i = sc.nextLine();
		
	//스위치문	
		switch(i) {
		case "1": addList(); break;	
		case "2": deleteInfo();break;
		case "3": showList();break;
			
		default: System.out.println("종료");
			
			}
}



//메소드들 만들기
public void addList() {
	System.out.println("=========== 정보 추가 ===========");
		Scanner sc = new Scanner(System.in);
		
	//이름 입력받기
		System.out.print("이름을 입력하세요");
		String name = sc.nextLine();
		
	//나이 입력받기
		System.out.print("나이를 입력하세요");
		int age = sc.nextInt();
	
	//전화번호 입력받기
		Scanner t = new Scanner(System.in);
		System.out.print("전화번호를 입력하세요");
		String tel = t.nextLine();
	
	//객체 생성
		Person person = new Person(name, age, tel);
	
	//정보 저장	
		list.add(person);
		System.out.println("정보가 저장되었습니다.");
	
	//보기 좋게 하기 위해서 간격띄우기
		System.out.println("\n");
	
	//다시 메뉴에서 선택하게 하기
		Info();
}
		

public void deleteInfo() {
		System.out.println("=========== 정보 삭제 ===========");
		System.out.print("삭제할 대상의 이름을 입력하세요 : ");
		Scanner sc = new Scanner(System.in);
		String name = sc.nextLine();
		
		for(int i =0; i< list.size();i++) {
			if(list.get(i).getName().equals(name)) {
				
				list.remove(i);
			}
		}
		
		System.out.println("삭제 완료");
		
	//보기 좋게 하기 위해서 간격띄우기
	System.out.println("\n\n");
		
	//다시 메뉴에서 선택하게 하기
		Info();
}


public void showList() {
	//리스트에 있는거 다 출력하기
	System.out.println("=========== 전체 정보 ===========");
	
	for(int i =0; i< list.size();i++) { 
		System.out.println("이름 : " + list.get(i).getName() +"/ 나이 : " +list.get(i).getAge() +"/ 전화번호 : " +list.get(i).getTel());
	
	}
		
	
	//보기 좋게 하기 위해서 간격띄우기
	System.out.println("\n");
	
	//다시 메뉴에서 선택하게 하기
			Info();
	
}






}


