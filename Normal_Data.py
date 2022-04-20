from ib_insync import *
import csv

ib = IB()

ib.connect('127.0.0.1', 4001, clientId=1)


def get_data(ticker='SPY', file='default_data.csv', window='1 M', barsize='1 min', num_window=2, end_date='20211018 09:30:00'):

    contract = Stock(ticker, exchange='SMART', currency='USD')

    O = []
    H = []
    L = []
    C = []
    D = []

    for i in range(0, num_window):

        bars = ib.reqHistoricalData(contract, endDateTime=end_date, durationStr=window,
                barSizeSetting=barsize, whatToShow='MIDPOINT', useRTH=True)

        df = util.df(bars)

        o = []
        h = []
        l = []
        c = []
        d = []
        for z in range(0, len(df['close'])):
            o.append(df['open'][z])
            h.append(df['high'][z])
            l.append(df['low'][z])
            c.append(df['close'][z])
            d.append(df['date'][z])

        o.reverse()
        h.reverse()
        l.reverse()
        c.reverse()
        d.reverse()

        for n in range(0, len(o)):
            O.append(o[n])
            H.append(h[n])
            L.append(l[n])
            C.append(c[n])
            D.append(d[n])


        end_date = d[-1]
        print(f'{i+1} / {num_window}')
        print(end_date)



    with open(file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(['open', 'high', 'low', 'close', 'date'])

        for i in range(0, len(O))[::-1]:
            writer.writerow([O[i], H[i], L[i], C[i], D[i]])



get_data(file='tday.csv', num_window=36, ticker='VIX')