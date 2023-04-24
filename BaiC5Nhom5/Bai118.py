from random import randrange
def createDeck():
    cards = []
    for suit in ["s", "h", "d", "c"]:
        for value in ["2", "3", "4", "5", "6", "7", "8", "9", \
            "T", "J", "Q", "K", "A"]:
            cards.append(value + suit)
    return cards 
def shuffle(cards):
    for i in range(0, len(cards)):
        pos = randrange(0, len(cards))
        t = cards[i]
        cards[i] = cards[pos]
        cards[pos] = t
        
def main():
    cards = createDeck()
    print("The original deck of cards is: ")
    print(cards)
    print()
    
    shuffle(cards)
    print("The shuffled deck of cards is: ")
    print(cards)
    
main()