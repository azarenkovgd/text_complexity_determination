import pathlib

PROJECT_ROOT = pathlib.Path(__file__).parent.parent
DATA_FOLDER = PROJECT_ROOT / 'data'
WORDS_WITH_LVLS_FOLDER = DATA_FOLDER / 'words_with_lvls'
ENGLISH_LVLS = ['A', 'B', 'C']
SONG_LOCATION = DATA_FOLDER / 'song.txt'
KAGGLE_DATASET_LOCATION = DATA_FOLDER / 'words_freq.csv'

C_SONG_LOCATION = DATA_FOLDER / 'c_song.txt'
B_SONG_LOCATION = DATA_FOLDER / 'b_song.txt'
A_SONG_LOCATION = DATA_FOLDER / 'a_song.txt'
