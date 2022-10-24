import random


class Card:
    def __init__(self, suit, symbol, value):
        self.symbol = symbol
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.suit} {self.symbol}"


class Deck:
    def __init__(self):
        self.cards = []
        symbols = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        suits = ['Heart', 'Tile', 'Clover', 'Pike']
        for suit in suits:
            for value, symbol in enumerate(symbols):
                self.cards.append(Card(suit, symbol, value))

    def shuffle(self):
        random.shuffle(self.cards)


class Pile:
    def __init__(self):
        self.cards = []

    def draw_cards(self, deck, num):
        for _ in range(num):
            self.cards.append(deck.cards.pop())

    def put_card(self):
        return self.cards.pop()

    def collect_win(self, stake):
        self.cards.extend(stake)

    def __len__(self):
        return len(self.cards)


class Game:
    def __init__(self):
        deck = Deck()
        deck.shuffle()
        self.pile1 = Pile()
        self.pile2 = Pile()
        self.pile1.draw_cards(deck, 26)
        self.pile2.draw_cards(deck, 26)
        self.round = 0
        self.is_over = False

    def is_war(self, card1, card2):
        return card1.value == card2.value

    def battle(self):
        card1 = self.pile1.put_card()
        card2 = self.pile2.put_card()
        return card1, card2

    def game_status(self):
        print(f'Pile 1: {len(self.pile1)} cards')
        print(f'Pile 2: {len(self.pile2)} cards')

    def compare_cards(self):
        self.round += 1
        print(f'------------------')
        print(f'ROUND {self.round}')
        print(f'------------------')
        stake = []
        card1, card2 = self.battle()
        stake.append(card1)
        stake.append(card2)

        while self.is_war(card1, card2):
            print(f'{card1} = {card2}')
            print('WAR TIME!')
            if len(self.pile1) < 4 or len(self.pile2) < 4:
                self.is_over = True
                self.game_status()
                print('GAME OVER!')
                return
            for _ in range(3):
                stake.append(self.pile1.put_card())
                stake.append(self.pile2.put_card())
            card1, card2 = self.battle()
            stake.append(card1)
            stake.append(card2)

        if card1.value > card2.value:
            self.pile1.collect_win(stake)
            print(f'{card1} > {card2}')
        elif card1.value < card2.value:
            self.pile2.collect_win(stake)
            print(f'{card1} < {card2}')

        self.game_status()
        if len(self.pile1) < 1 or len(self.pile2) < 1:
            self.is_over = True
            print('GAME OVER!')


game = Game()
while not game.is_over:
    game.compare_cards()
