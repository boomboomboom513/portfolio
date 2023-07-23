import pandas as pd

class dataHap:
    def __init__(self, minDf, jipyoDf, newsScore):
        self.minDf = minDf
        self.jipyoDf = jipyoDf
        self.newsScore = newsScore

    def hap(self):
        self.minDf['SMA5'] = self.jipyoDf['SMA5'].iloc[0]
        self.minDf['SMA20'] = self.jipyoDf['SMA20'].iloc[0]
        self.minDf['UPPER'] = self.jipyoDf['UPPER'].iloc[0]
        self.minDf['MAVG'] = self.jipyoDf['MAVG'].iloc[0]
        self.minDf['LOWER'] = self.jipyoDf['LOWER'].iloc[0]
        self.minDf['RSI'] = self.jipyoDf['RSI'].iloc[0]
        self.minDf['MACD'] = self.jipyoDf['MACD'].iloc[0]
        self.minDf['AROONUP'] = self.jipyoDf['AROONUP'].iloc[0]
        self.minDf['AROONDN'] = self.jipyoDf['AROONDN'].iloc[0]
        self.minDf['news'] = self.newsScore

        return self.minDf