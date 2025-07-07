# 1. Which are the Top 10 best rated movies (consider only movies which have at least 10 ratings)?
# 2. Which age group give the most ratings overall?
import pandas as pd
from pandas import DataFrame
from data_import import import_users, import_movies, import_ratings
from filtering import filter_for_movies_with_over_x_ratings

def find_top_ten_movies(movies:DataFrame, ratings:DataFrame, min_number_of_rating_per_movie:int):
    """returns the top ten movies based on average rating"""
    relevant_movies = filter_for_movies_with_over_x_ratings(movies, ratings, min_number_of_rating_per_movie)

    mean_ratings_per_movie = ratings.groupby(['mid']).rating.mean()
    relevant_movies_with_mean_rating = relevant_movies.join(mean_ratings_per_movie, how='inner')
    relevant_movies_with_mean_rating_sorted = relevant_movies_with_mean_rating.sort_values(by='rating', ascending=False)
    return relevant_movies_with_mean_rating_sorted[:10]



if __name__ == "__main__":
    top_ten = find_top_ten_movies(movies=import_movies(),ratings=import_ratings(), min_number_of_rating_per_movie=10)
    print('The Top 10 best rated movies are')
    for i, mid in enumerate(top_ten.index):
        print(f"{i+1}. {top_ten.iloc[i]['title']} with an average rating of {round(top_ten.iloc[i]['rating'], 2)} stars ")
    print('(averages are rounded to 2 decimal points)')