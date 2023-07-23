import win32com.client
import datetime as dt

import timeCh

class stockHTS:
    def __init__(self, action, timeNow):
        self.action = action
        self.instCpCybos = win32com.client.Dispatch('CpUtil.CpCybos')
        self.cpTradeUtil =  win32com.client.Dispatch("CpTrade.CpTdUtil")
        self.instCpTdNew5331A =  win32com.client.Dispatch("CpTrade.CpTdNew5331A")
        self.instCpTdNew5331B = win32com.client.Dispatch("CpTrade.CpTdNew5331B")
        self.instCpTd0311 = win32com.client.Dispatch("CpTrade.CpTd0311")
        self.timeNow = timeNow

    def buysell(self):
        self.cpTradeUtil.TradeInit()
        acc = self.cpTradeUtil.AccountNumber[0]
        accFlag = self.cpTradeUtil.GoodsList(acc, 1)

        timeCt = timeCh.timeChange(self.timeNow).timeDay()
        buysellTime = dt.datetime(int(timeCt[0][:4]), int(timeCt[0][4:6]), int(timeCt[0][6:8]), int(timeCt[1][:2]), int(timeCt[1][2:]))

        if self.action == '홀드':
            print('[시스템]:주식을 매수 또는 매도하지 않고 홀드하였습니다.')

        elif self.action == '매수':
            # 매수 코드
            self.instCpTd0311.SetInputValue(0,'2')
            self.instCpTd0311.SetInputValue(1,acc)
            self.instCpTd0311.SetInputValue(2,accFlag[0])
            self.instCpTd0311.SetInputValue(3,'A328130')
            self.instCpTd0311.SetInputValue(4,1)
            self.instCpTd0311.SetInputValue(8,'03') #01보통 03시장가 13최우선지정가
            self.instCpTd0311.BlockRequest()
            print('계좌명 : '+str(self.instCpTd0311.GetHeaderValue(1)))
            print('이름 : '+str(self.instCpTd0311.GetHeaderValue(9)))
            print('체결수량 : '+str(self.instCpTd0311.GetHeaderValue(4)))
            print('[시스템]:주식을 '+str(self.instCpTd0311.GetHeaderValue(4))+'주 매수 하였습니다.')
            self.instCpTdNew5331A.SetInputValue(0, acc)
            self.instCpTdNew5331A.BlockRequest()
            print('거래 가능한 계좌 잔액 : '+str(self.instCpTdNew5331A.GetHeaderValue(10))+'원')

            # 거래 시간, 종목명, 체결 수량, 거래 가능 계좌 금액, 거래 상태
            return (buysellTime.strftime('%Y-%m-%d %H:%M'), '루닛', int(self.instCpTd0311.GetHeaderValue(4)), int(self.instCpTdNew5331A.GetHeaderValue(10)), '매수')

        elif self.action == '매도':
            # 매도 코드
            self.instCpTd0311.SetInputValue(0,'1')
            self.instCpTd0311.SetInputValue(1,acc)
            self.instCpTd0311.SetInputValue(2,accFlag[0])
            self.instCpTd0311.SetInputValue(3,'A328130')
            self.instCpTd0311.SetInputValue(4,1)
            self.instCpTd0311.SetInputValue(8,'03')
            self.instCpTd0311.BlockRequest()
            print('계좌명 : '+str(self.instCpTd0311.GetHeaderValue(1)))
            print('이름 : '+str(self.instCpTd0311.GetHeaderValue(9)))
            print('체결수량 : '+str(self.instCpTd0311.GetHeaderValue(4)))
            print('[시스템]:주식을 '+str(self.instCpTd0311.GetHeaderValue(4))+'주 매도 하였습니다.')
            self.instCpTdNew5331A.SetInputValue(0, acc)
            self.instCpTdNew5331A.BlockRequest()
            print('거래 가능한 계좌 잔액 : '+str(self.instCpTdNew5331A.GetHeaderValue(10))+'원')

            # 거래 시간, 종목명, 체결 수량, 거래 가능 계좌 금액, 거래 상태
            return (buysellTime.strftime('%Y-%m-%d %H:%M'), '루닛', int(self.instCpTd0311.GetHeaderValue(4)), int(self.instCpTdNew5331A.GetHeaderValue(10)), '매도')