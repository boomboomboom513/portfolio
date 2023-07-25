import redis
import time
import pandas as pd

class dataSubPub:
    def __init__(self):
        self.address = redis.Redis(host='localhost', port=6388, db=0)

    def sub(self):
        print('[시스템]:64bit 환경으로부터 결과 데이터를 수신 대기중 입니다...')
        self.address.delete('actionChoose')
        while True:
            getData = self.address.get('actionChoose')
            if getData is not None:
                getData = getData.decode()
                print('[시스템]:64bit 환경으로부터 수신완료!')
                return getData
            time.sleep(0.1)

    def pub(self):
        print('[시스템]:64bit 환경에 업로드 완료 메세지 전송중...')
        self.address.set('uploadOkaySign', 'done')
        print('[시스템]:메세지 전송 완료!')

