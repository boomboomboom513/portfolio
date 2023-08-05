from keras.models import load_model
import pandas as pd
import random
import warnings
warnings.filterwarnings('ignore')

class rl:
    def __init__(self, dataDf):
        self.dataDf = dataDf
        self.maxClose = 200500
        self.minClose = 18900

    def dp(self):
        print('[시스템]:실시간 주가 데이터를 기준으로 탐험을 진행 중입니다.')
        result = []
        if self.maxClose >= self.dataDf['종가'] >= self.minClose:
            lstmLoad = load_model('./lstm.hdf5')
            resul = round(lstmLoad.predict(self.dataDf), 1)
            result.append(resul)
        else:
            result.append(random.randrange(0,2))

        travel = pd.read_csv('./travelReward.csv', encoding='euc-kr')
        travel.loc[travel.shape[0] + 1] = [self.dataDf['종가'], result]
        travel.to_csv('./travelReward.csv', encoding='euc-kr', index=False)

        return result

    def reinforce():
        print('[시스템]:탐험한 결과에 reward 부여중...')
        rewardList = 0
        travel = pd.read_csv('./travelReward.csv', encoding='euc-kr')

        for i in range(travel.shape[0] - 1):
            if travel['종가'][i] > travel['종가'][i+1]:
                rewardList -= 1
            elif travel['종가'][i] < travel['종가'][i+1]:
                rewardList += 1
            else:
                rewardList += 0
        
        return rewardList
    
    def training(self, reward):
        if reward >= 0 or reward <= 0:
            print('[시스템]:탐험한 결과를 신경망에 업데이트 중입니다...')
            lstmLoad = load_model('./lstm.hdf5')
            lstmLoad.fit(self.dataDf)