# Задание 1:
# Вам нужно реализовать родительский класс для всех животных и вынести общее поведение в него.
# От родительского класса должны будут отнаследоваться все остальные животные.
# В родительском классе должно быть 2-3 общих класса и общие поля.
#
# Задание 2:
# Используя методы из родительского класса, вызовите их в цикле у списка всех животных.

class Animal:
    def feed(self, food):
        self.weight += food * 0.3

    def say(self):
        print(self.voice)

class Bird(Animal):

    def egg(self):
        return f'Я собрала яйца {self.name} {type(self)}'

class Cattle(Animal):
    pass

class Milking(Cattle):
    def __init__(self, name, weight, voice):
        self.name = name
        self.weight = weight
        self.voice = voice

    def milk(self, liter):
        self.weight -= liter

class Mutton(Cattle):
    def __init__(self, name, weight, voice):
        self.name = name
        self.weight = weight
        self.voice = voice

    def wool(self, wool):
        self.weight -= wool

class Goose(Bird):
    def __init__(self, name, weight, voice='Ga-ga-ga'):
        self.name = name
        self.weight = weight
        self.voice = voice

grey_goose = Goose('Серый', 5)
white_goose = Goose('Белый', 5)

class Cow(Milking):
    def __init__(self, name, weight, voice='Moo!'):
        self.name = name
        self.weight = weight
        self.voice = voice

manya = Cow('Манька', 100)

class Sheep(Mutton):
    def __init__(self, name, weight, voice='Bee!'):
        self.name = name
        self.weight = weight
        self.voice = voice

barashek = Sheep('Барашек', 60)
kudryaviy = Sheep('Кудрявый', 60)

class Chicken(Bird):
    def __init__(self, name, weight, voice='Ko-ko-ko'):
        self.name = name
        self.weight = weight
        self.voice = voice

koko = Chicken('koko', 3)
kukareku = Chicken('kukareku', 3)

class Goat(Milking):
    def __init__(self, name, weight, voice='Meee'):
        self.name = name
        self.weight = weight
        self.voice = voice

roga = Goat('Roga', 50)
kopyta = Goat('kopyta', 50)


class Duck(Bird):
    def __init__(self, name, weight, voice='Krya-krya'):
        self.name = name
        self.weight = weight
        self.voice = voice

kryakva = Duck('Kryakva', 4)

# список всех животных на ферме
animals = [grey_goose, white_goose, manya, barashek, kudryaviy, koko, kukareku, roga, kopyta, kryakva]

# кормить всех животных
for animal in animals:
    if type(animal) == Goose or Chicken or Duck:
        animal.feed(1)
    elif type(animal) == Cow or Sheep or Goat:
        animal.feed(10)
    print(f'Я накормила {animal.name} {type(animal)}')

print()


# голоса животных
for animal in animals:
    print(f'{animal.name} говорит {animal.voice}')

print()