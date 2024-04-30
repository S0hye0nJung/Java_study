<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
JSP 문제입니다! <br />

1. JSP로 "Hello, World!" 출력하기 <br />
<%out.println("Hello, World!"); %>
<br /><hr />





2. JSP에서 아래의 변수를 만들어서 사용하기("Hello,"는 html로 출력할 것) <br />
<%
String name = "John";
%>
Hello, <%=name %>!
<br /><hr />





3. 아래의 조건문을 JSP에서 사용하기<br />
<% boolean weather = true;
   if(weather) {
       out.print("우산을 가져가라");
   } else {
	
       out.print("우산을 가져가지마라");
   }%>
<br /><hr />





4. JSP에서 반복문(for 또는 while) 사용하기<br />
<%
for(int i=1; i<=5; i++) {%>
· item <% out.print(i);%> <br /><%}%>
<br /><hr />





5. JSP에서 아래의 배열  선언 후 for문으로 출력하기<br />
<%
String[] fruits = {"Apple", "Banana", "Orange"};

for(String fruit:fruits){
	%> . <%out.print(fruit);%>
	<br />
	<%
}
%>
<br /><hr />






6. JSP에서 아래의 함수(메서드) 정의하고 호출하기<br />
<%!
    int add(int a, int b) {
        return a + b;
    }
%> Result : <%=add(3, 5) %>
<br /><hr />






7. JSP에서 HTML 폼(form) 사용하기(이름, 주소, 취미를 입력 받고 출력하기(전송버튼 누르면 출력))<br />
  <h3>개인정보</h3>
	<form action="processForm.jsp" method="post">
	<table border="1">
		<tr>
			<td>이름</td>
			<td> <input type ="text" name ="name" size="20"/> </td>
			<td>주소</td>
			<td> <input type ="text" name ="address" size="20"/> </td>
			<td>이메일</td>
			<td> <input type ="text" name ="hobby" size="20"/> </td>
		</tr>
	</table>
	<input type="submit" value="전송" />
	</form>
<br /><hr />





8. JSP에서 예외 처리하기(try catch문을 사용하여 예외 처리하기)<br />
    <%
    try{
    	int result = 5 / 0;
    }catch(Exception e){
    	out.print("오류발생 : / by zero");
    }
    
    %>
    

    
</body>
</html>
