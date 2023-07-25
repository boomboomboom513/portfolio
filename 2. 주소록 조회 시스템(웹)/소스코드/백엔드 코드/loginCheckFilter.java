package com.member.diary.filter;

import java.io.IOException;
import javax.servlet.Filter;
import javax.servlet.FilterChain;
import javax.servlet.FilterConfig;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import javax.servlet.annotation.WebFilter;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

// 로그인한 회원만 이용할 수 있는 웹페이지 /memberdiary/diary로 이동하려고 시도할 시,
// 현재 session에 로그인한 회원 정보가 들어가 있는 상태인지 확인하기
@WebFilter("/memberdiary/diary")
public class loginCheckFilter implements Filter {
	
    public loginCheckFilter() {
    }

	public void init(FilterConfig fConfig) throws ServletException {
	}


	public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) 
		throws IOException, ServletException {
		
		HttpServletRequest req = (HttpServletRequest) request; // 다운캐스팅을 하여 request를 대입
		HttpServletResponse res = (HttpServletResponse) response; // 다운캐스팅 하여 response를 대입
		HttpSession session = req.getSession(); // request에 있는 session을 대입
		// 사용자에게 보내기전 코드 처리
		if(session.getAttribute("loginName") == null) {
			res.sendRedirect("/memberdiary/loginError");
		}
		chain.doFilter(req, res);
	}
}