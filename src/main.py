from src.configs import B_SONG_LOCATION, A_SONG_LOCATION, C_SONG_LOCATION
from src.grammar import get_grammar_based_estimation
from src.load_data import get_song_text
from src.words import get_words_based_estimation


def main():
    song_text = get_song_text(B_SONG_LOCATION)
    # оцениваем текст песни используя данные о сложности употребляемых в ней слов
    print('words_based_estimation:', get_words_based_estimation(song_text))
    # ищем грамматические конструкции, актуальные для определенных уровней языка, делаем оценку
    print('grammar_based_estimation:', get_grammar_based_estimation(song_text))


if __name__ == '__main__':
    main()
