package com.member.diary.controller;

import java.util.ArrayList;
import java.util.List;
import javax.servlet.http.HttpSession;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;
import com.member.diary.dao.MemberDao;
import com.member.diary.dto.MemberDto;
import com.member.diary.service.MemberService;


@Controller
@RequestMapping("/memberdiary")
public class MemberWebController {
	private final Logger logger = LoggerFactory.getLogger(this.getClass());
	private String UpdateMemberPhoneNumber = "";
	MemberService service = new MemberService();
	MemberDao dao;
	
	@Autowired
	public MemberWebController(MemberDao dao) {
		this.dao = dao;
	}
	
	// 별다른 주소를 입력하지 않을 시 맨 처음에 보게되는 웹페이지로 이동, 로그인한 상태라면 로그인한 회원이름과 로그아웃 버튼 보이게 설정
	@GetMapping("")
	public String mainpage(Model model, HttpSession session) {
		if(session.getAttribute("loginName") != null) {
			model.addAttribute("memname", session.getAttribute("loginName")+"님");
			model.addAttribute("logout", "로그아웃");
		}
		return "mainpage";
	}
	
	// 아이디, 비밀번호 기입 후 로그인을 시도할 시, db안에 들어있는 가입된 사람들의 아이디와 비밀번호를 비교하여
	// 입력한 계정정보가 존재하는지 확인 후 로그인 완료 처리 또는 예외처리
	@PostMapping("/login")
	public String loginCheck(@ModelAttribute MemberDto memberDto, RedirectAttributes red, HttpSession session) {
		List<MemberDto> registerMem = null;
		
		if(session.getAttribute("loginName") == null) {
			try {
				registerMem = dao.getRegisterAll();
			} catch (Exception e) {
				logger.warn("회원정보 불러오기 실패");
			}
			
			for(int i = 0; i < registerMem.size(); i++) {
				if(registerMem.get(i).getRegister_id().equals(memberDto.getRegister_id()) && 
				   registerMem.get(i).getRegister_pw().equals(memberDto.getRegister_pw())) {
					session.setAttribute("loginName", registerMem.get(i).getRegister_id());
					red.addFlashAttribute("msg", "<script>alert('로그인 성공');</script>");
					red.addFlashAttribute("memname", session.getAttribute("loginName")+"님");
					red.addFlashAttribute("logout", "로그아웃");
					break;
				}else {
					red.addFlashAttribute("msg", "<script>alert('아이디 또는 비밀번호가 일치하지 않습니다.');</script>");
				}
			}
		}else {
			red.addFlashAttribute("msg", "<script>alert('로그아웃 후, 로그인 해주세요.');</script>");
			red.addFlashAttribute("memname", session.getAttribute("loginName")+"님");
			red.addFlashAttribute("logout", "로그아웃");
		}
		return "redirect:/memberdiary";
	}
	
	// 로그아웃 버튼 클릭할 시 session영역에 있는 로그인한 회원의 정보를 삭제, 메인 웹페이지로 이동처리
	@GetMapping("/logout")
	public String loginCheck(RedirectAttributes red, HttpSession session) {
		session.removeAttribute("loginName");
		red.addFlashAttribute("memname", null);
		red.addFlashAttribute("logout", null);
		red.addFlashAttribute("msg", "<script>alert('로그아웃');</script>");
		return "redirect:/memberdiary";
	}
	
	// 새로운 회원 가입시 입력한 계정정보를 db에 추가하고 완료 메시지 표시
	// Spring에서 예외처리를 구현하지 않고 AJAX를 이용하여 구현하려고 했는데 성공하지 못하였습니다ㅠㅠ
	@PostMapping("/register")
	public String loginCheck(@ModelAttribute MemberDto memberDto, RedirectAttributes red) {
		try {
			dao.registerAdd(memberDto);
			red.addFlashAttribute("msg", "<script>alert('회원가입을 완료하였습니다.');</script>");
		} catch (Exception e) {
			logger.warn("회원추가 오류 및 실패");
		}
		return "redirect:/memberdiary";
	}
	
	
//	MemberPage 관련 맵핑
	// 멤버 조회, 검색, 추가, 수정, 삭제를 할 수 있는 웹페이지로 이동하게끔 한다.(단, session에 로그인한 사람의 정보가 존재할 시)
	// 이동하게끔 처리하고, 그렇지 않을 경우 로그인한 상태가 아닌 것으로 판단하고 메인 페이지로 이동한다.
	@GetMapping("/diary")
	public String diarypage(Model model, HttpSession session) {
		if(session.getAttribute("loginName") != null) {
			model.addAttribute("memname", session.getAttribute("loginName")+"님");
			model.addAttribute("logout", "로그아웃");
		}
		return "MemberPage";
	}
	
