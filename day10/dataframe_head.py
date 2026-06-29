import pandas as pd
data={
    "name":["A","B","C","D","E"],
    "age":[20,30,23,25,55]
}
df=pd.DataFrame(data)
print(df.head(3))