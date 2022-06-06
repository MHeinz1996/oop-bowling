class Frame:
    def __init__(self, frame_num) -> None:
        self.frame_num = frame_num


# What does a Frame do?
# Frames keep track of the amount of pins knocked down for that specific round
## Each Frame has two chances to knock down all 10 pins
### If it is the 10th frame, there are 3 rounds if the player gets a spare or a strike