	// 멤버 정보를 전부 조회할 때 해당 URL로 mapping을 받아서 db에서 멤버 정보를 모두 가져와서 보여준다.(로그인한 회원이 작성한 멤버 정보만 출력)
	@GetMapping("/diary/getall")
	public String memberGetAll(Model model, HttpSession session) {
		List<MemberDto> memberList;
		ArrayList<MemberDto> memberFilterList = new ArrayList<>();
		try {
			memberList = dao.getMemberDataAll();
			for(int i = 0; i < memberList.size(); i++) {
				if((session.getAttribute("loginName")).equals(memberList.get(i).getRegister_id())) {
					MemberDto mem = new MemberDto();
					mem.setMember_name(memberList.get(i).getMember_name());
					mem.setPhone_number(memberList.get(i).getPhone_number());
					mem.setAddress(memberList.get(i).getAddress());
					mem.setMember_group_no(memberList.get(i).getMember_group_no());
					memberFilterList.add(mem);
				}
			}
			model.addAttribute("MemberList", memberFilterList);
			model.addAttribute("memname", session.getAttribute("loginName")+"님");
			model.addAttribute("logout", "로그아웃");
		} catch (Exception e) {
			logger.warn("멤버 정보 전부 불러오기 오류 및 실패");
		}
		return "MemberPage";
	}
	
	// 특정 이름을 가진 멤버 정보를 조회할 때 해당 URL로 mapping을 받아서 db에서 멤버 정보를 모두 가져와서 
	// 검색한 멤버와 같은 이름을 가진 멤버 정보만 보여준다.(로그인한 회원이 작성한 멤버 정보만 출력)
	@GetMapping("/diary/search")
	public String memberSearch(@ModelAttribute MemberDto memberDto, Model model, HttpSession session) {
		List<MemberDto> memberList;
		ArrayList<MemberDto> memberFilterList = new ArrayList<>();
		ArrayList<MemberDto> memberSearchList = new ArrayList<>();
		try {
			memberList = dao.getMemberDataAll();
			for(int i = 0; i < memberList.size(); i++) {
				if((session.getAttribute("loginName")).equals(memberList.get(i).getRegister_id())) {
					MemberDto mem = new MemberDto();
					mem.setMember_name(memberList.get(i).getMember_name());
					mem.setPhone_number(memberList.get(i).getPhone_number());
					mem.setAddress(memberList.get(i).getAddress());
					mem.setMember_group_no(memberList.get(i).getMember_group_no());
					memberFilterList.add(mem);
				}
			}
			for(int i = 0; i < memberFilterList.size(); i++) {
				if((memberDto.getSearchName()).equals(memberFilterList.get(i).getMember_name())) {
					MemberDto mem = new MemberDto();
					mem.setMember_name(memberFilterList.get(i).getMember_name());
					mem.setPhone_number(memberFilterList.get(i).getPhone_number());
					mem.setAddress(memberFilterList.get(i).getAddress());
					mem.setMember_group_no(memberFilterList.get(i).getMember_group_no());
					memberSearchList.add(mem);
				}
			}
			model.addAttribute("MemberList", memberSearchList);
			model.addAttribute("memname", session.getAttribute("loginName")+"님");
			model.addAttribute("logout", "로그아웃");
		} catch (Exception e) {
			logger.warn("멤버 정보 전부 불러오기 오류 및 실패");
		}
		return "MemberPage";
	}
	
	// 로그인을 하지 않고 로그인 완료한 회원만 이용이 가능한 웹페이지로 이동을 하려고 시도 시, 이동이 불가능하게 예외처리
	@GetMapping("/loginError")
	public String loginError(RedirectAttributes red) {
		red.addFlashAttribute("msg", "<script>alert('해당 페이지는 로그인후 이용 가능합니다.');</script>");
		return "redirect:/memberdiary";
	}
	
