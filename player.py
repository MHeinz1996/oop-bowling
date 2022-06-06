from frame import Frame
from random import randrange

class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.score = 0
        self.frames = []

    def bowl(self, frame_num):
        frame = Frame(frame_num)
        
        if(frame_num != 10):
            frame.first_bowl = randrange(0, 11)

            if(frame.first_bowl != 10):
                frame.second_bowl = randrange(0, 11-frame.first_bowl)

                self.frames.append(frame.set_frame())
            else:
                self.frames.append(frame.set_frame())
        else: # frame_num == 10
            frame.first_bowl = randrange(0, 11)

            if(frame.first_bowl != 10):
                frame.second_bowl = randrange(0, 11-frame.first_bowl)
                
                if(frame.first_bowl + frame.second_bowl == 10):
                    frame.third_bowl = randrange(0, 11)

                    self.frames.append(frame.set_frame())
                else: # frame.first_bowl + frame.second_bowl != 10
                    self.frames.append(frame.set_frame())
            else: # frame.first_bowl == 10
                frame.second_bowl = randrange(0, 11)
                
                if frame.second_bowl != 10:
                    frame.third_bowl = randrange(0, 11-frame.second_bowl)
                    self.frames.append(frame.set_frame())
                else:
                    frame.third_bowl = randrange(0, 11)
                    self.frames.append(frame.set_frame())
    
        print(frame.first_bowl, frame.second_bowl, frame.third_bowl)

        if frame_num == 10:
            print(self.frames)
            print(len(self.frames))
    # def score(self):
    #     return self.frames



# What can a Player do?
# players can bowl and keep score
## If they don't get a strike, they can bowl twice per frame
### If they are on the tenth frame and bowl a strike or a spare, they can bowl a third time