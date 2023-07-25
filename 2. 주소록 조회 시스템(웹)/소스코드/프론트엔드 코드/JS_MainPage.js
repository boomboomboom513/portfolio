window.addEventListener("scroll", (Event)=>{ // 웹페이지 스크롤 좌표값을 알아낼때 사용하는 이벤트 리스너
	// document를 통해 웹페이지에 있는 여러 태그들에 접근 및 지정
    let HeaderArea = document.querySelector('header');
    let HeaderTextColor = document.getElementById('listUl');
    let HeaderLogoImageScaleBig = document.querySelector('.headerLogoImage');
    let HeaderLogoImageScaleSmall = document.querySelector('.headerLogoImageSmall');
    let HeaderLogoText = document.querySelector('.headerLogoText');
    let HeaderLoginJungBo1 = document.getElementById('memcolor1');
    let HeaderLoginJungBo2 = document.getElementById('memcolor2');
    let headerMenuListBarAreaPosition = document.getElementById('headerMenuListBarAreaPosition');
    let headerLoginBtnAreaPosition = document.getElementById('headerLoginBtnAreaPosition');
    let introTextvisi = document.getElementById('introTextvisi');

    let scrollY = this.scrollY; // scrollY에 스크롤 좌표값을 대입
    if(scrollY > 0){ // 만약 웹페이지 영역 중 아래 영역으로 스크롤할 경우
        HeaderArea.classList.add('sticky'); // Header 태그 영역에 있는 모든 태그들에 position -> fixed 지정
        HeaderLogoImageScaleBig.classList.replace('headerLogoImage','headerLogoImageSmall');
        headerMenuListBarAreaPosition.style.marginTop = "26px"; // margin-top 위치를 26px로 지정
        HeaderLogoText.classList.add('hidden'); // header 부분 로고이미지 옆에 사이트 제목을 숨김처리
        HeaderTextColor.style.color = 'black'; // header 부분 문자 색상을 black으로 지정
        HeaderLoginJungBo1.style.color = 'black'; // header 부분 문자 색상을 black으로 지정
        HeaderLoginJungBo2.style.color = 'black'; // header 부분 문자 색상을 black으로 지정
        headerLoginBtnAreaPosition.style.paddingTop = "20px"; // header영역부분 줄어드는 것에 맞춰 로그인 버튼 위치 조정
        introTextvisi.style.opacity = "0"; // 웹페이지 배경에 뜨는 인트로 문자 투명도 0으로 처리하여 안보이게 처리 
    }else{ // 만약 스크롤을 웹페이지 맨 위로 끝까지 올릴경우 
        HeaderArea.classList.remove('sticky'); // Header 태그 영역에 있는 모든 태그들에 position -> fixed 해제
        HeaderLogoImageScaleSmall.classList.replace("headerLogoImageSmall","headerLogoImage");
        headerMenuListBarAreaPosition.style.marginTop = "56px"; // margin-top 위치를 56px로 지정
        HeaderLogoText.classList.remove('hidden'); // header 부분 로고이미지 옆에 사이트 제목 숨김처리한 것을 다시 보이게 처리 
        HeaderLoginJungBo1.style.color = 'white'; // header 부분 문자 색상을 white으로 지정
        HeaderLoginJungBo2.style.color = 'white'; // header 부분 문자 색상을 white으로 지정
        HeaderTextColor.style.color = 'white'; // header 부분 문자 색상을 white으로 지정
        headerLoginBtnAreaPosition.style.paddingTop = "50px"; // header영역부분 줄어드는 것에 맞춰 로그인 버튼 원래 위치로 조정
        introTextvisi.style.opacity = "1";  // 웹페이지 배경에 뜨는 인트로 문자 투명도 1으로 처리하여 보이게 처리 
    }
    console.log(scrollY); // 웹페이지 애니메이션 개발할때 스크롤 좌표값을 확인하기 위해 콘솔에 표시용으로 사용
});

function loginSlideDown(){ // 로그인 버튼 클릭시 숨어있던 로그인창 아래로 위치하게끔 해당 태그에 css 추가
    document.getElementById('loginInsertAreaBoxId').classList.add('loginInsertAreaBoxMove');
}
function loginSlideUp(){ // 로그인 버튼 클릭시 원래 숨어있던 곳으로 위치하게끔 해당 태그에 css 삭제
    document.getElementById('loginInsertAreaBoxId').classList.remove('loginInsertAreaBoxMove');
}

function registerSlideDown(){ // 회원가입 버튼 클릭시 원래 숨어있던 곳으로 위치하게끔 해당 태그에 css 추가
    document.getElementById('registerAreaBoxId').classList.add('registerAreaBoxMove');
    document.getElementById('loginInsertAreaBoxId').classList.remove('loginInsertAreaBoxMove');
}
function registerSlideUp(){ // 회원가입 버튼 클릭시 원래 숨어있던 곳으로 위치하게끔 해당 태그에 css 삭제
    document.getElementById('registerAreaBoxId').classList.remove('registerAreaBoxMove');
    document.getElementById('loginInsertAreaBoxId').classList.add('loginInsertAreaBoxMove');
}



function usernm(){ // 유저 이름을 입력하는 텍스트박스에 20글자 이상 작성시 경고 메세지 표시
	const userName = document.getElementById('userNameCheck').value;
	if(userName.length > 20) {
		alert("유저 이름은 20글자 이상 작성이 불가능합니다.");
	}
}
function userpw(){ // 비밀번호를 입력하는 텍스트박스에 20글자 이상 작성시 경고 메세지 표시
	const userPass = document.getElementById('userPassCheck').value;
	if(userPass.length > 20) {
		alert("비밀번호는 20글자 이상 작성이 불가능합니다.");
	}
}
function userEmail(){ // 이메일을 입력하는 텍스트박스에 30글자 이상 작성시 경고 메세지 표시
	const userEmail = document.getElementById('userEmailCheck').value;
	if(userEmail.length > 30) {
		alert("이메일은 30글자 이상 작성이 불가능합니다.");
	}
}