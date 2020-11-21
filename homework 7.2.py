# Необходимо уметь хранить информацию по альбомам и трекам в них. Это можно сделать, используя классы Album и Track.
# У класса Track есть поля:
# Название;
# Длительность в минутах(используется тип данных int).
# И метод show, выводящий информацию по треку в виде <Название-Длительность>.

# У класса Album есть поля:
# Название альбома
# Группа
# Список треков
# И три метода:
# get_tracks - выводит информацию по всем трекам(используется метод show).
# add_track - добавление нового трека в список треков.
# get_duration - выводит длительность всего альбома.
# Задание:
# Создать 2 альбома с 3 треками. Для каждого вывести его длительность.

class Track:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def __str__(self):
        return f'{self.name} - {self.duration} min'

    # Сравнивать треки по длительности
    def __lt__(self,other):
        if not isinstance(other, Track):
            print('Это не трек!')
        return self.duration < other.duration


yellow_submarine = Track('Yellow Submarine', 5)
she_said = Track('She Said She Said', 4)
good_day_sunshine = Track('Good Day Sunshine', 4)

breed = Track('Breed', 3)
lithium = Track('Lithium', 4)
polly = Track('Polly', 2)

# Сравнивать треки по длительности
print(breed > polly)
print(she_said < yellow_submarine)

class Album:
    def __init__(self, name, band):
        self.name = name
        self.band = band
        self.tracks = []

    def get_tracks(self):
        for track in self.tracks:
            print(track)
        return f''

    def add_track(self, new_track):
        self.tracks.append(new_track)

    def get_duration(self):
        album_duration = 0
        for track in self.tracks:
            album_duration += track.duration
        print(f'Длительность альбома {self.name} - {album_duration} минут')

    def __str__(self):
        # self.get_tracks()
        print(f'Название группы: {self.band}\nНазвание альбома: {self.name}\nСписок треков: ')
        return f'{self.get_tracks()}'




print()
revolver = Album('Revolver', 'Beatles')
revolver.tracks = [yellow_submarine, she_said, good_day_sunshine]
# revolver.get_tracks()
# print(revolver.tracks)

print()
nevermind = Album('Nevermind', 'Nirvana')
nevermind.tracks = [breed, lithium, polly]
# nevermind.get_tracks()


print(nevermind)
print(revolver)

# print()
# revolver.get_duration()
# nevermind.get_duration()






