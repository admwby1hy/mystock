from mystock import *
import time

pd.set_option('display.width', 1000)  # 设置字符显示宽度
pd.set_option('display.max_rows', None)  # 设置显示最大行


stockcode  = input("请输入证券代码:")
if len(stockcode) == 0:
    stockcode = '601398'

if stockcode[0:1] == '5':
    stockdf = get_shanghai_from_tushare()
else:
    stockdf = get_anystock_from_tushare(stockcode)

history_pb_dif_dict = {}
moni_list = []

starttime = time.process_time()

stock_df = get_stock_df_from_tdx(stockcode)


startdate = '20151106'

ndays  = 244 * 5
while ndays>=1130:
    
    history_pb_dif_dict = get_ndays_average_pb_dif_from_tushare(stockdf,ndays)

    startdate = history_pb_dif_dict['0']                 #从20181028开始买
    #while startdate<='20151106':

    tmpstock_df = stock_df[stock_df['trade_date']>=startdate]
    tmpstock_df = tmpstock_df.reset_index(drop=True)


    d = 0.01
    while d>=-0.01:
        tmplist = moni(history_pb_dif_dict,tmpstock_df,ndays,round(d,2))

        if not tmplist:
            d -= 0.01
            continue

        moni_list.append(tmplist)
        
        #if (df.loc[len(df)-1]['累计买入金额'] - df.loc[len(df)-1]['累计卖出金额']) == 0:
        #    d -= 0.01
        #    continue  
 
        d -= 0.01

    #    startdate = strtodate(startdate,30)

    ndays -= 10

tmpdf = pd.DataFrame(data=moni_list,columns=['ndays','justvalue','累计买入金额','累计卖出金额','股票剩余资产','开始日期','结束日期','IRR'])
tmpdf.to_csv(stockcode+'综合结果'+'.csv',encoding='utf_8_sig')
endtime = time.process_time()
print (endtime - starttime)


"""


tmpdf = pd.DataFrame(data=moni_list,columns=['ndays','justvalue','累计买入金额','累计卖出金额','股票剩余资产','开始日期','结束日期','IRR'])
tmpdf.to_csv(stockcode+'综合结果'+'.csv',encoding='utf_8_sig')
endtime = time.process_time()
print (endtime - starttime)
"""




