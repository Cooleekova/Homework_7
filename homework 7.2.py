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
            print(f'                 {track}')
        return f''

    def add_track(self, new_track):
        self.tracks.append(new_track)

    def get_duration(self):
        album_duration = 0
        for track in self.tracks:
            album_duration += track.duration
        print(f'Длительность альбома {self.name} - {album_duration} минут')

    def __str__(self):
        print(f'Название группы: {self.band}\nНазвание альбома: {self.name}\nСписок треков: ')
        return f'{self.get_tracks()}'


print()
revolver = Album('Revolver', 'Beatles')
revolver.tracks = [yellow_submarine, she_said, good_day_sunshine]

nevermind = Album('Nevermind', 'Nirvana')
nevermind.tracks = [breed, lithium, polly]

print(nevermind)
print(revolver)
