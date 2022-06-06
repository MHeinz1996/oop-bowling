from player import Player

class Game:
    def __init__(self) -> None:
        pass

    def play(self):

        player_name = input("Player Name: ")

        # Creates a player object
        player = Player(player_name)
    
        # Has player bowl 10 frames
        for frame in range(1,11):
            player.bowl(frame)

        # print(type(player.score()))
            

game_1 = Game()
game_1.play()
# What does the game do?
# Begins the game
# The game keeps track of each player's score and which frame they are on
## The game ends after the 10th frame