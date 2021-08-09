import csv
import matplotlib.pyplot as plt

dates = []
rtns = []
prev = 0
with open('default_data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for i in reader:
        if prev == 0:
            prev = int(i['date'][14:16])
        else:
            if int(i['date'][14:16]) == prev + 1 or int(i['date'][14:16]) == 00 and prev == 59:
                pass
            else:
                print('')
                print(i)
                print(prev)
                print('')
        prev = int(i['date'][14:16])
        rtns.append(float(i['close']))

plt.plot(rtns)
plt.show()