class Bowling_player(object):

    def __init__(self, overall = 0):
        self.overall = overall

    def frames(self):
        shot_one = int(input('  on first shot:'))

        if shot_one == 10: # this is a strike
            shot_two_after_strike = int(input('  on shot after strike:'))

            if shot_two_after_strike == 10: # you got another strike. continue the frame!
                shot_three_after_strike = int(input('  on shot after two strikes:'))
                self.overall += (shot_three_after_strike + shot_two_after_strike + shot_one)
                return self.overall

            else:# you did not get another strike, frame over.
                self.overall += (shot_one + shot_two_after_strike)
                return self.overall

        elif shot_one < 10:
            shot_two = int(input('  on second shot:'))
            shots = shot_one + shot_two

            if shots == 10: # this is a spare          
                shot_three_after_spare = int(input('  on shot after spare'))  
                self.overall += (shots + shot_three_after_spare)
                return self.overall

            else: # you suck at bowling 
                self.overall += shots
                return self.overall

                
total_score = 0

for i in range(10):
    print(i+1 , 'Frame : ')
    sub_frame = Bowling_player(total_score)
    total_score=sub_frame.frames()

print('Total_score : ', total_score)