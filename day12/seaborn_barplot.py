import seaborn as sns
import matplotlib.pyplot as plt
students=["A","B","C","D"]
marks=[70,50,90,30]
sns.barplot(x=students,y=marks)
plt.show()