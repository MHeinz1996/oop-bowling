from frame import Frame
from random import randrange

class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.score = 0
        self.frames = []
        self.multipliers = []

    def bowl(self, frame_num):
        frame = Frame(frame_num)
        
        if(frame_num != 10):
            frame.first_bowl = randrange(0, 11)

            if(frame.first_bowl != 10):
                frame.second_bowl = randrange(0, 11-frame.first_bowl)
                self.frames.append(frame.set_frame())
                # if(frame.first_bowl+frame.second_bowl == 10):
                #     self.multipliers.append('/')
            else:
                self.frames.append(frame.set_frame())
                # self.multipliers.append('X')
        else: # frame_num == 10
            frame.first_bowl = randrange(0, 11)

            if(frame.first_bowl != 10):
                frame.second_bowl = randrange(0, 11-frame.first_bowl)
                
                if(frame.first_bowl + frame.second_bowl == 10):
                    # self.multipliers.append('/')
                    frame.third_bowl = randrange(0, 11)

                    self.frames.append(frame.set_frame())
                else: # frame.first_bowl + frame.second_bowl != 10
                    self.frames.append(frame.set_frame())
            else: # frame.first_bowl == 10
                # self.multipliers.append('X')
                frame.second_bowl = randrange(0, 11)
                
                if frame.second_bowl != 10:
                    frame.third_bowl = randrange(0, 11-frame.second_bowl)
                    self.frames.append(frame.set_frame())
                else:
                    # self.multipliers.append('X')
                    frame.third_bowl = randrange(0, 11)
                    self.frames.append(frame.set_frame())
    
        # Write logic to calculate the score
        # Maybe make a first in-first out queue that store multipliers and applies them to the total score
        if len(self.multipliers) > 0:
            if self.multipliers[0] == 'X':
                if frame_num != 10:
                    if frame.second_bowl != None:
                        self.score += (frame.first_bowl + frame.second_bowl) * 2
                        self.multipliers.pop(0)
                    else:
                        self.score += (frame.first_bowl *2)
                        self.multipliers.pop(0)
                else:
                    if frame.first_bowl == 10:
                        self.score += frame.first_bowl + ((frame.second_bowl+frame.third_bowl) * 2)
                        self.multipliers.pop(0)
                    elif frame.first_bowl + frame.second_bowl == 10:
                        self.score += frame.first_bowl + frame.second_bowl + (frame.third_bowl*2)
                        self.multipliers.pop(0)
                    elif frame.third_bowl != None:
                        self.score += frame.first_bowl + frame.second_bowl + frame.third_bowl
                    else:
                        self.score += frame.first_bowl + frame.second_bowl
            elif self.multipliers[0] == '/':
                if frame.second_bowl != None:
                    self.score += (frame.first_bowl * 2) + frame.second_bowl
                    self.multipliers.pop(0)
                else:
                    self.score += frame.first_bowl*2
                    self.multipliers.pop(0)
        else:
            if frame.first_bowl == 10:
                self.score += frame.first_bowl
            elif frame.third_bowl == None:
                self.score += frame.first_bowl + frame.second_bowl
            else:
                self.score += frame.first_bowl + frame.second_bowl + frame.third_bowl

        if frame.first_bowl == 10:
            self.multipliers.append('X')
        elif frame.first_bowl+frame.second_bowl == 10:
            self.multipliers.append('/')
        
        # # if frame_num == 10:
        # print(self.frames)
            
        # print(self.score)
        # # print(len(self.multipliers))

        

    # def score(self):
    #     return self.frames



# What can a Player do?
# players can bowl and keep score
## If they don't get a strike, they can bowl twice per frame
### If they are on the tenth frame and bowl a strike or a spare, they can bowl a third time