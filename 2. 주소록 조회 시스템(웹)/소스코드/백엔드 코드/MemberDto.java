package com.member.diary.dto;

public class MemberDto {
	private String register_id; // 회원의 계정 id 값을 담아두는 변수
	private String register_pw; // 회원의 계정 비밀번호 값을 담아두는 변수
	private String register_email; // 회원의 계정 이메일 값을 담아두는 변수
	private String member_name; // 멤버 이름 값을 담아두는 변수
	private String phone_number; // 멤버 전화번호 값을 담아두는 변수
	private String address; // 멤버 주소 값을 담아두는 변수
	private String member_group_no; // 멤버 그룹번호 값을 담아두는 변수
	private String SearchName; // 검색하려는 멤버의 이름을 담아두는 변수
	
	public String getRegister_id() {
		return register_id;
	}
	public void setRegister_id(String register_id) {
		this.register_id = register_id;
	}
	public String getRegister_pw() {
		return register_pw;
	}
	public void setRegister_pw(String register_pw) {
		this.register_pw = register_pw;
	}
	public String getRegister_email() {
		return register_email;
	}
	public void setRegister_email(String register_email) {
		this.register_email = register_email;
	}
	public String getMember_name() {
		return member_name;
	}
	public void setMember_name(String member_name) {
		this.member_name = member_name;
	}
	public String getPhone_number() {
		return phone_number;
	}
	public void setPhone_number(String phone_number) {
		this.phone_number = phone_number;
	}
	public String getAddress() {
		return address;
	}
	public void setAddress(String address) {
		this.address = address;
	}
	public String getMember_group_no() {
		return member_group_no;
	}
	public void setMember_group_no(String member_group_no) {
		this.member_group_no = member_group_no;
	}
	public String getSearchName() {
		return SearchName;
	}
	public void setSearchName(String searchName) {
		SearchName = searchName;
	}
}