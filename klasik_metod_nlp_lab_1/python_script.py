import numpy as np
import pandas as pd
df1 = pd.read_csv('train_tweets.csv')
df2 = pd.read_csv('test_tweets.csv')
print(df1.head(), df2.head())
print(df1.dtypes, df2.dtypes)
print(df1.info(), df2.info())
df = pd.concat([df1, df2], ignore_index=True)
print(df)
df.to_csv('data.csv')

