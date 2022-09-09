import random

class Game(object):
    def __init__(self):
        self.__cards = [1,2,3,4,5,6,7,8,9,10,10,10]
    
    def shuffle(self):
        random.shuffle(self.__cards)
    
    def get_card(self):
        card = random.choice(self.__cards)
        self.__cards.remove(card)
        return card
    
    def round(self, player):
        self.shuffle()
        player.add_card(self.get_card())
        player.check_points()
        return
    
    def winner(self, player1,player2):
        p1 = player1.points
        p2 = player2.points

        if p1 == p2:
            return "Empate!!"
        if p1 <= 21 and p2 > 21:
            return f"{player1.name} venceu!!"
        if p2 <= 21 and p1 > 21:
            return f"{player2.name} venceu!!"
        if p1 > p2:
            return f"{player1.name} venceu!!"
        return f"{player2.name} venceu!!"
