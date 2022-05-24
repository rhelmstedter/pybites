##{
import pandas as pd

data = "https://bites-data.s3.us-east-2.amazonaws.com/summer.csv"


def athletes_most_medals(data: str = data) -> pd.Series:
    df = pd.read_csv(data)
    top_athletes = dict()
    for gender in ["Men", "Women"]:
        top_athlete, medal_count = df.where(df.Gender == gender).Athlete.value_counts().agg(['idxmax', max])
        top_athletes[top_athlete] = medal_count
    return top_athletes

##}
