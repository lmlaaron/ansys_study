import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('data/nyc_taxi.csv',usecols=['pickup_x','pickup_y','dropoff_x', 'dropoff_y','passenger_count','tpep_pickup_datetime'])
plt.scatter(df.dropoff_x,df.dropoff_y)
plt.show()
