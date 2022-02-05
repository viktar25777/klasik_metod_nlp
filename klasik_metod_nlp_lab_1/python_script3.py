import numpy as np
import pandas as pd
df = pd.read_csv('data1.csv')
df['clean_tweet'] = df['clean_tweet'].str.lower()
df.to_csv('data1.csv')

