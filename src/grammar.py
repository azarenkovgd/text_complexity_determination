import re


def get_grammar_based_estimation(song_text: str) -> str:
    # делаем проверку для конструкций уровня C
    regex_list = [
        r'(get|got) used to \w*ing',
        f'(is|am|are)(nt|)( not|) having',
        f'(have|has)(nt|) being having',
        'ly enough',
        '(were|was)( not|) to'
    ]

    for regex in regex_list:
        if re.search(regex, song_text) is not None:
            return 'C'

    # делаем проверку для конструкций уровня B
    regex_list = [
        '(will|wont)'
        'used to',
        r'ing ',
        '(could|couldnt)',
        '(have to|got to)'
        '(may|might|must|should|have to|ought to)'
    ]

    for regex in regex_list:
        match = re.search(regex, song_text)
        if match is not None:
            return 'B'

    # если продвинутые конструкции не найдены, выводим A, как минимально возможный уровень
    return 'A'
