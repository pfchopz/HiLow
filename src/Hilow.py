#!/usr/bin/env python3
from os import system
from random import randint
from keyboard import is_pressed

# Class for individual card objects
class Card:
    def __init__(self, value, suit, strength):
        self.value = value
        self.suit = suit
        self.strength = strength

    def __repr__(self):
        return self.value + ' of ' + self.suit

def main():
    playGame(createDeck())

# Function which starts the gameplay loop
def playGame(deck, userInput = 0):
    # Shuffle deck and draw cards
    shuffleDeck(deck)
    cards = drawCards(deck, 2)
    
    # Create local variable for each card
    firstCard, secondCard = '???' if userInput == 0 else cards[0], cards[1]

    # Show cards to player
    system('cls||clear')   # Clear Screen
    print('King is high || Ace is low\n')
    print(f'First draw:  {firstCard}')
    print(f'Second draw: {secondCard}\n')

    # User input and game logic
    if userInput == 0: # Phase 1
        print('Guess if hidden card is higher or lower than shown card')
        print(' 1. Higher')
        print(' 2. Lower')

        # Wait for user input
        while True:
            if is_pressed('1'):
                playGame(cards, 1)
                break
            elif is_pressed('2'):
                playGame(cards, 2)
                break
            elif is_pressed('esc'):
                exit()

    else: # Phase 2
        # Determine if player won the round
        victory = False
        if userInput == 1:
            print('You guessed higher.')
            victory = True if firstCard.strength > secondCard.strength else False
        elif userInput == 2:
            print('You guessed lower.')
            victory = True if firstCard.strength < secondCard.strength else False

        # Print result of round
        print('YOU WIN!\n') if victory else print('YOU LOSE!\n')
        print('Press ENTER to play again, or ESC to quit.')

        # Wait for user input
        while True:
            if is_pressed('enter'):
                playGame(cards)
                break
            elif is_pressed('esc'):
                exit()

# Function to create a deck of 52 ordered cards
def createDeck():
    # Create lists for card creation
    deck = []
    cardValues = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 
                'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
    cardSuits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']

    # Loop to generate one of each card
    for suit in cardSuits:
        strength = 0
        for value in cardValues:
            strength += 1
            deck.append(Card(value, suit, strength))

    return deck

# Shuffle a deck of cards using Fisher-Yates algorithm
def shuffleDeck(deck):
    # Declare index variables
    currentIndex, randomIndex = len(deck), 0

    # Shuffle every index in deck'
    while currentIndex > 0:
        currentIndex -= 1
        # Select random index for shuffling
        randomIndex = randint(0, currentIndex)

        # Swap current card and random card
        deck[currentIndex], deck[randomIndex] = deck[randomIndex], deck[currentIndex]

    return deck

# Function to draw 'num' of cards
def drawCards(deck, num):
    
    # Draw cards from deck
    cards = []
    while num > 0:
        num -= 1
        cards.append(deck.pop())

    # Put cards back into deck for next hand
    deck.extend(cards.copy())

    return cards

if __name__ == '__main__':
    main()