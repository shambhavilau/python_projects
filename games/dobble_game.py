""" two cards are shown and both have only one character/symbol in common
    aim is to find the common symbol
"""
import string
import random

# print ascii letters
# print(string.ascii_letters)

symbols = []
symbols = list(string.ascii_letters)

card1 = [0]*5
card2 = [0]*5

pos1 = random.randint(0, 4)
pos2 = random.randint(0, 4)
# pos1 and pos2 are the same symbol positions in car1 and card2
same_symbol = random.choice(symbols)
symbols.remove(same_symbol)
if pos1 == pos2:
    card2[pos1] = same_symbol
    card1[pos1] = same_symbol
else:
    card1[pos1] = same_symbol
    card2[pos2] = same_symbol
    card1[pos2] = random.choice(symbols)
    symbols.remove(card1[pos2])
    card2[pos1] = random.choice(symbols)
    symbols.remove(card2[pos1])
i=0
while i<5:
    if i != pos1 and i != pos2:
        alphabet1 = random.choice(symbols)  # for card1
        symbols.remove(alphabet1)
        alphabet2 = random.choice(symbols)  # for card2
        symbols.remove(alphabet2)
        card1[i] = alphabet1
        card2[i] = alphabet2
    i += 1
print(card1)
print(card2)
ch = input("Spot the common symbol: ")
if ch == same_symbol:
    print("Correct! ")
else:
    print("Better Luck next time ")