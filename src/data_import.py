import pandas as pd
from pandas import DataFrame


def import_users() -> DataFrame:
    """returns df indexed by userid"""
    return pd.read_csv('data/users.dat', sep='::', engine='python', names=['uid', 'gender', 'age', 'occupation', 'zip-code'], index_col='uid', dtype={'uid': 'int32', 'gender': 'string', 'age': 'int32', 'occupation': 'int32', 'zip-code': 'string'})


def import_movies() -> DataFrame:
    """returns df indexed by movieid"""
    return pd.read_csv('data/movies.dat', sep='::', engine='python', encoding='latin-1', names=['mid', 'title', 'genres'], index_col='mid', dtype={'mid': 'int32', 'title': 'string', 'genres': 'string'})


def import_ratings() -> DataFrame:
    """returns dataframe"""
    def cast_ratings_to_float(rating):
        ranting_for_float = str(rating).replace(',', '.')
        return float(ranting_for_float)
    return pd.read_csv('data/ratings.dat', sep='::',
                       engine='python', names=['uid', 'mid', 'rating', 'timestamp'], converters={'rating': cast_ratings_to_float}, dtype={'uid': 'int32', 'mid': 'int32', 'timestamp': 'string'})


age_group_translation = {1:  "Under 18",
                         18:  "18-24",
                         25:  "25-34",
                         35:  "35-44",
                         45:  "45-49",
                         50:  "50-55",
                         56:  "56+"}
