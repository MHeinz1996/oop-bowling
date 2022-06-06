class Frame:
    def __init__(self, frame_num) -> None:
        self.frame_num = frame_num
        self.first_bowl = None
        self.second_bowl = None
        self.third_bowl = None
        self.frame = []

    def set_frame(self):
        if self.first_bowl != None:
            if self.first_bowl == 10:
                self.frame.append('X')
            elif self.first_bowl == 0:
                self.frame.append('-')
            else:
                self.frame.append(self.first_bowl)
        
        if self.second_bowl != None:
            if self.second_bowl == 0:
                self.frame.append('-')
            elif self.first_bowl+self.second_bowl == 10:
                self.frame.append('/')
            elif self.third_bowl != None and self.second_bowl == 10:
                self.frame.append('X')
            else:
                self.frame.append(self.second_bowl)
        
        if self.third_bowl != None:
            if self.third_bowl == 0:
                self.frame.append('-')
            elif self.second_bowl != 10 and self.second_bowl+self.third_bowl == 10:
                self.frame.append('/')
            elif self.second_bowl == 10 and self.third_bowl == 10:
                self.frame.append('X')
            else:
                self.frame.append(self.third_bowl)

        return self.frame
        
        # Write logic to store scores in the frame.
        # If a bowl is a strike, it should be an X
        # If a bowl is a spare, it should be a /
        # If a bowl is a miss, it should be a -
        # Make sure to accout for the 10th frame



# What does a Frame do?
# Frames keep track of the amount of pins knocked down for that specific round
## Each Frame has two chances to knock down all 10 pins
### If it is the 10th frame, there are 3 rounds if the player gets a spare or a strike