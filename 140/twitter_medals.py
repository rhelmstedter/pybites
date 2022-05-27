##{
import pandas as pd
import plotext as plt

data = "https://raw.githubusercontent.com/rhelmstedter/coding-class/main/coding-projects/data/summer.csv"

df = pd.read_csv(data)
top10 = df.Country.value_counts().index[:10]

medals = (
    df
    .where(df.Country.isin(top10))
    .groupby(["Country", "Medal"])
    .Medal.count()
    .unstack()
    .reset_index()
    .assign(Total=lambda x: x.Bronze + x.Silver + x.Gold)
    .sort_values(by="Total")
)

plt.bar(medals.Country, medals.Total, orientation="h", width=0.3, marker="fhd")
plt.title("Top Ten Summer Olympic Medal Counts 1896-2014")
plt.clc()
plt.plotsize(100, (2 * len(medals.Country) - 1) + 4)
plt.show()
##}
