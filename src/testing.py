import pytest
from data_import import *
## testing everything that went wrong for me while importing 
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

if __name__ == "__main__":
    print(import_users().head())
    print(import_movies().head())
    print(import_ratings().head())
    test_import_users()
    test_import_movies()
    test_import_ratings()