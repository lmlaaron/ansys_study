import pandas as pd
from bokeh.plotting import figure, output_file, show
import datashader as ds
from datashader import transfer_functions as tf
from datashader.colors import Greys9

df=pd.read_csv('data/nyc_taxi.csv',usecols=['pickup_x','pickup_y','dropoff_x', 'dropoff_y','passenger_count','tpep_pickup_datetime'])

NYC = x_range, y_range = ((-8242000,-8210000), (4965000,4990000))

plot_width  = int(750)
plot_height = int(plot_width//1.2)

Greys9_r = list(reversed(Greys9))[:-2]

cvs = ds.Canvas(plot_width=plot_width, plot_height=plot_height, x_range=x_range, y_range=y_range)
agg = cvs.points(df, 'dropoff_x', 'dropoff_y',  ds.count('passenger_count'))
img = tf.shade(agg, cmap=["white", 'darkblue'], how='linear')
