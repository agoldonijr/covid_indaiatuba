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

plt.title("Curva Epidemiológica de Indaiatuba") 
plt.xlabel("Data")
plt.ylabel("Quantidade")
plt.annotate(confirmados[-1], xy=(1, confirmados[-1]), xytext=(8, 0), xycoords=('axes fraction', 'data'), textcoords='offset points')
plt.annotate(mortes[-1], xy=(1, mortes[-1]), xytext=(8, 0), xycoords=('axes fraction', 'data'), textcoords='offset points')
plt.plot_date(data,confirmados, marker='o',color="blue", ls="-", label='Confirmados')
plt.plot_date(data,mortes, marker='^', color='red', ls="-", label='Mortes')
plt.legend(loc="upper left")
plt.show()
