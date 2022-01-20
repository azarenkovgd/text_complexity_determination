import pathlib


def load_txt_to_list_of_lines(path: pathlib.Path):
    with open(path) as f:
        lines = f.readlines()

    cleaned_lines = []
    for line in lines:
        # убираем лишние пробелы, табуляцию и переносы строк, приводим к нижнему регистру - это универсальное действие
        line = line.strip()
        # пустые строки бесполезны в нашем сценарии, так что их можно смело выкидывать
        if line != '':
            cleaned_lines.append(line)

    return cleaned_lines
