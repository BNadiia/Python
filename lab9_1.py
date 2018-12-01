#!/usr/bin/env python3

def count_cards(cards: str) -> int:
    cards = cards.split()
    
    card_table = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,\
    '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 0}
    
    amount = sum([card_table[_] for _ in cards])
    
    if 'A' in cards:
        ace_score = 21 - amount
        if ace_score < 1: amount += 1
        elif ace_score > 11: amount += 11
        else: amount += ace_score
    return amount

def ui_output(result: int) -> None:
    if(result > 21): print("Bust")
    else: print(result)

ui_output(count_cards(input("Input your cards: ")))
