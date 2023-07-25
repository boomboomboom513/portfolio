<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>멤버 다이어리</title>
    <link href="/css/Css_MainPage.css" rel="stylesheet" type="text/css"/>
    <script src="/js/JS_MainPage.js"></script>
</head>
<body>
<!---------------------- 헤더 영역 ---------------------->
    <header>
        <div class="headerLogoArea">
            <img src="./images/Logo.png" class="headerLogoImage">
            <div class="headerLogoText" id="headerLogoTextVisible">
                <p>MEMBER DIARY</p>
                <p>DATA CENTER</p>
            </div>
        </div>
        <div class="headerMenuListBarArea" id="headerMenuListBarAreaPosition">
            <ul id="listUl">
                <li>HOME</li>
                <li>SERVICE</li>
                <li>CONTACT</li>
                <li>ABOUT</li>
            </ul>
        </div>

        <div class="headerSearchArea" id="headerLoginBtnAreaPosition">
            <div class="loginLogoutPosition">
                <p id="memcolor1">${memname}</p>
                <a href="/memberdiary/logout" id="memcolor2">${logout}</a>
                <button class="loginBtnStyle" onclick="loginSlideDown()">LOGIN</button>
            </div>
        </div>


        <div class="loginInsertAreaBox" id="loginInsertAreaBoxId">
            <div class="closeLoginArea">
                <button class="closeLoginbtn" onclick="loginSlideUp()">X</button>
            </div>
            <h1>로그인</h1>
            <form action="/memberdiary/login" method="post" class="dataInsertArea">
                <div class="dataSlotBox">
                    <div>
                        <p>Username</p>
                        <input type="text" name="register_id" placeholder="유저이름 입력" maxlength="30">
                        <img src="./images/loginMemberIcon.png">
                    </div>
                </div>
                <div class="dataSlotBox">
                    <div>
                        <p>Password</p>
                        <input type="text" name="register_pw" placeholder="비밀번호 입력" maxlength="30">
                        <img src="./images/loginLockIcon.png">
                    </div>
                </div>
                <div class="forgetpw">
                    <a href="#findPassword">비밀번호 찾기</a>
                </div>
                <button type="submit">로그인</button>
                <div class="goRegister">
                    <span>계정이 없으신가요? </span><span onclick="registerSlideDown()">회원가입</span>
                </div>
            </form>
        </div>


        <div class="registerAreaBox" id="registerAreaBoxId">
            <div class="closeLoginArea">
                <button class="closeLoginbtn" onclick="registerSlideUp()">X</button>
            </div>
            <h1>회원가입</h1>
            <form action="/memberdiary/register" method="post" class="dataInsertArea">
                <div class="dataSlotBox">
                    <div>
                        <p>Username</p>
                        <input type="text" id="userNameCheck" name="register_id" placeholder="회원 아이디 입력" maxlength="30" onblur="usernm()">
                        <img src="./images/loginMemberIcon.png">
                    </div>
                </div>
                <div class="dataSlotBox">
                    <div>
                        <p>Password</p>
                        <input type="text" id="userPassCheck" name="register_pw" placeholder="비밀번호 입력" maxlength="30" onblur="userpw()">
                        <img src="./images/loginLockIcon.png">
                    </div>
                </div>
                <div class="dataSlotBox">
                    <div>
                        <p>Email</p>
                        <input type="text" id="userEmailCheck" name="register_email" placeholder="이메일 입력" maxlength="40" onblur="userEmail()">
                        <img src="./images/loginMailIcon.png">
                    </div>
                </div>
                <div class="checkSlotBox">
                    <input type="checkbox">
                    <span>가입 조건 및 약관에 동의합니다</span>
                </div>
                <button type="submit">계정 등록</button>
            </form>
        </div>
    </header>



