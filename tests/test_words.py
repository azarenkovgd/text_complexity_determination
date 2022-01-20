from src.configs import C_SONG_LOCATION, B_SONG_LOCATION, A_SONG_LOCATION
from src.words import get_estimation_using_words


def test_get_estimation_using_words():
    assert get_estimation_using_words(C_SONG_LOCATION) == 'C'
    assert get_estimation_using_words(B_SONG_LOCATION) == 'B'
    assert get_estimation_using_words(A_SONG_LOCATION) == 'A'
