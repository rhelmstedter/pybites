##{
import pandas as pd
from matplotlib import pyplot as plt

data = "https://bites-data.s3.us-east-2.amazonaws.com/summer.csv"


def athletes_most_medals(data: str = data) -> pd.Series:
    df = pd.read_csv(data)
    top_athletes = dict()
    for gender in ["Men", "Women"]:
        top_athlete, medal_count = (
            df
            .where(df.Gender == gender)
            .Athlete.value_counts()
            .agg(['idxmax', max])
        )
        top_athletes[top_athlete] = medal_count
    return top_athletes


##}


##{
df = pd.read_csv(data)
top10 = df.Country.value_counts().index[:10]
medals = (
    df
    .where(df.Country.isin(top10))
    .groupby(['Country', "Medal"])
    .Medal
    .count()
    .unstack()
    .reset_index()
)

medals['Total'] = medals.Bronze + medals.Silver + medals.Gold
medals.sort_values(by=['Total'], ascending=False)

import plotext as plt

countries = medals.Country
total = medals.Total

plt.bar(countries, total, orientation = "h", width = 0.3, marker = 'fhd') 
plt.title("Top Ten Medal Counts")
plt.clc() # to remove colors
plt.plotsize(100, (2 * len(pizzas) - 1) + 4) # 4 = (1 for x numerical ticks + 2 for x axes + 1 for title)
plt.show()
##}
