# Задача №1 "Ферма Дядюшки Джо"
# Вы приехали помогать на ферму Дядюшки Джо и видите вокруг себя множество разных животных:

# гусей "Серый" и "Белый"
# корову "Маньку"
# овец "Барашек" и "Кудрявый"
# кур "Ко-Ко" и "Кукареку"
# коз "Рога" и "Копыта"
# и утку "Кряква"​Со всеми животными вам необходимо как-то взаимодействовать:
# кормить
# корову и коз доить
# овец стричь
# собирать яйца у кур, утки и гусей
# различать по голосам(коровы мычат, утки крякают и т.д.)​

# Задание 1:
# Нужно реализовать классы животных и определить методы взаимодействия с животными.
# ​Для каждого животного из списка должен существовать экземпляр класса.
# Каждое животное требуется накормить и подоить/постричь/собрать яйца, если надо.​

# Задание 2:
# У каждого животного должно быть определено имя(self.name) и вес(self.weight).

# Необходимо посчитать общий вес всех животных(экземпляров класса);
# Вывести название самого тяжелого животного.

# классы: Гусь, корова, овца, курица, коза, утка
# Goose, cow, sheep, chicken, goat, duck
# список всех видов животных на ферме
# animals_types = [Goose, Cow, Sheep, Chicken, Goat, Duck]

class Animal:
    def feed(self, food):
        self.weight += food * 0.3

    def say(self):
        print(self.voice)

class Bird(Animal):
    def __init__(self, name, weight, voice):
        self.name = name
        self.weight = weight
        self.voice = voice

    def egg(self):
        return f'Я собрала яйца {self.name} {type(self)}'

class Cattle(Animal):
    def __init__(self, name, weight, voice):
        self.name = name
        self.weight = weight
        self.voice = voice

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