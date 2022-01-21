from src.configs import C_SONG_LOCATION, B_SONG_LOCATION, A_SONG_LOCATION
from src.grammar import get_grammar_based_estimation
from src.load_data import get_song_text


def test_get_grammar_based_estimation():
    assert get_grammar_based_estimation(get_song_text(A_SONG_LOCATION)) == 'A'
    assert get_grammar_based_estimation(get_song_text(B_SONG_LOCATION)) == 'B'
    assert get_grammar_based_estimation(get_song_text(C_SONG_LOCATION)) == 'C'
