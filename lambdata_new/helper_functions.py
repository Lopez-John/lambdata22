"""LambdataJohnLopez - A collection of Data Science Helper functions"""

import pandas as pd
import numpy as np
from datetime import datetime as dt

def null_count(df):
    """Checks the Dataframe for null values and
    returns amount of null values"""

    return df.isnull().sum().sum()


def list_2_series(list, df):
    """Converts a list into a Series, and creates a new column in
    the DataFrame"""

    # converts list into pandas Series
    new_series = pd.Series(list)

    # adds Series as column in the inputed DataFrame
    df['list'] = new_series
    return df


def split_dates(date_series):
    """Function to split dates of format "MM/DD/YYYY" into multiple
    columns (df['month'], df['day'], df['year']) and
    then return the same dataframe with those additional columns"""

    # converts dates to datetime
    date_series['date'] = date_series["date"].apply(pd.to_datetime)

    # creates a month, day, and year column
    date_series['Month'] = date_series['date'].dt.month
    date_series['Day'] = date_series['date'].dt.day
    date_series['Year'] = date_series['date'].dt.year

    return date_series


def train_test_split(df, frac):
    """Create a Train/Test split function for a dataframe and returns
    both the Training and Testing sets. Frac referes to the precent
    of data you would like to set aside for training"""

    train_split = df[: (int(len(df) * frac))]
    test_split = df[(int(len(df) * frac)):]
    return train_split, test_split
