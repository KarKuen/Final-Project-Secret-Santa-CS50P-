import random


class Person:
    def __init__ (self, name, secretsanta, gift='coals'):
        self.name = name
        self.secretsanta = secretsanta
        self.gift = gift

    def __str__ (self):
        return f"{self.name} is {self.secretsanta}'s secret santa! {self.name} is gifting {self.secretsanta} {self.gift}"

    def gifting (self, gift):
        self.gift = gift


def main():
    santa = participants()
    secretsanta = secretsantas(santa)
    christmassales(secretsanta)
    christmaseve()
    christmasday(secretsanta)


def participants():
    santa = []
    print('Add in participants. Enter "E" to stop')
    while True:
        participant = input('Name: ')
        if participant != 'E':
            santa.append(participant)
        else:
            break
    return santa


def secretsantas(santas):
    secretsanta = []
    random.shuffle(santas)
    for i in range(len(santas)):
        person = Person(santas[i], santas[i - 1])
        secretsanta.append(person)
    return(secretsanta)


def presents():
    gifter = input('Who is buying a gift? ')
    gift = input('What gift is he buying? ')
    return(gifter, gift)


def purchase(secretsanta, gifter, gift):
    for santa in secretsanta:
        if santa.name == gifter:
            santa.gifting(gift)


def christmassales(secretsanta):
    while True:
        question = input('Is anyone buying presents? Y/N ').capitalize()
        if question == 'Y':
            gifter, gift = presents()
            purchase(secretsanta, gifter, gift)
        elif question == 'N':
            break
        else:
            pass


def christmaseve():
    while True:
        christmas = input("It's Christmas Day! (say 'Merry Christmas' to receive your gifts) ").upper()
        if christmas == "MERRY CHRISTMAS":
            break
        else:
            pass


def christmasday(secretsanta):
    for santa in secretsanta:
        print(santa)


if __name__ == '__main__':
    main()