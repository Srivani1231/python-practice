import pandas as pd
data={"name":["srivani","anu"],
    "age":[20,31]
    }
df=pd.DataFrame(data)
df["marks"]=[85,90]
print(df)