<!---------------------- 메인 영역 ---------------------->
    <main>
        <div class="mainIntroArea">
            <div class="introText" id="introTextvisi">
                <h1>MEMBER DIARY</h1>
                <p>MANAGE YOUR MEMBERSHIP INFORMATION USING THE TELEPHONE DIRECTORY SITE</p>
                <p>빅데이터 16기 JAVA SPRING을 이용한 3차 과제</p>
            </div>
            <img src="./images/intro.jpg">
        </div>
        <div class="mainPhotoArea1">
            <div class="mainPhotoArea1TextZone">
                <h1>BIG STORAGE</h1>
                <p>대규모 데이터베이스 서버 구축 및 빠른 인터넷 읽기 쓰기 속도</p>
            </div>
            <div class="mainPhotoArea1PhotoZone">
                <div class="text">
                    <h1>대규모 데이터 서버를</h1>
                    <h1>이용한 정보 관리</h1>
                    <h1>회원정보를 안전하고</h1>
                    <h1>편리하게 관리하세요</h1>
                    <br><br><br>
                    <p>MEMBERDIARY서버는 필요한 자원을</p>
                    <p>쉽고 빠르게 이용이 가능하며 사용한</p>
                    <p>만큼만 지불을 하는 서비스입니다.</p>
                    <p>서버 구축과 운영에 따라 언제든지</p>
                    <p>원하는 시점에 서버를 증감할 수 있고</p>
                    <p>자동확장이 가능한 오토스케일링 기능을</p>
                    <p>통해 유연하게 처리할 수 있어 높은</p>
                    <p>안정성을 확보 할 수 있습니다.</p>
                    <p>또한 무한한 확장성을 제공합니다.</p>
                    <a>더 보 기</a>
                </div>
                <div class="photo1">
                    <img src="./images/Photo1.jpg">
                </div>
                <div class="photo2">
                    <img src="./images/Photo2.jpg">
                </div>
            </div>
        </div>
        <%--<div class="mainPhotoArea2">
            사진영역2(아직 작업중)
        </div>--%>
        <div class="serviceArea">
            <div class="memberDataZone">
                <div>
                    <h1>회원 수</h1>
                    <h1 class="line">회원 평균 연령</h1>
                    <h1 class="line">서울 회원 수</h1>
                    <h1 class="line">하루 이용자</h1>
                    <p>32,231명</p>
                    <p class="line">36.2세</p>
                    <p class="line">25,695명</p>
                    <p class="line">18,734명</p>
                </div>
            </div>
            <div class="serviceTitleTextZone">
                <h1>SERVICE</h1>
                <p>MEMBER DIARY에서는 다양한 서비스를 제공합니다</p>
            </div>
            <div class="clickBtnZone">
                <div class="blocks bgimg1">
                    <a href="/memberdiary/diary"><p class="textSul">회원 조회</p></a>
                </div>
                <div class="blocks bgimg2">
                    <a href="/memberdiary/diary"><p class="textSul">회원 추가 및 수정</p></a>
                </div>
                <div class="blocks bgimg3">
                    <a href="/memberdiary/diary"><p class="textSul">회원 삭제</p></a>
                </div>
            </div>
        </div>
        <%--<div class="mainPhotoArea3">
            사진영역3(아직 작업중)
        </div>--%>
        <div class="cubeTitleTextArea">
            <h1>FUTURE ORIENTED</h1>
            <p>Member Diary Data Center는 미래를 바꿀 새로운 트렌드입니다.</p>
        </div>
        <div class="cubeArea">
            <div class="container">
                <div class="cube">
                    <div class="front1">
                    </div>
                    <div class="left">left</div>
                    <div class="right">
                        <h2>최상의 보안체계 설비</h2>
                        <p>기업들을 노리는 해킹공격</p>
                        <p>우리가 찾은 해법</p>
                        <p>해킹 대응 사이버 보안 시스템</p>
                        <br>
                        <p>엔터프라이즈급 악성코드</p>
                        <p>실시간 검사/관리 및 사전 방어</p>
                        <p>고객 데이터 및 서비스</p>
                        <p>다목적 서버까지</p>
                        <p>해킹 공격으로부터 보호</p>
                    </div>
                    <div class="back">back</div>
                    <div class="top">top</div>
                    <div class="bottom">bottom</div>
                </div>
                <div class="cubeSulText1">최상의 보안등급</div>
            </div>
            <div class="container">
                <div class="cube">
                    <div class="front2">
                    </div>
                    <div class="left">left</div>
                    <div class="right">
                        <h2>강력한 서비스 인프라</h2>
                        <p>빠르고 안전한 10G 이중화 네트워크</p>
                        <p>환경과 SSL, 방화벽, 모니터링</p>
                        <p>VPC등 클라우드 이용에 필요한</p>
                        <p>서비스를 ISMS를 획득한</p>
                        <p>인프라에서 제공합니다.</p>
                    </div>
                    <div class="back">back</div>
                    <div class="top">top</div>
                    <div class="bottom">bottom</div>
                </div>
                <div class="cubeSulText2">강력한 인프라</div>
            </div>
            <div class="container">
                <div class="cube">
                    <div class="front3">
                    </div>
                    <div class="left">left</div>
                    <div class="right">
                        <h2>고객 만족 기술지원</h2>
                        <p>스마일서브 정직원이 24시간 365일</p>
                        <p>서버 기술력을 서포트하고 운영에</p>
                        <p>도움을 드립니다.</p>
                        <p>또한 Linux, Windows의 다양한</p>
                        <p>종류와 docker등 응용 소프트웨어가</p>
                        <p>기본 탑재된 버전까지</p>
                        <p>선택할 수 있습니다.</p>
                    </div>
                    <div class="back">back</div>
                    <div class="top">top</div>
                    <div class="bottom">bottom</div>
                </div>
                <div class="cubeSulText3">고객 만족 기술지원</div>
            </div>
        </div>
    </main>



<!---------------------- 푸터 영역 ---------------------->
    <footer>
        <div class="jungTextAreaUp">
            <div class="smallArea1">
                <img id="footerIcon" src="./images/footerIcon.png">
                <p>간편하고 쉬운 회원 관리를</p>
                <p>보다 간편하게 이용하세요. </p>
                <p>많은 양의 저장 공간 제공.</p>
                <p>보기 쉬운 UI</p>
            </div>
            <div>
                <h2>Member Of Group</h2>
                <br>
                <p>1. 고범희</p>
                <p>2. 정승권</p>
                <p>3. 장하진</p>
                <p>4. 윤광현</p>
            </div>
            <div>
                <h2>Big Data 16기(주)</h2>
                <br>
                <p>수강생등록번호 456-72-12734</p>
                <p>대표이사 홍킬떵</p>
                <p>이메일 fuahjkf@gmail.com</p>
                <p>수강생등록정보 확인</p>
                <p>호스팅 서비스 제공 : 누군가의 톰켓서버</p>
            </div>
            <div>
                <h2>Contact Us</h2>
                <br>
                <p>서울특별시 강남구 역삼동 831-3 한국빌딩 4층 40X호</p>
                <p>웹페이지 디자인 오류신고 1234-1234</p>
                <p>전화 6575-7897</p>
                <a>1:1문의 바로가기</a>
            </div>
        </div>
        <div class="jungTextAreaDown">
            <div>
                <h2>구독과 좋아요 이메일 알림까지!!</h2>
                <p>매일 새로운 정보와 공지사항을 이메일로 받아보세요.</p>
            </div>
            <div class="rightArea">
                <input type="text" id="emailTextBox" placeholder="이메일">
                <button id="emailBtn"><img src="./images/SendEmailIcon.png"></button>
            </div>
        </div>
    </footer>
    ${msg}
</body>
</html>