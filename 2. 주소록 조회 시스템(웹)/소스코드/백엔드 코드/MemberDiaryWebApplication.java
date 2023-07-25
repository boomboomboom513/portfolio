package com.member.diary;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.web.servlet.ServletComponentScan;

@ServletComponentScan // Filter기능을 사용하기 위해서 어노테이션 추가
@SpringBootApplication
public class MemberDiaryWebApplication {

	public static void main(String[] args) {
		SpringApplication.run(MemberDiaryWebApplication.class, args);
	}

}
