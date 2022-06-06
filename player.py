from frame import Frame
from random import randrange

class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.score = 0

    def bowl(self, frame_num):
        frame = Frame(frame_num)
        pass

        # Write logic to randomize a bowl
        # if frame_num < 10, only two bowls (unless the first is a strike)
        # if frame_num == 10, player can bowl 3 times if the first bowl is a 10, or the first + second bowls == 10



# What can a Player do?
# players can bowl and keep score
## If they don't get a strike, they can bowl twice per frame
### If they are on the tenth frame and bowl a strike or a spare, they can bowl a third time