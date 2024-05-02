<!-- 세션생성과 세션닫기 파일 만들기- ???를 채워서 만들어주세요~! -->
<!-- session_info.jsp파일과 session_close.jsp파일 두 개를 만드시오 -->

///<session_info.jsp파일>//////////////////////////////////////////////
<%@page import="java.text.SimpleDateFormat"%>
<%@page import="java.util.Date"%>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@page session="true" %> <!-- JSP에서 세션 생성여부 -->
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<h3>Session</h3>
	<%
		Date time = new Date();
		SimpleDateFormat sdf = new ???("yyyy-MM-dd HH:mm:ss");
		time.???(session.getCreationTime()) ;
	%>
	1. Session Id = <%=session.getId() %> <br />
	2. Session 생성시간 = <%=sdf.format(???) %> <br />
	<% time.setTime(session.getLastAccessedTime()); %>
	3. Session 최종접속시간 = <%=sdf.format(time) %> <br />
</body>
</html>


















