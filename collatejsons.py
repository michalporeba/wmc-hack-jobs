import os, json, html
import pandas as pd
from glob import glob
from lxml import html as lxhtml

df = pd.concat([pd.read_json(f_name, lines=True) for f_name in glob('data/*.json')])


def strip_html(s):
    return str(lxhtml.fromstring(html.unescape(s)).text_content())

df.reset_index(drop=True, inplace=True)
#print(strip_html(df['description'].iloc[2]


df['description'] = df['description'].apply(lambda x: strip_html(x))
#df['description'].to_csv('OldDescriptions.csv', index=False)