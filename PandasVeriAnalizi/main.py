import pandas as pd
import numpy as np

data = np.random.randint(10,100,15).reshape(5,3)#100 den 10 a 15 sayı çıkar ve bunu 5 e 3 lük matrise çevirelim
df=pd.DataFrame(data,index=['a','c','e','f','h'],columns=['column1','column2','column3'])
df=df.reindex(['a','b','c','d','e','f','g','h'])
result=df

newColumn =[np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df["column4"] =newColumn

result=df.drop("column1",axis=1)#1. columnu siliyorum ve axis eğer 0 sa satır 1 ise kolonu sil
result=df.drop("a",axis=0)

result=df.isnull()#boş olmayan kısımlar false boş olan kısımlar true oluyor.
result=df.notnull()#buda üsttekinin tam tersi
result=df.isnull().sum()#her kolondaki ull değerleri saldır
result=df["column1"].isnull().sum()
print(result)
print(df)
