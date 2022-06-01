
class LeaderBoard():
    
    _table = {}

    @classmethod
    def addWinner(cls, position, name):
        
        cls._table[position] = name
    
    @classmethod
    def print(cls):

        return cls._table


class Game1():

    def __init__(self):

        self.leaderBoard = LeaderBoard()


    def addWinner(self, pos, name):
        self.leaderBoard.addWinner(pos, name)



class Game2():

    def __init__(self):

        self.leaderBoard = LeaderBoard()


    def addWinner(self, pos, name):
        self.leaderBoard.addWinner(pos, name)



g1 = Game1()
g1.addWinner(1, "Real Madrid")

g2 = Game2()
g2.addWinner(2, "Liverpool")

print(LeaderBoard.print())

lb1 = LeaderBoard()
lb1.addWinner(1, "Arsenal")

print(LeaderBoard.print())