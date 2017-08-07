import pandas as pd
import quandl

dataframe = quandl.get('WIKI/GOOGL')

# Print dataset
# print(df.head())

dataframe = dataframe[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]

# High-low
dataframe['HL'] = (dataframe['Adj. High'] - dataframe['Adj. Low']) / dataframe['Adj. Low']
# Change between opening and closing price
dataframe['change'] = (dataframe['Adj. Close'] - dataframe['Adj. Open']) / dataframe['Adj. Open']

dataframe = dataframe[['Adj. Close', 'HL', 'change', 'Adj. Volume']]

print(dataframe.head())
