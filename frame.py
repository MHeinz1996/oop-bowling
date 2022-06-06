class Frame:
    def __init__(self, frame_num) -> None:
        self.frame_num = frame_num
        self.first = 0
        self.second = 0
        self.third = 0
        self.frame = []

    def set_frame(self):
        pass
        
        # Write logic to store scores in the frame.
        # If a bowl is a strike, it should be an X
        # If a bowl is a spare, it should be a /
        # If a bowl is a miss, it should be a -
        # Make sure to accout for the 10th frame



# What does a Frame do?
# Frames keep track of the amount of pins knocked down for that specific round
## Each Frame has two chances to knock down all 10 pins
### If it is the 10th frame, there are 3 rounds if the player gets a spare or a strike