function memberAddBoxDown() { // 안보이는 영역에 숨어있던 멤버 추가하는 div영역 보이게끔 위치 변경
    document.getElementById('memberAddBoxDown').classList.add('AddBoxDown');
}

function memberAddBoxUp() { // 멤버 추가하는 div영역 안보이게끔 위치 변경
    document.getElementById('memberAddBoxDown').classList.remove('AddBoxDown');
}

function memberUpdateBoxDown() { // 안보이는 영역에 숨어있던 멤버정보 수정하는 div영역 보이게끔 위치 변경
    document.getElementById('memberUpdateBoxDown').classList.add('UpdateBoxDown');
}

function memberUpdateBoxUp() { // 멤버정보 수정하는 div영역 인보이게끔 위치 변경
    document.getElementById('memberUpdateBoxDown').classList.remove('UpdateBoxDown');
}



function usernm(){ // 멤버 추가하는 텍스트박스에 멤버 이름을 10글자 초과 입력시 경고메세지 표시
	const userName = document.getElementById('userNameCheck').value;
	if(userName.length > 10) {
		alert("유저 이름은 10글자 이상 작성이 불가능합니다.");
	}
}
function userphone(){ // 멤버 추가하는 텍스트박스에 멤버 전화번호를 13글자 초과 입력시 경고메세지 표시
	const userPhone = document.getElementById('userPhoneCheck').value;
	if(userPhone.length > 13) {
		alert("전화번호는 13글자 이상 작성이 불가능합니다.");
	}
}
function userAddress(){ // 멤버 추가하는 텍스트박스에 멤버 주소를 30글자 초과 입력시 경고메세지 표시
	const userAddress = document.getElementById('userAddressCheck').value;
	if(userAddress.length > 30) {
		alert("집주소는 30글자 이상 작성이 불가능합니다.");
	}
}
function userGroup(){ // 멤버 추가하는 텍스트박스에 멤버 그룹을 가족, 친구, 기타 외 입력시 경고메세지 표시
	const userGroup = document.getElementById('userGroupCheck').value;
	if(!(userGroup == "가족" || userGroup == "친구" || userGroup == "기타")) {
		alert("그룹은 가족, 친구, 기타 중에서 입력이 가능합니다.");
	}
}

function usernm2(){ // 멤버 추가하는 텍스트박스에 멤버 이름을 10글자 초과 입력시 경고메세지 표시
	const userName = document.getElementById('userNameCheck2').value;
	if(userName.length > 10) {
		alert("유저 이름은 10글자 이상 작성이 불가능합니다.");
	}
}
function userphone2(){ // 멤버 추가하는 텍스트박스에 멤버 전화번호를 13글자 초과 입력시 경고메세지 표시
	const userPhone = document.getElementById('userPhoneCheck2').value;
	if(userPhone.length > 13) {
		alert("전화번호는 13글자 이상 작성이 불가능합니다.");
	}
}
function userAddress2(){ // 멤버 추가하는 텍스트박스에 멤버 주소를 30글자 초과 입력시 경고메세지 표시
	const userAddress = document.getElementById('userAddressCheck2').value;
	if(userAddress.length > 30) {
		alert("집주소는 30글자 이상 작성이 불가능합니다.");
	}
}
function userGroup2(){ // 멤버 추가하는 텍스트박스에 멤버 그룹을 가족, 친구, 기타 외 입력시 경고메세지 표시
	const userGroup = document.getElementById('userGroupCheck2').value;
	if(!(userGroup == "가족" || userGroup == "친구" || userGroup == "기타")) {
		alert("그룹은 가족, 친구, 기타 중에서 입력이 가능합니다.");
	}
}