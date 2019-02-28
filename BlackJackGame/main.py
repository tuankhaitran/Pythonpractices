'''
CREAT A BLACKJACK GAME

'''

'''
Create variables to store value of the decks
'''

import random

suits=["Heart","Spade","Club","Diamond"]
ranks=['One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace']
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}


#Card class to handle
class Card():
    def __init__(self,suit,rank):
        self.rank=rank
        self.suit=suit
        
    def __str__(self):
        return(f"{self.rank} of {self.suit}")

#Deck Class represent the deck on the table. The deck has 52 cards. You should be able to shuffle it and also take take card out of the deck.
class Deck():
    mydeck=[]

    def __init__(self,suits,ranks):
        self.ranks=ranks
        self.suits=suits
        for suit in self.suits:
            for rank in self.ranks:
                self.mydeck.append(Card(suit,rank))

    def __str__(self):
        dec_com = ''
        for card in self.mydeck:
            dec_com += '\n' + card.__str__()
        return dec_com
    
    def shuffle(self):
        random.shuffle(self.mydeck)

    def deal(self):
        return self.mydeck.pop()

# This class is basically representation of player, they can add card and check ace. They should be able to bet too??
class Hand():
    def __init__(self):
        self.cards=[]
        self.value=0
        self.hasace=False

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank=='Ace':
            self.hasace = True
    def check_ace(self):
        while self.value>21 and self.hasace:
            self.value-=10
            self.hasace=False
        

  


class Chip():
    def __init__(self,totalchips=100):
        self.totalchips=totalchips
        self.betchips=0
    
    def win_bet(self):
        self.totalchips += (self.betchips*2)
    
    def take_bet(self):
        while True:
            try:
                self.betchips=int(input("How much do you want to bet? "))
            except: 
                print("Invalid input, Please enter an integer: ")
            else:
                if self.betchips <= self.totalchips:
                    self.totalchips-=self.betchips
                    break
                else:
                    print(f"You cannot bet more than what you have!!! You have {self.totalchips} but you bet {self.betchips}")
    



def hit_or_stay(deck,hand):
    while True:
        answer=input("What will you do? hit or stay ? h/s: ")
        if (answer[0].lower()=='h'):
            hand.add_card(deck.deal())
            hand.check_ace()
            print("Player've drawn a card from the deck")
            
            
        elif (answer[0].lower()=='s'):
            print("Player choose stay, Computer turn!!")
            break
        else:
            print("Please input H or S!! ")

def player_bust(player,computer,compchips):
    print("\n*****************************")
    print("Player busted!! Computer win")
    print("*****************************\n")
    compchips.win_bet()

def player_win(player,computer,playerchips):
    print("\n*****************************")
    print("Player win!")
    print("*****************************\n")
    playerchips.win_bet()

def comp_bust(player,computer,playerchips):
    print("\n*****************************")
    print("Computer busted, Player win!!")
    print("*****************************\n")

    playerchips.win_bet()

def comp_win(player,computer,compchips):
    print("\n*****************************")
    print("Computer win!!!")
    print("*****************************\n")
    compchips.win_bet()

def draw(playerchips,compchips):
    print("\n*****************************")
    print("Its a draw!!!")
    print("*****************************\n")
    playerchips.totalchips+=playerchips.betchips
    compchips.totalchips+=compchips.betchips


def showcard(player,computer):
    
    print("\nPlayer cards: ")
    for card in player.cards:
        print(card)
    print("\nComputer cards: ")
    print(computer.cards[0])

def showallcards(player,computer):
    print("Player cards: ")
    for card in player.cards:
        print(card)
    print("\nComputer cards: ")
    for card in computer.cards:
        print(card)

def play_game():
    print("******************************************")
    print("*                                        *")
    print("* WELCOME TO BLACKJACK GAME ON PYTHON!!! *")
    print("*                                        *")
    print("******************************************")

    thedeck = Deck(suits, ranks)  # Create a Deck object
    thedeck.shuffle()  # Shuffle the deck

    # Create player hand, give them 2 cards
    player = Hand()
    player.add_card(thedeck.deal())
    player.add_card(thedeck.deal())

    #Create computer hand, give them 2 cards
    computer = Hand()
    computer.add_card(thedeck.deal())
    computer.add_card(thedeck.deal())

    while True:
        try:
            initchip = int(
                input("How much chips do you want to start with ???: "))
        except:
            print("Invalid input, Please enter an integer: ")
        else:
                break

    playerchips = Chip(initchip)    # Create an Chip object
    computerchips = Chip(initchip)

    playerchips.take_bet()  # Ask the player to bet

    print(f"Player've just bet {playerchips.betchips}")

    # Make computer bet the chips automatically based on player bet
    computerchips.betchips = playerchips.betchips
    computerchips.totalchips -= computerchips.betchips

    print(f"Computer follows player bet {computerchips.betchips}")

    # Show 2 cards of the players and 1 card of the computer
    showcard(player, computer)

    hit_or_stay(thedeck, player)  # Ask Player if they want to hit or stay

    showcard(player, computer)  # Show card again

    # Control gameplay of the computer
    if player.value > 21:
        player_bust(player, computer, computerchips)

    while player.value >= computer.value and player.value <= 21:
        computer.add_card(thedeck.deal())
        computer.check_ace()
        if player.value < computer.value and computer.value <=21:
            comp_win(player,computer,computerchips)
            break
        elif player.value == computer.value:
            draw(playerchips,computerchips)
            break
        else:
            comp_bust(player, computer, playerchips)
            break

    else:
        comp_win(player,computer,computerchips)

    print("\nCARDS REVEALED!!!")
    showallcards(player, computer)
    print("\nResults:")
    print(f"The total chips of the player are: {playerchips.totalchips}")
    print(f"The total chips of the computer are: {computerchips.totalchips}")

    print(f"\n End game!!\n")


    
play_game()
