
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
df = pd.read_csv( 'data/meter_reads_121997.csv', index_col=[0], parse_dates=['start_date'], date_parser=my_date_parser )

## This file has temperature in degrees Fahrenheit
df_temp = pd.read_csv( 'data/temperature_121997.csv', index_col=[0], parse_dates=['start_date'], date_parser=my_date_parser )

## We will overwrite the 'df' dfframe by merging it with all of the regression variables
df = pd.merge( df, df_temp, on='start_date' )

## A few debug statement to see how things look...
print( df.loc[:,['temperature']].head() )
## print( df.loc[:,['reading']].head() )
## print( type(df.loc[:,['reading']]) )

## print( df.loc[:,'temperature'].head() )
## print( df.columns )
## print( df.dtypes )
## print( df.head() )


########################################################
## Create training / cross validate / test sets
########################################################

## TODO...


########################################################
## Create the predictor model
########################################################

## regr_model = linear_model.LinearRegression()
## regr_model.fit( df.loc[:,'temperature'], df.loc[:,'reading'] )

