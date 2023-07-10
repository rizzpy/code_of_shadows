# Code of Shadows
# A Sam Grey Mystery
# RizzPy, July 2023
# -----------------
import time

class Game:
    story_choices = []

    def display(self, story_array):
        for line in story_array:
            print(line)
            time.sleep(3)

    def start(self):
        print('--------------------------')
        print('Welcome to Code of Shadows')
        print('--------------------------')
        time.sleep(1.3)
        self.name = input('Enter your name: ')
        print(f'{self.name} you have been working as Sam Grey\'s intern for 5 months.')
        time.sleep(1.3)
        self.display(['Sam is a private detective who as far as you know used to be a cop and in the military.',
                      'The pay has not been the best but you expect a good recommendation.',
                      'A woman walks into the office.',
                      "\"I'm here to see Sam,\" she says."])

def main():
    game = Game()
    game.start()


if __name__ == "__main__":
    main()
