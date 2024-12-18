import pandas as pd
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
df = pd.read_csv('https://drive.google.com/uc?id=1zO8ekHWx9U7mrbx_0Hoxxu6od7uxJqWw&export=download')
df.rename(columns={'First Name':'Fname'})
print(df)
