# BLACKJACK GAME
# 1 Computer Dealer
# 1 Human Player
# Player can place a bet
# Player Actions: Hit, Stand
# Face Cards(Jack, Queen, King) count as value of 10
# Ace can count as 1 or 11(maybe ask player if they have)

# Game Play:
# 1. Create a deck of 52 cards
# 2. Shuffle the deck
# 3. Ask the Player for their bet
# 4. Make sure the Player's bet does not exceed their available chips
# 5. Deal two cards to the Dealer and two cards to the Player
# 6. Show only one of the Dealer's cards, the other remains hidden
# 7. Show both of the Player's cards
# 8. Ask the Player if they wish to Hit, and take another card
# 9. If the Player's hand doesn't Bust(over 21), ask if they'd like to Hit again.
# 10. If a Player Stands, play the Dealer's hand. 
# The dealer will always Hit until the Dealer's value meets or exceeds 17
# 11. Determine the winner and adjust the Player's chips accordingly
# 12. Ask the Player if they'd like to play again

import random

suits = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace')
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

class Card:
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        if self.rank in ('Jack', 'Queen', 'King', 'Ace'):
            return self.rank + f'({self.value}) of ' + self.suit
        return self.rank + ' of ' + self.suit
        
class Deck:
    
    def __init__(self):
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                # Create the Card Object
                created_card = Card(suit, rank)
                
                self.all_cards.append(created_card)
                
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()
        
class Player:
    
    def __init__(self):
        self.hand = []
        
    def add_card(self, new_card):
        self.hand.append(new_card)
        
    def sum_of_hand(self):
        total = 0
        
        for num in self.hand:
            total += num.value
            
        return total
        
    def show_hand(self):
        for card in self.hand:
            print(card)
        
    def __str__(self):
        return f'Player has {len(self.hand)} cards.'
        
class Gamer(Player):
    
    def __init__(self, balance):
        Player.__init__(self)
        self.balance = balance
        
    def bet(self, ammount):
        if ammount > self.balance:
            print('Insufficient funds')
        else:
            self.balance -= ammount
            print(f'You bet ${ammount}')
            
class Dealer(Player):
    def __init__(self):
        Player.__init__(self)
        self.hand = []
    
    def show_initial_dealer_hand(self):
        print(self.hand[0])
        print('HIDDEN')
        
def blackjack():
    player = Gamer(1000)
    dealer = Dealer()
    
    deck1 = Deck()
    deck1.shuffle()
    
    # Deal initial hand
    for _ in range(2):
        player.add_card(deck1.deal_one())
        dealer.add_card(deck1.deal_one())
    
    dealer.sum_of_hand()
    player.sum_of_hand()
    
    print('### IT\'S TIME TO PLAY THE GAME ###\n\n')
      
    blackjack_game = True
    
    while blackjack_game:
        player_turn = True
        dealer_turn = True
        bet_on = False
        current_dealer_hand = 0
        current_player_hand = 0
        player_decision = ''
        
        print('Dealer Hand:')
        dealer.show_initial_dealer_hand()
    
        print('\nPlayer hand:')   
        player.show_hand()
        
        while bet_on is False:
            bet_ammount = int(input(f'\nPlease place your bet(Current balance: ${player.balance}): '))
            
            if bet_ammount > player.balance:
                player.bet(bet_ammount)
                bet_on = False
            else:
                player.bet(bet_ammount)
                bet_on = True
        
        
        while player_turn:
            print('\n\n### PLAYER\'S TURN ###\n\n')
            while player_decision not in ('1', '2'):
                player_decision = input('Hit or Stand? Type 1 for Hit or 2 for Stand: ')
            
                if player_decision == '1':
                    player.add_card(deck1.deal_one())
                    current_player_hand = player.sum_of_hand()
                
                    print('\nDealer Hand:')
                    dealer.show_initial_dealer_hand()
                    
                    print('\nPlayer hand:')   
                    player.show_hand()
                
                    if current_player_hand > 21:
                        for find_eleven in player.hand:
                            if find_eleven.value == 11:
                                change_eleven = ''
                                
                                while change_eleven not in ('y', 'n'):
                                    change_eleven = input('You are over 21, but have an Ace. Would you like to change its value to 1 in order to continue playing(y/n): ')
                                    
                                    if change_eleven == 'y':
                                        find_eleven.value = 1
                                        current_player_hand = player.sum_of_hand()                                  
                                        
                                        print('\nDealer Hand:')
                                        dealer.show_initial_dealer_hand()
                                        
                                        print('\nPlayer hand:')   
                                        player.show_hand()
                                        
                                        player_decision = ''
                                        break
                                    
                                    else:
                                        print('\nPlayer is BUST!')
                                        print(f'Dealer wins and Player lost ${bet_ammount}')
                                        
                                        player_turn = False
                                        dealer_turn = False
                                        blackjack_game = False

                                        break

                                if current_player_hand <= 21:
                                    break
                        
                            # else:
                            #     print('\nPlayer is BUST!')
                            #     print(f'Dealer wins and Player lost ${bet_ammount}')
                                
                            #     player_turn = False
                            #     dealer_turn = False
                            #     blackjack_game = False
                                
                            #     break
                        
                    elif current_player_hand == 21:
                        print('\nPlayer WINS!')
                        print(f'Player wins ${bet_ammount * 2}')
                        
                        player.balance += (bet_ammount * 2)
                        player_turn = False
                        dealer_turn = False
                        blackjack_game = False
                        
                    else:
                        player_decision = ''
                        break
                
                else:
                    player_turn = False
        
        while dealer_turn:
            print('\n\n### DEALER\'s TURN ###\n\n')
            
            current_dealer_hand = dealer.sum_of_hand()
            
            print('Dealer Hand:')
            dealer.show_hand()
            
            print('\nPlayer hand:')   
            player.show_hand()
            
            if current_dealer_hand > 21:
                print('\nDealer is BUST!')
                print(f'Player wins ${bet_ammount * 2}')
                
                dealer_turn = False
                blackjack_game = False
                
            elif current_dealer_hand in (21, current_player_hand):
                print(f'\nDealer wins and Player lost ${bet_ammount}')
                
                dealer_turn = False
                blackjack_game = False
                
            elif current_dealer_hand < 17:
                dealer.add_card(deck1.deal_one())
                continue
            
            elif current_dealer_hand >= 17 and current_dealer_hand < 21:
                if current_dealer_hand >= current_player_hand:
                    print(f'\nDealer wins and Player lost ${bet_ammount}')
                    
                    dealer_turn = False
                    blackjack_game = False
                else:
                    print(f'\nPlayer wins ${bet_ammount * 2}')
                    
                    
                    player.balance += (bet_ammount * 2)
                    dealer_turn = False
                    blackjack_game = False
        
        if blackjack_game is False:
            if player.balance == 0:
                print('\nOut of funds! Back to work :}')
                print(f'Player left the table with: ${player.balance}')
                
                break
            
            replay = input('Would you like to play again?(y/n):')
            
            if replay == 'y':
                player.hand = []
                dealer.hand = []
                
                blackjack_game = True
                
            else:
                print(f'\nPlayer left the table with: ${player.balance}')
    
blackjack()
