import random
# https://www.youtube.com/watch?v=8QTsK1aVMI0&t=1133s - used as a guide on how to go about creating the game in the shell form
# Used to Create All the Cards - https://stackoverflow.com/questions/41970795/what-is-the-best-way-to-create-a-deck-of-cards/41970851
# How to use classes with functions, __init__, __str__, (sel)f - https://www.youtube.com/watch?v=wfcWRAxRVBA

playing = True # We will use gloabal logic to coninuosly play the game

suits = ('Spades', 'Clubs', 'Hearts', 'Diamonds')
names = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King')
values = {'Ace': 11, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10}

class individualCardCreator:
    def __init__ (self, suit, name):
        self.suit = suit
        self.name = name
    
    def __str__ (self):
        return self.name + ' of ' + self.suit

class Deck:                             # Creates a deck 
    def __init__(self):
        self.deck = []                  # Initializes deck list
        for suit in suits:
            for suitNumb in names:
                self.deck.append(individualCardCreator(suit, suitNumb))
    
    def shuffle(self):
        random.shuffle(self.deck)       # Shuffles deck
    def deal(self):
        dealt_card = self.deck.pop()    # Picks a card from the deck, and removes it
        return dealt_card               # Returns picked card

class Hand:
    def __init__(self):
        self.cards = []                 # Creats the hand
        self.value = 0                  # Initializes the hand value
        self.aces = 0                   # Need to account for aces b/c troublesome

    def add_card(self, card):           # adds card to the player's or dealer's hand
        self.cards.append(card)
        self.value += values[card.name]
        if card.name == 'Ace':
            self.aces += 1

    def ace_adjust(self):
        while self.value > 21 and self.aces:
            self.value -= 10            # Accounts for Ace counting as 11, or 1 when the hand total is over 21
            self.aces -=1               # Removes the count of ace after it is accounted for once, this allows for the loop to run twice just in case there is a senario of double aces


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.ace_adjust()

def HoS(deck, hand):
    global playing

    while True:
        HorS = input("\nHit or Stand? (Enter 'h' to hit or 's' to stand) ")
        
        if HorS[0].lower() == 'h':
            hit(deck, hand)
        elif HorS[0].lower() == 's':
            print("You have chosen to stand. The deal will play his turn now.")
            playing = False                     # Ends global 'True' on play, everything is now automatic
        else:
            print("Invalid input. Try again!")
            continue
        break                                   # https://www.tutorialspoint.com/python/python_loop_control.htm

def hidden(player, dealer):
    print("\nDealer's Hand: ")
    print(" <card hidden>")
    print("", dealer.cards[1])
    print("\nPlayer's Hand: ", *player.cards, sep='\n ')

def shown(player, dealer):
    print("\nDealer's Hand: ", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand: ", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)

class Bank:
    def __init__(self):
        self.total = 1000
        self.bet = 0
    
    def betW(self):
        self.total += self.bet

    def betL(self):
        self.total -= self.bet

def wager(cash):
    while True:
        try:
            cash.bet = int(input("How much money would you like to wager? (Enter dollar amount) "))
        except ValueError:                      # https://www.journaldev.com/33500/python-valueerror-exception-handling-examples#:~:text=Python%20ValueError%20is%20raised%20when,precise%20exception%20such%20as%20IndexError.
            print("Invalid input. Please enter the amount of money you would like to bet: ")
        else:
            if cash.bet > cash.total:
                print("Your bet cannot exceed: $1000!")
            else:
                break


# Game Situations

def playerL(player, dealer, cash):         # Player Wins
    print("PLAYER LOSES!")
    cash.betL()

def playerW(player, dealer, cash):          # Player Loses
    print("PLAYER WINS!")
    cash.betW()

def dealerW(player, dealer, cash):          # Dealer Wins
    print("DEALER WINS!")
    cash.betL()

def dealerL(player, dealer, cash):         # Dealer Loses
    print("DEALER LOSES!")
    cash.betW()

def tie(player, dealer):                        # Tie
    print("Player and Dealer tie!")

# Game
while True:
    print("WELCOME TO BLACK JACK!")

    deck = Deck()                       # Creates a deck with 52 cards
    deck.shuffle()                      #Shuffles a 52 card deck

    playerH = Hand()                    # Creates a player hand
    dealerH = Hand()                    # Creates a dealer hand
    
    playerH.add_card(deck.deal())       # 1st Player Card
    playerH.add_card(deck.deal())       # 2nd Player Card

    dealerH.add_card(deck.deal())       # 1st Dealer Card
    dealerH.add_card(deck.deal())       # 2nd Dealer Card
    
    player_bank = Bank()                # Creates a bank for the player with an intial amount of $1000

    wager(player_bank)                  # Allows for a way to take in wager

    hidden(playerH, dealerH)            # Prints hands, 1 of dealer card is hidden

    while playing:
        HoS(deck, playerH)
        hidden(playerH, dealerH)

        if playerH.value > 21:
            playerL(playerH, dealerH, player_bank)

    if playerH.value <= 21:
        
        while dealerH.value < 17:
            hit(deck, dealerH)
        shown(playerH, dealerH)

        if dealerH.value > 21:
            dealerL(playerH, dealerH, player_bank)

        elif dealerH.value > playerH.value:
            dealerW(playerH, dealerH, player_bank)

        elif dealerH.value < playerH.value:
            playerW(playerH, dealerH, player_bank)

        if playerH.value > 21:
            playerL(playerH, dealerH, player_bank)

    print("\nPlayer's bank: ", player_bank.total)

    new_game = input("\nWould you like to play again? Enter 'y' or 'n': ")
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("\nThanks for playing!")
        break 