import pathlib


# для обработки текст нужно поместить в папку data (предварительно ее создав)
PROJECT_ROOT = pathlib.Path(__file__).parent.parent
DATA_FOLDER = PROJECT_ROOT / 'data'


def load_txt_to_list_of_lines(path: pathlib.Path):
    with open(path) as f:
        lines = f.readlines()

    # убираем пробелы, переносы строк
    return list(map(lambda string: string.strip(), lines))
