import string

START_MSG = 'Привет. Я - MovieBot. Помогу тебе найти информацию' \
            'об интересующем тебя фильме/сериале и найду, где ты можешь его посмотреть.' \
            'Введите название фильма или сериала, который вас интересует.'
ERROR_MSG = 'По запросу ниичего не удалось найти.' \
            'Попробуйте написать название на другом языке (русский, английский).' \
            'Если не получилось найти - информации о таком фильме нет или название ' \
            'введено неверно.'

WATCH_MSG = "Предлагаем вам ссылки на сервисы, где вы можете посмотреть это кино.\n" \
            "Выберете интересующий вас сервис и перейдите по ссылке.\n" \
            "Приятного просмотра!  🎥🍿"

LINK_IVI = "https://www.ivi.ru/search/?q="
LINK_OKKO = "https://okko.tv/search/"
LINK_KINOPOISK = "https://www.kinopoisk.ru/film/"
LINK_AMEDIATEKA = "https://www.amediateka.ru/search?query="
LINK_WINK = "https://wink.rt.ru/search?query="
LINK_MEGOGO = "https://megogo.ru/ru/search-extended?q="
LINK_START = "https://start.ru/search?q="
LINK_PREMIER = "https://premier.one/search?query="

#позже удалить
LINK_FS = "http://ex-fs.net/index.php?do=search&subaction=search&story="
LINK_HDREZKA = "http://hdrezka.name/index.php?do=search&subaction=search&q="
LINK_BASKINO = "http://baskino.me/index.php?do=search&mode=advanced&subaction=search&story="
#
#
#

def link_kinopoisk(id):
    return LINK_KINOPOISK + str(id) + '/watch/'


def error_msg(name):
    return ERROR_MSG.format(name)


PUNCTUATION = set(string.punctuation) - set('-')  #learn more