from django.shortcuts import render


def index(request):
    city = 'Санкт-Петербург'
    hobbies = ['Футбол', 'Программирование в совокупности с прослушиванием музыки',
               'Велосипедные прогулки', 'Осуществление мыслительных процессов, лежа на кровати:)']
    experience = [(None, 'Голосовой помощник для ведения дневника с домашним заданием, к сожалению, не сохранен в облаке (PyQt5, speech_recognition)'),
                  ('https://github.com/dm1itri/checkers', 'Реализация шашек (PyGame, socket)'),
                  ('https://github.com/dm1itri/WEB_PROJECT', 'Создания сайта для определения направления в крупной сфере IT (Flask)'),
                  (None, 'Создание простых чат-ботов в Telegram, VK'),
                  ('https://github.com/dm1itri/individual-project-10',
                   'Сейчас разрабатываю веб-игру для представления, как Итоговый проект в школе (в данным момент реализуется фронтенд: HTML5, SASS, JS)')]
    return render(request, 'profile/index.html', {'city': city, 'hobbies': hobbies, 'experience': experience})
