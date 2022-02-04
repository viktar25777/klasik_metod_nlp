import re
import numpy as np
import pandas as pd
import scipy
import sklearn
from sklearn.feature_extraction import DictVectorizer
df = pd.read_csv('data1.csv')
text = df['clean_tweet']
a = {'word-1': '@user'}, {'word-2': '@ '}
pattern = r'@[\w\b]*'
text = "{'user': '@user'}, {'clean_tweet': ''}"
b = re.findall(pattern, text)
c = re.sub(pattern, '', text)
print("text is ",text)
res = eval(text)
print(res)
d = a, res
vec = DictVectorizer()
f = c
print(f)
df.to_csv('data1.csv')

