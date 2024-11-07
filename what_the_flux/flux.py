from numpy import NaN
import pandas as pd

XYZ = "https://bites-data.s3.us-east-2.amazonaws.com/xyz.csv"
THRESHOLDS = (5000, 0.05)


def calculate_flux(XYZ: str) -> list:
    """Read the data in from xyz.csv
    add two new columns, one to calculate dollar flux,
    and the other to calculate percentage flux
    return as a list of tuples
    """

    df = (
        pd.read_csv(XYZ)
        .assign(dollar_flux=lambda df_: df_["12/31/20"] - df_["12/31/19"])
        .assign(percent_flux=lambda df_: round(df_["dollar_flux"] / df_["12/31/19"], 2))
    )

    return list(df.values)


def identify_flux(xyz: list) -> list:
    """Load the list of tuples, iterate through
    each item and determine if it is above both
    thresholds. if so, add to the list
    """
    df = (
        pd.read_csv(XYZ)
        .assign(dollar_flux=lambda df_: df_["12/31/20"] - df_["12/31/19"])
        .assign(percent_flux=lambda df_: round(df_["dollar_flux"] / df_["12/31/19"], 2))
        .where(lambda df_: abs(df_.dollar_flux) > THRESHOLDS[0], NaN)
        .where(lambda df_: abs(df_.percent_flux) > THRESHOLDS[1], NaN)
        .dropna()
    )
    return list(df.values)
