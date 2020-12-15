
## Please check back with me on this -
## This is a work in progress. I hope to have it completed sometime in January 2021, but
## I wanted to get as much out as possible to demo a regression example.

#########################################################################################################
## This is the starting point for all of the regression programs contained in this project.
#########################################################################################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

########################################################
## Load df files with hourly time series df
########################################################

my_date_parser = lambda x:datetime.strptime( x,'%Y-%m-%d %H:%M:%S.%f' )

## This file has the actual meter reads in KWh
## This is what we're trying to predict
df = pd.read_csv( 'data/meter_reads_121997.csv', parse_dates=['start_date'], date_parser=my_date_parser )
## df = pd.read_csv( 'data/meter_reads_121997.csv', index_col=[0], parse_dates=['start_date'], date_parser=my_date_parser )

## This file has temperature in degrees Fahrenheit
df_temp = pd.read_csv( 'data/temperature_121997.csv', parse_dates=['start_date'], date_parser=my_date_parser )
## df_temp = pd.read_csv( 'data/temperature_121997.csv', index_col=[0], parse_dates=['start_date'], date_parser=my_date_parser )

## We will overwrite the 'df' dfframe by merging it with all of the regression variables
df = pd.merge( df, df_temp, on='start_date' )

## A few debug statement to see how things look...
## print( df.dtypes )
## print( df.head() )
## print( df.loc[:,['start_date','temperature']].head() )
## print( df.loc[:,['start_date','reading']].head() )


########################################################
## Do some preliminary data exploration and visualization
########################################################

## The beginning of the set is on a holiday
## TODO: splice dates based on querying start date column, use iloc to get readings
plt.scatter( df.loc[1000:1500,'start_date'], df.loc[1000:1500,'reading'] )
## plt.scatter( df.loc[1000:1500,'temperature'], df.loc[1000:1500,'reading'] )

plt.xticks()
plt.yticks()

plt.show()

########################################################
## Create training / cross validate / test sets
########################################################

## TODO...


########################################################
## Create the predictor model
########################################################

## regr_model = linear_model.LinearRegression()
## regr_model.fit( df.loc[:,['temperature']], df.loc[:,['reading']] )

