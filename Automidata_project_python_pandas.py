import pandas as pd
import numpy as np

df = pd.read_csv('2017_Yellow_Taxi_Trip_Data.csv')
print("done")

df.head(10)

df.info()

df.describe()

df_sorted = df.sort_values('trip_distance', ascending=False)
df_sorted.head(10)

df_sort = df.sort_values(['total_amount'], ascending=False)['total_amount']
df_sort.head(20)

df_sort.tail(20)

df['payment_type'].value_counts()

average_tip_credit = df[df['payment_type']==1]['tip_amount'].mean()
print(average_tip_credit)

average_tip_cash = df[df['payment_type']==2]['tip_amount'].mean()
print(average_tip_cash)

df['VendorID'].value_counts()

df.groupby('VendorID').mean()['total_amount']

credit_only = df[df['payment_type']==1]
credit_only

credit_only['passenger_count'].value_counts()

credit_only.groupby(['passenger_count']).mean()[['tip_amount']]
