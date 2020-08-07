# Copyright (C) 2020 Alcides Goldoni Junior <agoldonijr@gmail.com>

import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates

df  = pd.read_csv('./data', parse_dates=[0])
df = df.resample('W-SUN', on='data').sum()

#print(df)

fig, ax = plt.subplots()
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
ax.bar(df.index, df['conf_dia'], width=5, align='center')
plt.title("Confirmados por semana")
plt.xlabel("Data")
plt.ylabel("Quantidade")
plt.show()
