import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("./file/train.csv")

# male/female
df = df.replace("male", 0).replace("female", 1)

df["Age"].fillna(df.Age.median(), inplace=True)

split_data = []
for s in [0, 1]:
    split_data.append(df[df.Survived == s])

temp = [i["Pclass"].dropna() for i in split_data]
plt.hist(temp, histtype="barstacked", bins=3)