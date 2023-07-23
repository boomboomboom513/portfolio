# 리눅스에 설치된 마리아DB에 데이터 전송
import pymysql
import pandas as pd
import datetime as dt
from tqdm import tqdm

import timeCh

class upload:
    def __init__(self, code, name, database, timeNow):
        self.code = code
        self.name = name
        self.timeNow = timeNow
        self.ipAddress = database[0]
        self.user = database[1]
        self.password = database[2]
        self.databaseName = database[3]
    
    def uploadMinStockData(self):
        loadMinStockData = pd.read_csv('./minstockdata/'+str(self.name)+' 분 단위 주식 데이터.csv', encoding='euc-kr')
        loadMinStockDataCp = loadMinStockData.copy()
        
        chtl = []
        for i in range(loadMinStockDataCp.shape[0]):
            changeTime = dt.datetime(int(str(loadMinStockDataCp['날짜'][i])[:4]), int(str(loadMinStockDataCp['날짜'][i])[4:6]), int(str(loadMinStockDataCp['날짜'][i])[6:8]), int(str(loadMinStockDataCp['시간'][i] // 100)), int(str(loadMinStockDataCp['시간'][i] % 100)))
            chtl.append(changeTime.strftime('%Y-%m-%d %H:%M'))
        loadMinStockDataCp['날짜'] = chtl

        conn = pymysql.connect(host=self.ipAddress, user=self.user, password=self.password, db=self.databaseName)
        cur = conn.cursor()

        timeDay = timeCh.timeChange(self.timeNow).timeDay()

        if str(loadMinStockDataCp['날짜'][0]) == str(chtl[0]):
            print('[시스템]:당일 현재 시간 '+str(self.name)+' 종목 분 단위 주식 데이터 마리아DB에 업로드 중...')
            sql = 'insert into minstockdata'+' (code,name,date,startprice,highprice,lowprice,endprice,tradecount)'+' values (%s, %s, %s, %s, %s, %s, %s, %s)'

            for i in range(0, loadMinStockDataCp.shape[0]):
                cur.execute(sql, (loadMinStockDataCp['종목코드'][i],loadMinStockDataCp['종목명'][i],loadMinStockDataCp['날짜'][i], loadMinStockDataCp['시가'][i]
                                ,loadMinStockDataCp['고가'][i],loadMinStockDataCp['저가'][i],loadMinStockDataCp['종가'][i],loadMinStockDataCp['거래량'][i]))
            conn.commit()
            print('[시스템]:당일 현재 시간 '+str(self.name)+' 종목 분 단위 주식 데이터 마리아DB에 업로드 완료!')
        else:
            print('[시스템]:당일 현재 시간 '+str(self.name)+' 종목의 분 단위 주식 거래된 데이터가 없어서 마리아DB에 업로드 불가!')

    def uploadDayStockData(self):
        loadDayStockData = pd.read_csv('./daystockdata/'+str(self.name)+' 일 단위 주식 데이터.csv', encoding='euc-kr')
        loadDayStockDataCp = loadDayStockData.copy()

        chtl = []
        for i in range(loadDayStockDataCp.shape[0]):
            changeTime = dt.datetime(int(str(loadDayStockDataCp['날짜'][i])[:4]), int(str(loadDayStockDataCp['날짜'][i])[4:6]), int(str(loadDayStockDataCp['날짜'][i])[6:8]))
            chtl.append(changeTime.strftime('%Y-%m-%d %H:%M'))
        loadDayStockDataCp['날짜'] = chtl

        conn = pymysql.connect(host=self.ipAddress, user=self.user, password=self.password, db=self.databaseName)
        cur = conn.cursor()

        timeDay = timeCh.timeChange(self.timeNow).yesterdatTimeDay()

        if str(loadDayStockDataCp['날짜'][1]) == str(chtl[1]):
            print('[시스템]:당일 현재 시간 '+str(self.name)+' 종목 일 단위 주식 데이터 마리아DB에 업로드 중...')
            sql = 'insert into daystockdata'+' (code,name,date,startprice,highprice,lowprice,endprice,tradecount)'+' values (%s, %s, %s, %s, %s, %s, %s, %s);'
            
            for i in range(1, loadDayStockDataCp.shape[0]):
                cur.execute(sql, (loadDayStockDataCp['종목코드'][i],loadDayStockDataCp['종목명'][i],loadDayStockDataCp['날짜'][i],loadDayStockDataCp['시가'][i]
                                ,loadDayStockDataCp['고가'][i],loadDayStockDataCp['저가'][i],loadDayStockDataCp['종가'][i],loadDayStockDataCp['거래량'][i]))
            conn.commit()
            print('[시스템]:당일 현재 시간 '+str(self.name)+' 종목 일 단위 주식 데이터 마리아DB에 업로드 완료!')
        else:
            print('[시스템]:당일 현재 시간 '+str(self.name)+' 종목의 일 단위 주식 거래된 데이터가 없어서 마리아DB에 업로드 불가!')

    def uploadNewsData(self):
        loadNewsData = pd.read_csv('./newsdata/'+str(self.name)+' 뉴스 데이터.csv', encoding='utf-8')

        conn = pymysql.connect(host=self.ipAddress, user=self.user, password=self.password, db=self.databaseName)
        cur = conn.cursor()

        timeDay = timeCh.timeChange(self.timeNow).timeDay()

        print('[시스템]:전날까지의 '+str(self.name)+' 종목의 뉴스 데이터 마리아DB에 업로드 중...')
        for i in tqdm(range(loadNewsData.shape[0])):
            day = str(loadNewsData['날짜'][i].strip()[:4])+str(loadNewsData['날짜'][i].strip()[5:7])+str(loadNewsData['날짜'][i].strip()[8:10])
            if str(day) == str(timeDay[0]):
                print('[시스템]:당일 현재 시간 '+str(self.name)+' 종목 뉴스 데이터 마리아DB에 업로드 중...')
                sql = 'insert into newsdata'+' (date,title,text)'+' values (%s, %s, %s);'
                cur.execute(sql, (loadNewsData['날짜'][i],loadNewsData['제목'][i],loadNewsData['내용'][i]))
                conn.commit()
        print('[시스템]:당일 현재 시간 '+str(self.name)+' 종목 뉴스 데이터 마리아DB에 업로드 완료!')
    
    def uploadjipyoData(self):
        loadJipyoData = pd.read_csv('./jipyo/'+str(self.name)+' 지표 데이터.csv', encoding='euc-kr')

        conn = pymysql.connect(host=self.ipAddress, user=self.user, password=self.password, db=self.databaseName)
        cur = conn.cursor()

        timeDay = timeCh.timeChange(self.timeNow).timeDay()

        sql1 = 'truncate stockjipyo;'
        cur.execute(sql1)
        conn.commit()

        print('[시스템]:전날까지의 '+str(self.name)+' 종목의 지표 데이터 마리아DB에 업로드 중...')
        for i in tqdm(range(loadJipyoData.shape[0])):
            sql2 = 'insert into stockjipyo'+' (code,name,date,sma5,sma20,upper,mavg,lower,rsi,macd,aroonup,aroondn)'+' values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);'
            cur.execute(sql2, (loadJipyoData['종목코드'][i],loadJipyoData['종목명'][i],loadJipyoData['날짜'][i],loadJipyoData['SMA5'][i],loadJipyoData['SMA20'][i],loadJipyoData['UPPER'][i]\
                                 ,loadJipyoData['MAVG'][i],loadJipyoData['LOWER'][i],loadJipyoData['RSI'][i],loadJipyoData['MACD'][i],loadJipyoData['AROONUP'][i],loadJipyoData['AROONDN'][i]))
        conn.commit()
        print('[시스템]:전날까지의 '+str(self.name)+' 종목 지표 데이터 마리아DB에 업로드 완료!')

    def uploadStockdata(stockdataTuple):
        print('[시스템]:'+str(stockdataTuple[1])+' 종목의 주식 거래 정보 마리아DB에 업로드 중...')

        conn = pymysql.connect(host='34.64.50.135', user='root', password='P@ssw0rd6388', db='stockdata')
        cur = conn.cursor()

        sql = 'insert into stockrecord'+' (date,name,stockcount,money,tradeaction)'+' values (%s, %s, %s, %s, %s);'
        cur.execute(sql, (stockdataTuple[0], stockdataTuple[1], stockdataTuple[2], stockdataTuple[3], stockdataTuple[4]))
        conn.commit()

        print('[시스템]:'+str(stockdataTuple[1])+' 종목의 주식 거래 정보 마리아DB에 업로드 완료!!')

