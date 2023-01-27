import random


class Player:

    def __init__(self):
        self.playerList = []
        self.numPlayers = int(input("How many people are playing?"))

        if self.numPlayers == 1:
            print("You are in single mode :D, you happy free individual !!!!!!")

        if self.numPlayers == 2:
            print("You are in taken mode <3")

        for x in range(self.numPlayers):
            self.playerList.append(input("What is your name, player?"))

class GamePlay:

    def __init__(self):
        x = Player()
        self.list_of_suspects = ['Tom', 'Timmy', 'Tilly', 'Topper']
        self.list_of_weapons = ['pool float', 'stuffed animal', 'plastic straw', 'a rock or something']
        self.list_of_rooms = ['kitchen', 'ur moms room', 'basement']
        self.playerList = x.playerList
        self.murderCopy = self.list_of_suspects.copy()
        self.weaponCopy = self.list_of_weapons.copy()
        self.roomCopy = self.list_of_rooms.copy()

        self.whodidit = {'Suspect': self.list_of_suspects.pop(random.randrange(0, len(self.list_of_suspects))),
                         'Weapon': self.list_of_weapons.pop(random.randrange(0, len(self.list_of_weapons))),
                         'Room': self.list_of_rooms.pop(random.randrange(0, len(self.list_of_rooms)))}
        print(self.whodidit)
        self.current_player = 0
        counter = 0


        print('Welcome to Clue. Enjoy your stay! or whatever.')

        while self.playerList.__len__() > 0:
            currentPlay = self.playerList.pop(0)

            action = input("What do you want to do, " + str(currentPlay) + "?" "\n" "1)Type 'i' to interrogate someone." "\n" "2)Type 'r' to go to a room." "\n" "3)Type g to guess who the killer is.")

            if action == 'i':
                print("You interrogated: " + random.choice(self.murderCopy) + " and you discovered they were not the murderer")

            if action == 'r':
                print("You walked into: " + random.choice(self.roomCopy) + " and did not discover a body.")

            self.playerList.append(currentPlay)

            if action == 'g':
                option1 = input("Who is the killer? " + "The options are " + str(self.murderCopy) + ".")
                if option1 == self.whodidit["Suspect"]:
                    counter = counter + 1

                option2 = input("What was the weapon? " + "The options are " + str(self.weaponCopy) + ".")
                if option2 == self.whodidit["Weapon"]:
                    counter = counter + 1

                option3 = input("What room was the murder in? " + "The options are " + str(self.roomCopy) + ".")
                if option3 == self.whodidit["Room"]:
                    counter = counter + 1

                if counter < 3:
                    print('someone hit you on the head with a rock because you are so stupid!')
                    self.playerList.pop(self.playerList.__len__() - 1)

                if counter == 3:
                    print('Wow you are an absolute genius individual!')
                    self.playerList.clear()


if __name__ == '__main__':
    GamePlay()
