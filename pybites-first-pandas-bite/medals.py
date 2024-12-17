import pandas as pd

data = "https://bites-data.s3.us-east-2.amazonaws.com/summer.csv"


def athletes_most_medals(data: str = data) -> pd.Series:
    df = pd.read_csv(data)
    male = (
        df.where(df.Gender == "Men")
        .dropna()
        .groupby("Athlete")
        .Medal.count()
        .sort_values(ascending=False)
        .head(1)
    )
    female = (
        df.where(df.Gender == "Women")
        .dropna()
        .groupby("Athlete")
        .Medal.count()
        .sort_values(ascending=False)
        .head(1)
    )
    return pd.concat([male, female])


if __name__ == "__main__":
    print(
        athletes_most_medals(
            "https://bites-data.s3.us-east-2.amazonaws.com/summer_2008-2012.csv"
        )
    )
