# 1. Which are the Top 10 best rated movies (consider only movies which have at least 10 ratings)?
# 2. Which age group give the most ratings overall?
import pandas as pd
from pandas import DataFrame
from typing import Tuple

from data_import import import_users, import_movies, import_ratings, age_group_translation
from filtering import filter_for_movies_with_over_x_ratings


def find_top_ten_movies(movies: DataFrame, ratings: DataFrame, min_number_of_rating_per_movie: int):
    """returns the top ten movies based on average rating"""
    relevant_movies = filter_for_movies_with_over_x_ratings(
        movies, ratings, min_number_of_rating_per_movie)

    mean_ratings_per_movie = ratings.groupby('mid').rating.mean()
    relevant_movies_with_mean_rating = relevant_movies.join(
        mean_ratings_per_movie, how='inner')
    relevant_movies_with_mean_rating_sorted = relevant_movies_with_mean_rating.sort_values(
        by='rating', ascending=False)
    return relevant_movies_with_mean_rating_sorted[:10]


def find_age_group_with_most_ratings(users: DataFrame, ratings: DataFrame) -> Tuple[int, int]:
    number_of_ratings_per_user = ratings.uid.value_counts()
    users_with_number_of_ratings = users.join(number_of_ratings_per_user)
    age_groups_with_number_of_rating_total = users_with_number_of_ratings.groupby('age')[
        'count'].sum()
    age_groups_sorted_by_number_of_rating = age_groups_with_number_of_rating_total.sort_values(
        ascending=False)
    top_age_group = age_groups_sorted_by_number_of_rating.index[0]
    number_of_ratings_in_top_age_group = age_groups_sorted_by_number_of_rating.iloc[0]
    return (top_age_group, number_of_ratings_in_top_age_group)


if __name__ == "__main__":
    top_ten = find_top_ten_movies(movies=import_movies(
    ), ratings=import_ratings(), min_number_of_rating_per_movie=10)
    print()
    print('The Top 10 best rated movies are:')
    for i, mid in enumerate(top_ten.index):
        print(
            f"{i+1}. {top_ten.iloc[i]['title']} with an average rating of {round(top_ten.iloc[i]['rating'], 2)} stars ")
    print('(averages are rounded to 2 decimal points)')

    top_age_group, number_of_ratings = find_age_group_with_most_ratings(
        import_users(), import_ratings())
    print()
    print(
        f"The age group {age_group_translation[top_age_group]} gives the most ratings overall, giwith  a total of {number_of_ratings} ratings.")
