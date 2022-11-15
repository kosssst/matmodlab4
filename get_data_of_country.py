import pandas as pd

df = pd.read_csv("archive/covid_19_data.csv")
new_df = df.loc[df["Country/Region"] == "Ukraine"]
# print(new_df.to_string())
new_df.to_csv("ukraine.csv", sep=',', encoding='utf-8')