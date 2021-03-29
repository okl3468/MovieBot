from kinopoisk import movie
from imdb import IMDb
from src import config


class Parser:
    def __init__(self):
        self.output = ""
        self.full_output = ""
        self.photo = None
        self.name = ""
        self.id = 1

    def parse_text(self, text):
        Parser.__init__(self)
        m = movie.Movie()
        ia = IMDb()
        movie_list = m.objects.search(text)
        if len(movie_list) == 0:
            return config.error_msg(text)
        output_text = "По запросу \"{}\" найдено:\n".format(text)
        for item in movie_list[:8]:
            title = item.title
            year = item.year
            rating = item.rating

            if rating is None:
                rating = "Нет данных"

            if item.series:
                title = title + " (сериал)\t"
            if item.title_en:
                title = title + " ({})".format(item.title_en)
                movie_original = ia.search_movie(item.title_en)
                id_m = movie_original[0].movieID
                output_text += "● {}\n📅: {}\t⭐️ {}\t/i{} ️\n".format(title, year, rating, id_m)
            elif item.title_en is None:
                output_text += "● {}\n📅: {}\t⭐️ {}\t\n".format(title, year, rating)

 #           print(id)
        return output_text

    # "● Криминальное чтиво [1995; /i342]"

    def parse_id(self, film_id):
        ia = IMDb()
        movie = ia.get_movie(film_id)

        self.name = movie.get('title')
        self.id = movie.movieID

        self.full_output = movie.summary()

        #краткая информация (output)

        #Заголовок
        self.output = "Заголовок: " + movie.get('title') + "\n"
        # self.output += "Режиссёр: " + movie.get('director') + "\n"
        # self.output += "Жанр: " + movie.get('genres') + "\n"

        #Рейтинг

        #Актёры

        #Трейлер

        #Сюжет
        # pl = movie.get('plot')
        # self.output += "Сюжет: "
        # for i in pl:
        #     self.output += str(pl[0:i])
        # self.output += "\n"

        #Страница на ресурсе
#        self.output +=

        #Постер
        self.photo = movie.get('full-size cover url')


if __name__ == '__main__':
    pass