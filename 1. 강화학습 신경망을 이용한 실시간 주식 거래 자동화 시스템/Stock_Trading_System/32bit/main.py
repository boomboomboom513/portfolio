import pandas as pd
import numpy as np
import datetime as dt
from glob import glob
from tqdm import tqdm
import win32com.client
import time

import stockapicheck
import filterstockcodename
import minstock
import daystock
import news
import stocknewsdataupload
import jipyo
import subpub32bit
import stockHTS

instCpCybos = win32com.client.Dispatch('CpUtil.CpCybos')
instCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")
StockChart = win32com.client.Dispatch("CpSysDib.StockChart")
instStockChart = win32com.client.Dispatch('CpSysDib.CpSvr7254')


stockNameList = ['루닛']
database = ['34.64.50.135','root','P@ssw0rd6388','stockdata']
stockNewsPage = 3  # 원하는 뉴스페이지 숫자 1 ~ 999페이지까지만 긁어오기 가능. # 원하는 페이지수까지에 1을 더해서 입력해야한다.

stockapicheck.daesin(instCpCybos, instCpStockCode).apiConnectCheck()
stockapicheck.daesin(instCpCybos, instCpStockCode).canTradeStockCount()
codeNameDf = stockapicheck.daesin(instCpCybos, instCpStockCode).getStockNameCode()
filterCodeNameDf = filterstockcodename.filterCodeName(stockNameList, codeNameDf).jongmokSerach()

timeNow = dt.datetime.now()
#timeNow = dt.datetime(2022,12,7,10,15)

# for i in range(filterCodeNameDf.shape[0]):
#     daystock.getDayData(StockChart, filterCodeNameDf['종목코드'][i], filterCodeNameDf['종목명'][i]).getjusik()

# for k in range(filterCodeNameDf.shape[0]):
#     stocknewsdataupload.upload(filterCodeNameDf['종목코드'][k], filterCodeNameDf['종목명'][k], database, timeNow).uploadDayStockData()

# 반복문 실행할 코드
while True:
    timeNow = dt.datetime.now()
    if 1520 >= timeNow.hour * 100 + timeNow.minute >= 900:
        for h in range(filterCodeNameDf.shape[0]):
            minstock.getMinData(StockChart, filterCodeNameDf['종목코드'][h], filterCodeNameDf['종목명'][h]).getjusik()

        for k in range(filterCodeNameDf.shape[0]):
            stocknewsdataupload.upload(filterCodeNameDf['종목코드'][k], filterCodeNameDf['종목명'][k], database, timeNow).uploadMinStockData()

        for j in range(filterCodeNameDf.shape[0]):
            news.getNews(filterCodeNameDf['종목코드'][j], filterCodeNameDf['종목명'][j], stockNewsPage, timeNow).getData()

        for k in range(filterCodeNameDf.shape[0]):
            stocknewsdataupload.upload(filterCodeNameDf['종목코드'][k], filterCodeNameDf['종목명'][k], database, timeNow).uploadNewsData()

        subpub32bit.dataSubPub().pub()
        resultAction = subpub32bit.dataSubPub().sub()
        tradeResult = stockHTS.stockHTS(resultAction, timeNow).buysell()

        stocknewsdataupload.upload('328130', '루닛', database, timeNow).uploadStockdata(tradeResult)

        timeNow = dt.datetime.now()
        print('[시스템]:'+str(timeNow.hour)+'시 '+str(timeNow.minute + 1)+'분이 되기 기다리는 중...')
        secondLeft = 60 - int(timeNow.second)
        time.sleep(secondLeft)
    else:
        print('[시스템]:현재 주식 거래 가능한 시간이 아닙니다. 현재시간 : '+str(timeNow.hour)+'시 '+str(timeNow.minute)+'분')
        time.sleep(1)
        continue