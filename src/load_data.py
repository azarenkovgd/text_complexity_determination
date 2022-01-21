import pathlib
import re
import string


def load_txt_to_list_of_lines(path: pathlib.Path) -> list[str]:
    with open(path, encoding='utf-8') as f:
        lines = f.readlines()

    cleaned_lines = []
    for line in lines:
        # убираем лишние пробелы, табуляцию и переносы строк, приводим к нижнему регистру - это универсальное действие
        line = line.strip()
        # пустые строки бесполезны в нашем сценарии, так что их можно смело выкидывать
        if line != '':
            cleaned_lines.append(line)

    return cleaned_lines


def get_song_text(song_location: pathlib.Path) -> str:
    lines = load_txt_to_list_of_lines(song_location)

    text = ' '.join(lines)
    text = re.sub(f'[{string.punctuation}’]', '', text)
    text = text.lower()

    return text
