import pandas as pd
from pandas import DataFrame


def import_users() -> DataFrame:
    """returns df indexed by userid"""
    return pd.read_csv('data/users.dat', sep='::', engine='python', names = ['uid', 'gender', 'age', 'occupation', 'zip-code' ], index_col='uid')    


def import_movies() -> DataFrame:
    """returns df indexed by movieid"""
    return pd.read_csv('data/movies.dat', sep='::', engine='python', encoding='latin-1', names = ['mid', 'title', 'genres'], index_col = 'mid')


def import_ratings() -> DataFrame:
    """returns dataframe"""
    return pd.read_csv('data/ratings.dat', sep='::', engine='python', names = ['uid', 'mid', 'rating', 'timestamp'])
