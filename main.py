from ib_insync import *
import csv

ib = IB()

ib.connect('127.0.0.1', 4001, clientId=1)


def get_data(ticker='SPY', file='default_data.csv', window='2 M', barsize='1 min', num_window=2, end_date='20210101'):

    contract = Stock(ticker, exchange='SMART', currency='USD')

    bars = ib.reqHistoricalData(contract, endDateTime=f'{end_date} 00:00:00', durationStr=window,
            barSizeSetting=barsize, whatToShow='MIDPOINT', useRTH=True)

    df = util.df(bars)

    o = []
    h = []
    l = []
    c = []
    d = []
    for i in range(0, len(df['close'])):
        o.append(df['open'][i])
        h.append(df['high'][i])
        l.append(df['low'][i])
        c.append(df['close'][i])
        d.append(df['date'][i])