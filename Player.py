class Player(object):
    def __init__(self, player_name, initial_card):
        self.name = player_name
        self.cards = [initial_card]
        self.points = initial_card
        self.is_playing = True
    
    def __str__(self):
        cards = " - ".join(str(e) for e in self.cards)
        return f"""{self.name}
  Cartas  => {cards}
  Pontos => {self.points}"""

    def add_card(self, card):
        self.points += card
        return self.cards.append(card)
    
    def check_points(self):
        if self.points >= 21:
            self.stop_playing()
            return
    
    def stop_playing(self):
        self.is_playing = False