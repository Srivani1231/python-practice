import pandas as pd
data={"name":["srivani","anu","rinky"],
    "age":[20,31,22]
    }
df=pd.DataFrame(data)
print(df[df["age"]>20])