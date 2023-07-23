import redis
import time
import pandas as pd

class dataSubPub:
    def __init__(self):
        self.address = redis.Redis(host='localhost', port=6388, db=0)

    def sub(self):
        print('[시스템]:32bit 환경으로부터 수신 대기중 입니다...')
        self.address.delete('uploadOkaySign')
        while True:
            getData = self.address.get('uploadOkaySign')
            if getData is not None:
                getData = getData.decode()
                print('[시스템]:32bit 환경으로부터 수신완료!')
                break
            time.sleep(0.1)

    def pub(self, action):
        print('[시스템]:32bit 환경에 결과 메세지 전송중...')
        if action == 0:
            self.address.set('actionChoose', '홀드')
        elif action == 1:
            self.address.set('actionChoose', '매수')
        elif action == 2:
            self.address.set('actionChoose', '매도')
        
        print('[시스템]:메세지 전송 완료!')