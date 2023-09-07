import random

# Initialize deck
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']#Make all four suits
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']#Make all the card ranks
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}#Make the values of each card

# Functions
def deal_card():#Defines deal_card as a function below
    suit = random.choice(suits)#Program randomly selects an item from the suits list 
    rank = random.choice(ranks)#Program randomly selects an item from the ranks list 
    return (rank, suit)#Returns to the two random choices

def calculate_hand_value(hand):#Defines the calculated hand value and introduces hand as a variable
    value = sum([values[card[0]] for card in hand])#Sets the value equal to the sum of the cards in your hand
    num_aces = sum([1 for card in hand if card[0] == 'Ace'])#Sets the number of ace equal to the sum of the function
    
    while value > 21 and num_aces:#While the sum of your hand is more then 21 when you have an ace
        value -= 10#Subtract 10
        num_aces -= 1#Sets the ace equal to 1
    
    return value#Returns the new value

# Game setup
player_hand = [deal_card(), deal_card()]#Sets the player hand to the two cards dealt
dealer_hand = [deal_card(), deal_card()]#Sets the dealers hand to the two cards dealt

# Game loop
while True:#While the following applies
    player_value = calculate_hand_value(player_hand)#Sets the player hand equal to the calculated value of the sum of their hand
    dealer_value = calculate_hand_value(dealer_hand)#Sets the dealer hand equal to the calculated value of the sum of their hand
    
    print("\nYour hand:", player_hand, "Value:", player_value)#Prints the players hand 
    print("Dealer's hand:", [dealer_hand[0], 'Hidden'])#Prints the dealers hand
    
    if player_value == 21:#If the player hand equals 21
        print("Blackjack! You win!")#Prints that you win
        break#Break program
    elif player_value > 21:#If the player hand equals more then 21 
        print("Bust! You lose.")#prints you lose
        break#breaks program
    
    action = input("Do you want to 'hit' or 'stand'? ").lower()#Program asks if you want to hit or stand
    
    if action == 'hit':#If the player hits
        player_hand.append(deal_card())#Deal another card
    elif action == 'stand':#If the player stands
        while dealer_value < 17:#While the dealer hand is less then 17
            dealer_hand.append(deal_card())# deal a card to the player
            dealer_value = calculate_hand_value(dealer_hand)#Calculate the players hand sum
        
        print("Dealer's hand:", dealer_hand, "Value:", dealer_value)#Prints the dealer hand 
        
        if dealer_value > 21 or player_value > dealer_value:#If the dealer hand is more then 21 or the less then the player value
            print("You win!")# prints you win
        elif dealer_value > player_value:#If the dealer value is more then the player value
            print("Dealer wins.")#prints dealer wins
        else:#Other then that
            print("It's a tie!")# Print its a tie
        
        break# breaks program