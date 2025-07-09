import pandas as pd
from pandas import DataFrame


def import_users(filepath) -> DataFrame:
    """
    returns df indexed by userid (uid) with columns 'gender', 'age', 'occupation', 'zip-code'
    """
    return pd.read_csv(
        filepath,
        sep="::",
        engine="python",  # because of the '::' separator
        names=["uid", "gender", "age", "occupation", "zip-code"],
        index_col="uid",
        dtype={
            "uid": "int32",
            "gender": "string",
            "age": "int32",
            "occupation": "int32",
            "zip-code": "string",
        },
    )


def import_movies(filepath) -> DataFrame:
    """
    returns df indexed by movieid (mid) with columns 'title' and 'genres'
    """
    return pd.read_csv(
        filepath,
        sep="::",
        engine="python",  # because of the '::' separator
        encoding="latin-1",  # utf-8 doesn't work
        names=["mid", "title", "genres"],
        index_col="mid",
        dtype={
            "mid": "int32",
            "title": "string",
            "genres": "string",  # genres aren't used for now so we keep them as string
        },
    )


def import_ratings(filepath) -> DataFrame:
    """
    returns df with columns 'uid', 'mid', 'rating', 'timestamp'
    """
    return pd.read_csv(
        filepath,
        sep="::",
        engine="python",  # because of the '::' separator
        names=["uid", "mid", "rating", "timestamp"],
        converters={"rating": lambda x: float(x.replace(",", "."))},
        dtype={
            "uid": "int32",
            "mid": "int32",
            "timestamp": "string",  # timestamp is not used for now, so we keep it as string
        },
    )


age_group_translation = {
    # taken from the dataset documentation
    1: "Under 18",
    18: "18-24",
    25: "25-34",
    35: "35-44",
    45: "45-49",
    50: "50-55",
    56: "56+",
}
