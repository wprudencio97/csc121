#William Prudencio, chapter 9 - lab 9, 10/05/19

''' This program will simulate a simple game of blackjack. Each 
player will be handed the amount of cards chosen by the user until
one or both players exceed 21. The program will continue until
there are no cards left on the deck. '''

#----------define the main function-------------
def main():
    #create a deck of cards 
    cardDeck = createCardDeck()
    #number of cards to deal
    cardsToDeal = int(input("How many cards should I deal? "))
    #deal the cards 
    deckLeft = dealCards(cardDeck, cardsToDeal)

    #create loop to continue until no cards are left
    while len(deckLeft) > cardsToDeal * 2:
        deckLeft = dealCards(deckLeft, cardsToDeal)
    else:
        if cardsToDeal * 2 > len(deckLeft):
            #split the cards evently for the last round!
            cardsToDeal = int(len(deckLeft) / 2)
        deckLeft = dealCards(deckLeft, cardsToDeal)

#--------define the card dealer function-------------
def dealCards(cardDeck, cardsToDeal):
    player1, player2 = 0, 0 #create the players 
    import random #import random to select random cards

    while player1 <= 21 and player2 <= 21:
        #check that the cards to be dealt are not more than the ones on deck
        if cardsToDeal > len(cardDeck):
            cardsToDeal = len(cardDeck)
            if cardsToDeal == 0:
                break
            
        #deal the cards and accumulate their value
        print("---------Player 1---------")
        for count in range(cardsToDeal):
            #select a random card using random
            card, value = random.choice(list(cardDeck.items()))
            cardDeck.pop(card) #remove the card from the card deck
            print(card)# print the card
            #check for ace
            if value == 1 and player1 < 11:
                value = 11
            player1 += value #accumulate the card's value
            
        #print the Value on the dealt hand
        print("Value on hand: ", player1) 

        print("---------Player 2---------")
        for count in range(cardsToDeal):
            #select a random card using random
            card, value = random.choice(list(cardDeck.items()))
            cardDeck.pop(card) #remove the card from the card deck
            print(card)# print the card
            #check for ace
            if value == 1 and player2 < 11:
                value = 11
            player2 += value #accumulate the card's value 

        #print the Value on the dealt hand
        print("Value on hand: ", player2) 

    if player1 > 21 and player2 <= 21:
        print("\nPLAYER TWO WINS!!!\n")
    elif player2 > 21 and player1 <= 21:
        print("\nPLAYER ONE WINS!!!\n")
    elif player1 > 21 and player2 > 21:
        print("\nIT'S A DRAW!!!\n")

    print("\nRemaining cards: ",len(cardDeck),"\n")    
    return cardDeck

#--------define the deck creator function------------
def createCardDeck():
    #dictionary with each card and their values 
    cards = {"Ace of Spades":1, "2 of Spades":2, "3 of Spades":3, 
            "4 of Spades":4, "5 of Spades":5, "6 of Spades":6,
            "7 of Spades":7, "8 of Spades":8, "9 of Spades":9,
            "10 of Spades": 10, "Jack of Spades":10,
            "Queen of Spades":10, "King of Spades":10,

            "Ace of Hearts":1, "2 of Hearts":2, "3 of Hearts":3, 
            "4 of Hearts":4, "5 of Hearts":5, "6 of Hearts":6,
            "7 of Hearts":7, "8 of Hearts":8, "9 of Hearts":9,
            "10 of Hearts": 10, "Jack of Hearts":10,
            "Queen of Hearts":10, "King of Hearts":10,

            "Ace of Clubs":1, "2 of Clubs":2, "3 of Clubs":3, 
            "4 of Clubs":4, "5 of Clubs":5, "6 of Clubs":6,
            "7 of Clubs":7, "8 of Clubs":8, "9 of Clubs":9,
            "10 of Clubs": 10, "Jack of Clubs":10,
            "Queen of Clubs":10, "King of Clubs":10,

            "Ace of Diamonds":1, "2 of Diamonds":2, "3 of Diamonds":3, 
            "4 of Diamonds":4, "5 of Diamonds":5, "6 of Diamonds":6,
            "7 of Diamonds":7, "8 of Diamonds":8, "9 of Diamonds":9,
            "10 of Diamonds": 10, "Jack of Diamonds":10,
            "Queen of Diamonds":10, "King of Diamonds":10 }

    return cards

#Call the main function to run the program
main()