	// 새로운 멤버 정보를 추가.(문자로 입력 받은 그룹명을 번호로 바꿔서 db에 추가)
	// AJAX를 이용해 예외 처리를 하려고 했으나 못했습니다.
	@PostMapping("/diary/memAdd")
	public String memberAdd(@ModelAttribute MemberDto memberDto, HttpSession session, RedirectAttributes red) {
		String changeType = String.valueOf(session.getAttribute("loginName"));
		memberDto.setRegister_id(changeType);
		
		if(memberDto.getMember_group_no().equals("가족")) {
			memberDto.setMember_group_no("10");
		}else if(memberDto.getMember_group_no().equals("친구")) {
			memberDto.setMember_group_no("20");
		}else if(memberDto.getMember_group_no().equals("기타")) {
			memberDto.setMember_group_no("30");
		}
		
		try {
			dao.MemberAdd(memberDto);
		} catch (Exception e) {
			logger.warn("멤버 정보 추가 에러");
		}
		red.addFlashAttribute("msg", "<script>alert('회원 추가 완료');</script>");
		return "redirect:/memberdiary/diary/getall";
	}
	
	// 수정을 하고 싶은 멤버 정보 옆에 있는 수정 버튼을 클릭 시, 해당 멤버 정보의 전화번호를 URL로 전송.
	// 새로 수정할 멤버의 정보를 가져와서 텍스트박스에 수정하기 전 데이터를 보여주기 위한 역활
	@GetMapping("/diary/memUpdateBox/{phone_number}")
	public String memberUpdateBox(@PathVariable String phone_number, RedirectAttributes red) {
		UpdateMemberPhoneNumber = phone_number;
		
		List<MemberDto> showUnchangeMember = new ArrayList<MemberDto>();
		try {
			showUnchangeMember = dao.getMemberDataAll();
		} catch (Exception e) {
			logger.warn("멤버 정보 불러오기 에러");
		}
		
		for(int i = 0; i < showUnchangeMember.size(); i++) {
			if(phone_number.equals(showUnchangeMember.get(i).getPhone_number())) {
				red.addFlashAttribute("unChangeName", showUnchangeMember.get(i).getMember_name());
				red.addFlashAttribute("unChangePhoneNumber", showUnchangeMember.get(i).getPhone_number());
				red.addFlashAttribute("unChangeAddress", showUnchangeMember.get(i).getAddress());
				if(showUnchangeMember.get(i).getMember_group_no().equals("10")) {
					red.addFlashAttribute("unChangeGroupName", "가족");
				}else if(showUnchangeMember.get(i).getMember_group_no().equals("20")) {
					red.addFlashAttribute("unChangeGroupName", "친구");
				}else if(showUnchangeMember.get(i).getMember_group_no().equals("30")) {
					red.addFlashAttribute("unChangeGroupName", "기타");
				}
			}
		}
		red.addFlashAttribute("style", "UpdateBoxDown");
		return "redirect:/memberdiary/diary/getall";
	}
	
	// 수정 완료 버튼을 클릭 시, 해당 멤버 정보의 전화번호를 URL로 전송. 
	// 새로 수정된 멤버 정보와 변경하기 전 전화번호를 db에 보내서 멤버 정보 변경
	@PostMapping("/diary/memUpdate")
	public String memberUpdate(@ModelAttribute MemberDto memberDto, RedirectAttributes red) {
		if(memberDto.getMember_group_no().equals("가족")) {
			memberDto.setMember_group_no("10");
		}else if(memberDto.getMember_group_no().equals("친구")) {
			memberDto.setMember_group_no("20");
		}else if(memberDto.getMember_group_no().equals("기타")) {
			memberDto.setMember_group_no("30");
		}
		
		try {
			dao.MemberUpdate(memberDto, UpdateMemberPhoneNumber);
		} catch (Exception e) {
			logger.warn("멤버 정보 업데이트 에러");
		}
		red.addFlashAttribute("msg", "<script>alert('회원 수정 완료');</script>");
		return "redirect:/memberdiary/diary/getall";
	}
	
	// 삭제하려는 멤버 정보 옆에 있는 삭제 버튼을 클릭시, 해당 멤버의 전화번호를 URL에 추가하여 전송
	// 해당 멤버의 전화번호를 db에 보내서 삭제를 완료
	@GetMapping("/diary/memdel/{phone_number}")
	public String memberDel(@PathVariable String phone_number, RedirectAttributes red) {		
		try {
			dao.MemberDel(phone_number);
			red.addFlashAttribute("msg", "<script>alert('회원 삭제 완료.');</script>");
		} catch (Exception e) {
			logger.warn("멤버 정보 삭제 에러");
		}
		return "redirect:/memberdiary/diary/getall";
	}
}