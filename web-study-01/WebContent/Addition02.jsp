<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Addition</title>
</head>
<body>

	<%
	int num1 = 20;
	int num2 = 10;
	int add = num1 + num2;
	%>
	
	<%= num1 %> + <%= num2 %> = <%= add %>
	
</body>
</html>