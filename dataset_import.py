import pandas as pd


df = pd.read_csv("Students_Grading_Dataset.csv")  

print(df.head(10))
print(df.shape)
print(df.dtypes)