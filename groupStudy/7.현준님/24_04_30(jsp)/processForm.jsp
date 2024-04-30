<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>개인정보 출력</title>
</head>
<body>
    <%
  		request.setCharacterEncoding("UTF-8");
        String name = request.getParameter("name");
        String address = request.getParameter("address");
        String hobby = request.getParameter("hobby");
    %>
    이름: <%= name %><br />
    주소: <%= address %><br />
    취미: <%= hobby %><br />
</body>
</html>
