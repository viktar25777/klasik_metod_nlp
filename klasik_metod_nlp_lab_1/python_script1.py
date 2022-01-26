import re
import html
import numpy as np
import pandas as pd
from html.parser import HTMLParser
from html import unescape
df = pd.read_csv('data1.csv')
df['clean_tweet']
my_string = df['clean_tweet']
def html_decode(s):
    htmlCodes = (
            ("'", '&#39;'),
            ('"', '&quot;'),
            ('>', '&gt;'),
            ('<', '&lt;'),
            ('&', '&amp;'))
    for code in htmlCodes:
        s = s.replace(code[1], code[0])
    return s

unescaped = html_decode(my_string)
print(unescaped)




