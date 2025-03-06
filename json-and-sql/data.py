import pandas as pd

df = pd.read_json('train.json')

dataframe= pd.read_json('https://api.exchangeratesapi.io/v1/latest?access_key=3087a6ccfede888ebca6b1419d2d1f11')

print(df)
print(dataframe)