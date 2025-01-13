import random

class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.scoreboard = Scoreboard()
        self.current_frame = 0

class Scoreboard:
    def __init__(self):
        self.total_score = 0
        self.frames = [Frame() for _ in range(9)]
        self.frames.append(Frame(is_last=True))

    def __repr__(self):
        return f'Total score: {self.total_score} \nFrames: {self.frames} \n'


class Frame:
    def __init__(self, is_last=False):
        self.score = 0
        self.is_last = is_last
        if not is_last:
            self.rolls = [None] * 2
        else:
            self.rolls = [None] * 3

    def __repr__(self):
        return f'Score: {self.score} Rolls: {self.rolls} \n'

class BowlingAlley:
    def __init__(self, players):
        self.players = players
        self.current_player = 0

    def is_game_over(self):
        for player in self.players:
            if player.current_frame < 10:
                return False
        return True
    
    def simulate_frame(self, frame):
        pin_count = 10
        for idx in range(2):
            pin_dropped = random.randint(0, pin_count)
            pin_count -= pin_dropped
            frame.score += pin_dropped
            frame.rolls[idx] = pin_dropped
            if pin_count == 0:
                if idx == 0:
                    frame.rolls[0] = ''
                    frame.rolls[1] = 'X'
                    break
                elif idx == 1:
                    frame.rolls[1] = '/'
        

    def sumulate_last_frame(self, frame):
        pin_count = 10

        for idx in range(2):
            pin_dropped = random.randint(0, pin_count)
            pin_count -= pin_dropped
            frame.score += pin_dropped
            frame.rolls[idx] = pin_dropped
            if pin_count == 0:
                if idx == 0:
                    frame.rolls[1] = 'X'
                elif idx == 1:
                    frame.rolls[2] = '/'
                pin_count = 10

        if frame.is_last:
            pin_dropped = random.randint(0, pin_count)
            frame.score += pin_dropped
            if pin_dropped == 10:
                frame.rolls[2] = 'X'
            elif pin_count == 0:
                frame.rolls[2] = '/'
            else:
                frame.rolls[2] = pin_dropped          

    def simulate_game(self):
        while not self.is_game_over():
            player = self.players[self.current_player]
            if player.current_frame >= 10:
                continue
            frame = player.scoreboard.frames[player.current_frame]        

            if not frame.is_last:
                self.simulate_frame(frame)
            else:
                self.sumulate_last_frame(frame)

            player.scoreboard.total_score += frame.score
            player.current_frame += 1
            self.current_player = (self.current_player + 1) % len(self.players)

    def print_winner(self):
        print('Printing winner')
        if not self.is_game_over():
            print('Game not played yet!')
            return
        
        winner = None
        max_score = 0
        for player in self.players:
            if player.scoreboard.total_score > max_score:
                max_score = player.scoreboard.total_score
                winner = player
        if winner:
            print(f'Winner is: {winner.name}')