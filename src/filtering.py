import pandas as pd
from pandas import DataFrame

from data_import import import_users, import_movies, import_ratings


def filter_for_movies_with_over_x_ratings(
    movies: DataFrame, ratings: DataFrame, x: int
) -> DataFrame:
    movies_with_counts = movies.join(ratings.mid.value_counts())
    return movies_with_counts[movies_with_counts["count"] >= x]
