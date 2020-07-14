# Copyright (C) 2020 Alcides Goldoni Junior <agoldonijr@gmail.com>

import csv
import matplotlib.pyplot as plt
import datetime
import pandas as pd

df  = pd.read_csv('./data')
df['data'] = pd.to_datetime(df['data'], utc=False, yearfirst=True, format="%Y-%m-%d")
df= df.resample('W-SUN', on='data').sum().reset_index().sort_values(by='data')

print(df)

df.plot(x='data', y='conf_dia', kind='bar',legend=None, title="Acumulados por semana")
plt.show()

