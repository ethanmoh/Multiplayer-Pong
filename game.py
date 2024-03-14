class Game:
    def __init__(self):
        self.ready = False
        self.close = False
        self.p0 = 0
        self.p1 = 0
        self.p0lives = 10
        self.p1lives = 10
    
    def connected(self):
        return self.ready