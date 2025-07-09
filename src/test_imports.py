import pytest
from data_import import import_movies, import_ratings, import_users
from io import StringIO


@pytest.fixture
def users_data():
    return StringIO(
        """
        1::F::1::10::48067
        2::M::56::16::70072
        3::M::25::15::55117
        """
    )


@pytest.fixture
def movies_data():
    return StringIO(
        """
        1::Toy Story (1995)::Animation|Children's|Comedy
        2::Jumanji (1995)::Adventure|Children's|Fantasy
        3::Grumpier Old Men (1995)::Comedy|Romance
        4::Waiting to Exhale (1995)::Comedy|Drama
        5::Father of the Bride Part II (1995)::Comedy
        """
    )


@pytest.fixture
def ratings_data():
    return StringIO(
        """
        1::1193::5::978300760
        1::661::3::978302109
        1::914::3::978301968
        1::1197::3::978302268
        1::1287::5::978302039
        2::1245::2::978299200
        2::1246::5::978299418
        3::3421::4::978298147
        3::1641::2::978298430
        3::648::3::978297867
        """
    )


def test_import_users(users_data):
    users = import_users(users_data)
    with pytest.raises(KeyError):
        users.loc[0]
    assert users.index[0] == 1, "index should be set to user id which doesnt contain 0"


def test_import_movies(movies_data):
    movies = import_movies(movies_data)
    with pytest.raises(KeyError):
        movies.loc[0]
    assert (
        movies.index[0] == 1
    ), "index should be set to movie id which doesnt contain 0"
    assert (
        movies["title"].iloc[0] == "Toy Story (1995)"
    ), "First movie title should be 'Toy Story (1995)'"


def test_import_ratings(ratings_data):
    ratings = import_ratings(ratings_data)
    assert len(ratings) == 10, "Test data contains 10 ratings, wrong number imported"
    assert ratings["uid"].iloc[0] == 1, "First rating should be from user ID 1"
    assert ratings["mid"].iloc[0] == 1193, "First rating should be for movie ID 1193"


def test_data_consistency():
    ratings = import_ratings("data/ratings.dat")
    movies = import_movies("data/movies.dat")
    users = import_users("data/users.dat")
    assert set(ratings["mid"]).issubset(
        set(movies.index)
    ), "IDs appear that aren't part of the movie data provided"
    assert set(ratings["uid"]).issubset(
        set(users.index)
    ), "IDs appear that aren't part of the user data provided"
