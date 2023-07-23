import talib
import pandas as pd

import timeCh

class jipyoCreate:
    def __init__(self, dayDf, time):
        self.dayDf = dayDf
        self.time = time

    def create(self):
        print('[시스템]:일 단위 데이터로 주식 지표 생성중...')

        upper, middle, lower = talib.BBANDS(self.dayDf['종가'], timeperiod=20)
        macd, macdsignal, macdhist = talib.MACD(self.dayDf['종가'], fastperiod=12, slowperiod=26, signalperiod=9)
        ar_up, ar_dn = talib.AROON(self.dayDf['고가'], self.dayDf['저가'], timeperiod=14)
        resultDf = pd.DataFrame({
            '종목코드':self.dayDf['종목코드'],
            '종목명':self.dayDf['종목명'],
            '날짜':self.dayDf['날짜'],
            'SMA5':talib.SMA(self.dayDf['종가'], timeperiod=5),
            'SMA20':talib.SMA(self.dayDf['종가'], timeperiod=10),
            'UPPER':upper,
            'MAVG':middle,
            'LOWER':lower,
            'RSI':talib.RSI(self.dayDf['종가'], timeperiod=14),
            'MACD':macd,
            'AROONUP':ar_up,
            'AROONDN':ar_dn
        })

        ytch = timeCh.timeChange(self.time).yesterdatTimeDay()
        jipyotch = str(ytch[0][:4])+'-'+str(ytch[0][4:6])+'-'+str(ytch[0][6:8])

        return resultDf[33:][resultDf['날짜'] == jipyotch]