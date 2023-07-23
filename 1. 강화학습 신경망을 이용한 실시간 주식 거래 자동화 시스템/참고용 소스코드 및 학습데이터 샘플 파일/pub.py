import redis
import pandas as pd

address = redis.Redis(host='localhost', port=6388, db=0)

dataDf = pd.read_csv('./32bit/hapminstockdata/데이타솔루션 분 단위 주식 데이터.csv', encoding='euc-kr')

address.set('column', str(dataDf.columns.values))
address.set('value', str(dataDf[-1:].values))