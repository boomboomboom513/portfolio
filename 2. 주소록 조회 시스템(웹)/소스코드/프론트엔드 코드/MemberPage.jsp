<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <link href="/css/Css_MemberPage.css" rel="stylesheet" type="text/css"/>
    <script src="/js/JS_MemberPage.js"></script>
</head>
<body>
    <div class="backgroundshadow">
        <div class="memberAddBox" id="memberAddBoxDown">
        	<div class="topBoxArea">
	            <h2>멤버 추가</h2>
	            <button onclick="memberAddBoxUp()">X</button>
	        </div>
	        <form action="/memberdiary/diary/memAdd" method="post">
	            <div class="aaa">
	                <p>Username</p>
	                <input type="text" id="userNameCheck" name="member_name" placeholder="멤버 이름 입력" onblur="usernm()">
	            </div>
	            <div class="aaa">
	                <p>Telephone</p>
	                <input type="text" id="userPhoneCheck" name="phone_number" placeholder="멤버 전화번호 입력" onblur="userphone()">
	            </div>
	            <div class="aaa">
	                <p>Address</p>
	                <input type="text" id="userAddressCheck" name="address" placeholder="멤버 주소 입력" onblur="userAddress()">
	            </div>
	            <div class="aaa">
	                <p>Group</p>
	                <input type="text" id="userGroupCheck" name="member_group_no" placeholder="멤버 그룹명 입력" onblur="userGroup()">
	            </div>
	            <div class="memberAddBtn">
	                <button onclick="location.href='/memberdiary/diary/memAdd' ">멤버 추가</button>
	            </div>
        	</form>
        </div>
        <div class="memberUpdateBox ${style}" id="memberUpdateBoxDown">
        	<div class="topBoxArea">
	            <h2>멤버 수정</h2>
	            <button onclick="memberUpdateBoxUp()">X</button>
	        </div>
	        <form action="/memberdiary/diary/memUpdate" method="post">
	            <div class="aaa">
	                <p>Username</p>
	                <input type="text" id="userNameCheck2" name="member_name" placeholder="${unChangeName}" onblur="usernm2()">
	            </div>
	            <div class="aaa">
	                <p>Telephone</p>
	                <input type="text" id="userPhoneCheck2" name="phone_number" placeholder="${unChangePhoneNumber}" onblur="userphone2()">
	            </div>
	            <div class="aaa">
	                <p>Address</p>
	                <input type="text" id="userAddressCheck2" name="address" placeholder="${unChangeAddress}" onblur="userAddress2()">
	            </div>
	            <div class="aaa">
	                <p>Group</p>
	                <input type="text" id="userGroupCheck2" name="member_group_no" placeholder="${unChangeGroupName}" onblur="userGroup2()">
	            </div>
	            <div class="memberAddBtn">
	                <button onclick="location.href='/memberdiary/diary/memUpdate' ">수정 완료</button>
	            </div>
        	</form>
        </div>
        <div class="optionBox">
            <div class="interactionBox">
                <div class="memberLogoutArea">
                    <div></div>
                    <p>${memname}</p>
                    <a href="/memberdiary/logout">${logout}</a>
                </div>
                <div class="searchInteractionArea">
                    <button class="searchbtn" onclick="location.href='/memberdiary/diary/getall' ">
                    	전체 조회
                    </button>
                    <button class="searchbtn" onclick="memberAddBoxDown()">추가</button>
                    <form action="/memberdiary/diary/search" method="get">
                    	<div class="searchBoxArea">
	                        <input type="text" name="SearchName" placeholder="멤버 이름 검색">
	                        <button type="submit">검색</button>
	                    </div>
                    </form>
                </div>
                <div class="memberListArea">
                    <table>
                        <tr class="listTitle">
                            <th>순번</th>
                            <th>이름</th>
                            <th>전화번호</th>
                            <th>주소</th>
                            <th>그룹명</th>
                            <th colspan="2">수정/삭제</th>
                        </tr>
                        <c:forEach var="mem" items="${MemberList}" varStatus="status">
                        	<tr>
	                            <td>${status.count}</td>
	                            <td>${mem.member_name}</td>
	                            <td>${mem.phone_number}</td>
	                            <td>${mem.address}</td>
	                            <c:if test="${mem.member_group_no == 10}">
	                            	<td>가족</td>
	                            </c:if>
	                            <c:if test="${mem.member_group_no == 20}">
	                            	<td>친구</td>
	                            </c:if>
	                            <c:if test="${mem.member_group_no == 30}">
	                            	<td>기타</td>
	                            </c:if>
	                            <td onclick="location.href='/memberdiary/diary/memUpdateBox/${mem.phone_number}' ">수정</td>
	                            <td onclick="location.href='/memberdiary/diary/memdel/${mem.phone_number}' ">삭제</td>
	                        </tr>
                        </c:forEach>
                    </table>
                </div>
            </div>
        </div>
    </div>
    ${msg}
</body>
</html>