package com.member.diary.dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import org.springframework.stereotype.Repository;

import com.member.diary.dto.MemberDto;

@Repository
public class MemberDao {
	final String JDBC_DRIVER = "oracle.jdbc.driver.OracleDriver";
	final String JDBC_URL = "jdbc:oracle:thin:@localhost:1521:xe";
	
	public Connection open() {
		Connection conn = null;
		try {
			Class.forName(JDBC_DRIVER);
			conn = DriverManager.getConnection(JDBC_URL, "ora_user", "hong");
		} catch (ClassNotFoundException e) {
			e.printStackTrace();
		} catch (SQLException e) {
			e.printStackTrace();
		}
		return conn;
	}
	
	// 웹페이지에 회원 가입한 회원의 ID, 비밀번호, 이메일 정보를 모두 가져오기
	public List<MemberDto> getRegisterAll() throws Exception{
		Connection conn = open();
		List<MemberDto> memberList = new ArrayList<>();
		
		String sql = "SELECT * FROM register";
		PreparedStatement pstmt = conn.prepareStatement(sql);
		ResultSet rs = pstmt.executeQuery();
		
		try(conn; pstmt; rs) {
			while(rs.next()) {
				MemberDto mem = new MemberDto();
				mem.setRegister_id(rs.getString("register_id"));
				mem.setRegister_pw(rs.getString("register_pw"));
				mem.setRegister_email(rs.getString("register_email"));
				memberList.add(mem);
			}
		}
		return memberList;
	}
	
	// 각각 회원들이 추가한 멤버 정보를 모두 가져오기
	public List<MemberDto> getMemberDataAll() throws Exception{
		Connection conn = open();
		List<MemberDto> memberList = new ArrayList<>();
		
		String sql = "SELECT * FROM memberdiary";
		PreparedStatement pstmt = conn.prepareStatement(sql);
		ResultSet rs = pstmt.executeQuery();
		
		try(conn; pstmt; rs) {
			while(rs.next()) {
				MemberDto mem = new MemberDto();
				mem.setRegister_id(rs.getString("register_id"));
				mem.setMember_name(rs.getString("member_name"));
				mem.setPhone_number(rs.getString("phone_number"));
				mem.setAddress(rs.getString("address"));
				mem.setMember_group_no(rs.getString("member_group_no"));
				memberList.add(mem);
			}
		}
		return memberList;
	}
	
	// 새로 회원 가입한 회원의 계정 정보를 db에 추가할 때 사용
	public void registerAdd(MemberDto dto) throws Exception{
		Connection conn = open();
		
		String sql = "INSERT INTO register(register_id, register_pw, register_email) VALUES(?,?,?)";
		PreparedStatement pstmt = conn.prepareStatement(sql);
		
		try(conn; pstmt) {
			pstmt.setString(1, dto.getRegister_id());
			pstmt.setString(2, dto.getRegister_pw());
			pstmt.setString(3, dto.getRegister_email());
			pstmt.executeUpdate();
		}
	}
	
	// 회원이 새로 추가한 멤버 정보를 db에 추가할 때 사용
	public void MemberAdd(MemberDto dto) throws Exception{
		Connection conn = open();
		
		String sql = "INSERT INTO memberdiary(register_id, member_name, phone_number, address, member_group_no) VALUES(?,?,?,?,?)";
		PreparedStatement pstmt = conn.prepareStatement(sql);
		
		try(conn; pstmt) {
			pstmt.setString(1, dto.getRegister_id());
			pstmt.setString(2, dto.getMember_name());
			pstmt.setString(3, dto.getPhone_number());
			pstmt.setString(4, dto.getAddress());
			pstmt.setString(5, dto.getMember_group_no());
			pstmt.executeUpdate();
		}
	}
	
	// 기존에 있는 멤버 정보를 새로 수정하여 db에 기입할 때 사용
	public void MemberUpdate(MemberDto dto, String ChangeMemberPhoneNumber) throws Exception{
		Connection conn = open();
		
		String sql = "UPDATE memberdiary SET member_name=?, phone_number=?, address=?, member_group_no=? WHERE phone_number=?";
		PreparedStatement pstmt = conn.prepareStatement(sql);
		
		try(conn; pstmt) {
			pstmt.setString(1, dto.getMember_name());
			pstmt.setString(2, dto.getPhone_number());
			pstmt.setString(3, dto.getAddress());
			pstmt.setString(4, dto.getMember_group_no());
			pstmt.setString(5, ChangeMemberPhoneNumber);
			pstmt.executeUpdate();
		}
	}
	
	// 삭제를 원하는 멤버의 전화번호 정보를 db에 보내서 삭제를 완료
	public void MemberDel(String delMemberPhoneNumber) throws Exception{
		Connection conn = open();
		
		String sql = "DELETE FROM memberdiary WHERE phone_number=?";
		PreparedStatement pstmt = conn.prepareStatement(sql);
		
		try(conn; pstmt) {
			pstmt.setString(1, delMemberPhoneNumber);
			pstmt.executeUpdate();
		}
	}
}
