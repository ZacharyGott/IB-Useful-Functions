import csv
import matplotlib.pyplot as plt

# dates = []
# rtns = []
# prev = 0
# with open('training_data.csv', 'r') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for i in reader:
#         if int(i['date'][10:13]) == 16:
#             print(i)
#         else:
#             rtns.append(i['close'])
#
# plt.plot(rtns)
# print(len(rtns))
# plt.show()

def remove_afterhours_data_csv(input_file, output_file):
    '''
        Function to remove after hours data
        that appears in older parts of IB data.
        May be sourced from Bloomberg.

        Returns a CSV of the clean data

        input_file : CSV file containing messy data
        output_file : CSV file to write clean data
    '''

    O = []
    H = []
    L = []
    C = []
    D = []
    with open(input_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for i in reader:
            if int(i['date'][10:13]) == 16:
                pass
            else:
                o = []
                h = []
                l = []
                c = []
                d = []

                o.append(float(i['open']))
                h.append(float(i['high']))
                l.append(float(i['low']))
                c.append(float(i['close']))
                d.append(i['date'])

                for n in range(0, len(o)):
                    O.append(o[n])
                    H.append(h[n])
                    L.append(l[n])
                    C.append(c[n])
                    D.append(d[n])

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(['open', 'high', 'low', 'close', 'date'])

        for i in range(0, len(O)):
            writer.writerow([O[i], H[i], L[i], C[i], D[i]])

remove_afterhours_data_csv('tday.csv', 'testing_data.csv')
