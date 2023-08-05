import pymysql
import pandas as pd

import timeCh

class database:
    def __init__(self, code, name, database, time):
        self.code = code
        self.name = name
        self.time = time
        self.ipAddress = database[0]
        self.user = database[1]
        self.password = database[2]
        self.databaseName = database[3]
        self.conn = pymysql.connect(host=self.ipAddress, user=self.user, password=self.password, db=self.databaseName)
        self.cur = self.conn.cursor()

    def upload():
        pass

    def download(self):
        tch = timeCh.timeChange(self.time).timeDay()
        ytch = timeCh.timeChange(self.time).yesterdatTimeDay()
        mintch = str(tch[0][:4])+'-'+str(tch[0][4:6])+'-'+str(tch[0][6:8])+' '+str(tch[1][:2])+':'+str(tch[1][2:])
        newstch = str(tch[0][:4])+'.'+str(tch[0][4:6])+'.'+str(tch[0][6:8])+' '+str(tch[1][:2])+':'+str(tch[1][2:])

        sql1 = 'select * from daystockdata'
        self.cur.execute(sql1)
        dayResult = pd.DataFrame(
            columns=['id','종목코드','종목명','날짜','시가','고가','저가','종가','거래량'],
            data=self.cur.fetchall())
        dayResult.drop('id', axis=1, inplace=True)
        
        sql2 = 'select * from newsdata where date="'+str(newstch)+'"'
        self.cur.execute(sql2)
        newsResult = pd.DataFrame(
            columns=['id','날짜','제목','내용'],
            data=self.cur.fetchall())
        newsResult.drop('id', axis=1, inplace=True)
        
        sql3 = 'select * from minstockdata where date="'+str(mintch)+'"'
        self.cur.execute(sql3)
        minResult = pd.DataFrame(
            columns=['id','종목코드','종목명','날짜','시가','고가','저가','종가','거래량'],
            data=self.cur.fetchall())
        minResult.drop('id', axis=1, inplace=True)

        return (minResult, dayResult, newsResult)
    
    def allDataGet(self):
        sql1 = 'select * from daystockdata'
        self.cur.execute(sql1)
        dayResult = pd.DataFrame(
            columns=['id','종목코드','종목명','날짜','시가','고가','저가','종가','거래량'],
            data=self.cur.fetchall())
        dayResult.drop('id', axis=1, inplace=True)
        
        sql2 = 'select * from newsdata'
        self.cur.execute(sql2)
        newsResult = pd.DataFrame(
            columns=['id','날짜','제목','내용'],
            data=self.cur.fetchall())
        newsResult.drop('id', axis=1, inplace=True)
        
        sql3 = 'select * from minstockdata'
        self.cur.execute(sql3)
        minResult = pd.DataFrame(
            columns=['id','종목코드','종목명','날짜','시가','고가','저가','종가','거래량'],
            data=self.cur.fetchall())
        minResult.drop('id', axis=1, inplace=True)

        return (minResult, dayResult, newsResult)