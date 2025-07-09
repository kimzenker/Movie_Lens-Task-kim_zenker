import pytest

from data_import import import_movies, import_ratings, import_users

# todo: maybe add tests for the casting i do in find_age_group_with_most_ratings in task.py


# testing everything that went wrong for me while importing
def test_import_users():
    users = import_users()
    with pytest.raises(KeyError):
        users.loc[0]
    assert users.index[0] == 1, "First User ID should be 1 "


def test_import_movies():
    movies = import_movies()
    with pytest.raises(KeyError):
        movies.loc[0]
    assert movies.index[0] == 1, "First movie ID should be 1 "


def test_import_ratings():
    ratings = import_ratings()
    movies = import_movies()
    assert set(ratings["mid"]).issubset(
        set(movies.index)
    ), "IDs appear that aren't part of the movie data provided"


if __name__ == "__main__":
    test_import_users()
    test_import_movies()
    test_import_ratings()
