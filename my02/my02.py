
from mystock import *
import time

stockcode  = input("请输入证券代码:")
if len(stockcode) == 0:
    stockcode = '510300'

ms = mystock()
shanghai_df = ms.get_shanghai_from_tushare()

#print(ms.get_anystock_from_tushare('600000'))

starttime = time.process_time()
ndays  = 244 * 2                        #2年线
history_pb_dif_dict = {}

startdate = '20120528'                  #从20181028开始买
print(startdate)

starttime = time.process_time()

history_pb_dif_dict = {}

history_pb_dif_dict = ms.get_ndays_average_pb_dif(shanghai_df,ndays)
    
stock_df = ms.get_stock_df_from_tdx(stockcode)
stock_df = stock_df[stock_df['trade_date']>=startdate]
stock_df = stock_df.reset_index(drop=True)




d = 0.3
while d>-0.3:
    #print(['操作日期','PB-PB*','本次单价','本次买入金额','本次卖出金额','累计买入金额','累计卖出金额','股票剩余资产'])
    df = ms.monimingxi(history_pb_dif_dict,stock_df,ndays,d)
    if df.empty:
        d -= 0.01
        continue

    if (df.loc[len(df)-1]['累计买入金额'] - df.loc[len(df)-1]['累计卖出金额']) == 0:
        d -= 0.01
        continue 

    rate = df.loc[len(df)-1]['股票剩余资产']/(df.loc[len(df)-1]['累计买入金额'] - df.loc[len(df)-1]['累计卖出金额'])
    print('value= %.2f,累计净赚比例：%.2f' %(d,rate))
    d -= 0.01
    df = []
#df.to_csv('a.csv',encoding='utf_8_sig')

stock_df = ms.monimingxi(history_pb_dif_dict,stock_df,ndays,0.09)
stock_df.to_csv('a.csv',encoding='utf_8_sig')
print(stock_df)

endtime = time.process_time()
print (endtime - starttime)
