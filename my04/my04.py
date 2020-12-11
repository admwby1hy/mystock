
from mystock import *
import time

starttime = time.process_time()

pd.set_option('display.width', 1000)  # 设置字符显示宽度
pd.set_option('display.max_rows', None)  # 设置显示最大行

stockcode  = input("请输入证券代码:")
if len(stockcode) == 0:
    stockcode = '601398'

startdate = '20150710'
ndays = 440
justvalue = 0

df = monimingxi1(stockcode,startdate,ndays,justvalue)
df.to_csv(stockcode+'_result.csv',encoding='utf_8_sig')

endtime = time.process_time()
print (endtime - starttime)

