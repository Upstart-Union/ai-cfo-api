import pandas as pd


def parse_csv(file):
    """
    Reads a CSV file into a pandas DataFrame.
    """

    dataframe = pd.read_csv(file)

    return dataframe