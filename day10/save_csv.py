import pandas as pd
data={
    "name":["srivani","anu","rinky"],
    "age":[20,31,22]
}
df=pd.DataFrame(data)
df.to_csv("student.csv",index=False)
print("csv saved")