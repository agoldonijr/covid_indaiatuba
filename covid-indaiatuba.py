import csv
import matplotlib.pyplot as plt
import datetime



with open('./data') as csvfile:
    data = [] 
    confirmados = []
    mortes = []

    reader = csv.reader(csvfile, delimiter=',')
    next(reader)
    for row in reader:
        data.append( datetime.datetime.strptime(row[0], '%Y-%m-%d').date())
        confirmados.append(row[1])
        mortes.append(row[2])

plt.plot_date(data,confirmados, marker='o')
plt.plot_date(data,mortes, marker='^', color='red')
plt.show()
        
