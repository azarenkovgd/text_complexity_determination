from src.configs import C_SONG_LOCATION, B_SONG_LOCATION, A_SONG_LOCATION
from src.load_data import get_song_text
from src.words import get_words_based_estimation


def test_get_estimation_using_words():
    assert get_words_based_estimation(get_song_text(A_SONG_LOCATION)) == 'A'
    assert get_words_based_estimation(get_song_text(B_SONG_LOCATION)) == 'B'
    assert get_words_based_estimation(get_song_text(C_SONG_LOCATION)) == 'C'
