import pathlib
import re
import string

import nltk
import pandas as pd
from nltk.corpus import stopwords
from sklearn import neighbors

from src.configs import KAGGLE_DATASET_LOCATION, ENGLISH_LVLS, WORDS_WITH_LVLS_FOLDER
from src.load_data import load_txt_to_list_of_lines


def get_song_words(song_text: str):
    words = song_text.split()

    # приводим слова к "базовой" форме
    wnl = nltk.stem.WordNetLemmatizer()
    words = map(lambda word: wnl.lemmatize(word), words)

    # оставляем только валидные английские слова
    text_vocab = set(word for word in words if word.isalpha())
    english_vocab = set(word.lower() for word in nltk.corpus.words.words())
    valid_words = text_vocab & english_vocab

    # удаляем предлоги, местоимения и тд
    stop_words = stopwords.words()
    words = filter(lambda word: word not in stop_words, valid_words)

    words = pd.DataFrame(words)
    words.set_index(0, drop=True, inplace=True)

    return pd.DataFrame(words)


def get_manual_dataset():
    manual_dataset = {}

    for lvl in ENGLISH_LVLS:
        for number in [1, 2]:
            path = WORDS_WITH_LVLS_FOLDER / f'{lvl}{number}_слова.txt'
            words = load_txt_to_list_of_lines(path)

            # берем только первые 100 слов для сбалансированного датасета
            for word in words[:100]:
                # к сожалению, словосочетания не получится учитывать
                if len(word.split()) > 1:
                    continue
                word = word.lower()
                manual_dataset[word.lower()] = {
                    'lvl': lvl
                }

    manual_dataset = pd.DataFrame.from_dict(manual_dataset)
    manual_dataset = manual_dataset.transpose()

    return manual_dataset


def create_count_column(df_to_update: pd.DataFrame, kaggle_dataset: pd.DataFrame):
    not_intersecting = set(df_to_update.index) - set(kaggle_dataset.index)
    df_to_update.drop(not_intersecting, axis=0, inplace=True)
    df_to_update['count'] = kaggle_dataset.loc[df_to_update.index]['count']


def get_words_based_estimation(song_text: str) -> str:
    kaggle_dataset = pd.read_csv(KAGGLE_DATASET_LOCATION, index_col=0, header=0)

    # подгружаем вручную размеченный датасет
    manual_dataset = get_manual_dataset()
    create_count_column(manual_dataset, kaggle_dataset)

    # подготовка тренировочного датасета
    x = pd.DataFrame(manual_dataset['count'])
    y = manual_dataset['lvl']

    # обучение модели
    classifier = neighbors.KNeighborsClassifier(15)
    classifier.fit(x, y)

    # подгружаем и обрабатываем трек
    song_words = get_song_words(song_text)
    create_count_column(song_words, kaggle_dataset)

    song_words['lvl'] = classifier.predict(song_words)
    table = song_words['lvl'].value_counts() / len(song_words)

    # границы счета вычисляются эмпирически (после экспериментов)
    score = table['B'] + table['C'] * 2

    if score > 0.50:
        return 'C'

    if score > 0.35:
        return 'B'

    return 'A'
