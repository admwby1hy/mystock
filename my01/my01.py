from mystock import *
import time

shanghai_df = get_shanghai_from_tushare()

starttime = time.process_time()
ndays  = 244 * 6                        #6年
history_pb_dif_dict = {}

startdate = '20181028'                  #从20181028开始买
#print(startdate)

i = 0
while ndays >= 10:
    tmpdate = strtodate(startdate,-(365*6 + 7 - i*25))
    tmpdf = shanghai_df[shanghai_df['trade_date']>=tmpdate]
    history_pb_dif_dict = get_ndays_average_pb_dif(tmpdf,ndays)

    stock_df = get_stock_df_from_tdx('510300')
    stock_df = stock_df[stock_df['trade_date']>=startdate]
    stock_df = stock_df.sort_values(by = 'trade_date',axis = 0,ascending = True).reset_index(drop=True)

    print(moni(history_pb_dif_dict,stock_df,ndays))

    ndays = ndays - 20
    i += 1
endtime = time.process_time()
print (endtime - starttime)

while 1==1:
    strndays = input("请输入pb均线天数:")
    if len(strndays) == 0:
        strndays = 488
    ndays = int(strndays)

    stockcode  = input("请输入证券代码:")
    if len(stockcode) == 0:
        stockcode = '510300'

    starttime = time.process_time()

    history_pb_dif_dict = {}


    history_pb_dif_dict = get_ndays_average_pb_dif(shanghai_df,ndays)
    
    stock_df = get_stock_df_from_tdx(stockcode)
    stock_df = stock_df[stock_df['trade_date']>=startdate]
    stock_df = stock_df.sort_values(by = 'trade_date',axis = 0,ascending = True).reset_index(drop=True)

    #print(['操作日期','PB-PB*','本次单价','本次买入金额','本次卖出金额','累计买入金额','累计卖出金额','股票剩余资产'])
    print(monimingxi(history_pb_dif_dict,stock_df,ndays))

    endtime = time.process_time()
    print (endtime - starttime)





