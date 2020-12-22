# coding=utf-8
import copy
import re
# from functools import cache
import sys
import unittest
import itertools

def dec22():
    player1 = []
    with open('input.txt', 'r') as f:
        for cnt, line in enumerate(f):
            player1.append(int(line.strip()))

    player2 = []
    with open('input2.txt', 'r') as f:
        for cnt, line in enumerate(f):
            player2.append(int(line.strip()))

    print(player1)
    print(player2)
    round = 0
    while player1 and player2:
        round += 1
        card1 = player1.pop(0)
        card2 = player2.pop(0)
        print(f'Round {round}: \n Player 1 desk: {player1} \n Player 2 desk: {player2} \nPlayer 1 plays:{card1} \nPlayer2 plays:{card2}')
        if card1 > card2:
            player1.append(card1)
            player1.append(card2)
        elif card2 > card1:
            player2.append(card2)
            player2.append(card1)
    print(player1)
    print(player2)
    score = 0
    index = 0
    while player1:
        index += 1
        score += index * player1.pop()
    print(score)
    while player2:
        index += 1
        score += index * player2.pop()
    print(score)


next_game = 1


def play_rec(player1, player2, game):
    global next_game
    round = 0
    print(f'=== Game {game}===\n')
    mem = {}
    while player1 and player2:
        #  Before either player deals a card, if there was a previous round in this game that had exactly
        #  the same cards in the same order in the same players' decks, the game instantly ends in a win for player 1.
        p1str = "".join(map(str, player1))
        p2str = "".join(map(str, player2))
        if p1str in mem:
            if p2str in mem[p1str]:
                return 1
            else:
                mem[p1str][p2str] = 1
        else:
            mem[p1str] = {}

        round += 1
        output = f'-- Round {round} (Game {game}) --: \n' \
                 f'Player 1\'s desk: {", ".join(map(str, player1))} \n' \
                 f'Player 2 desk: {", ".join(map(str, player2))}\n'

        card1 = player1.pop(0)
        card2 = player2.pop(0)
        output += f'Player 1 plays: {card1} \nPlayer 2 plays: {card2}\n'
        winner = 0
        if card1 <= len(player1) and card2<= len(player2):
            output += f'Playing a sub-game to determine the winner...\n'
            print(output)
            next_game += 1
            winner = play_rec(copy.deepcopy(player1[:card1]), copy.deepcopy(player2[:card2]), next_game)

        if winner == 1 or (winner == 0 and card1 > card2):
            output += f'Player 1 wins round {round} of game {game}!\n'
            player1.append(card1)
            player1.append(card2)
        elif winner == 2 or (winner == 0 and card2 > card1):
            output += f'Player 2 wins round {round} of game {game}!\n'
            player2.append(card2)
            player2.append(card1)
        else:
            print('ERRRRRRRRROR')
        print(output)

    print(player1)
    if player1:
        return 1
    return 2


def dec22_2():
    player1 = []
    with open('input.txt', 'r') as f:
        for cnt, line in enumerate(f):
            player1.append(int(line.strip()))

    player2 = []
    with open('input2.txt', 'r') as f:
        for cnt, line in enumerate(f):
            player2.append(int(line.strip()))
    winner = play_rec(player1, player2, 1)

    score = 0
    index = 0
    while player1:
        index += 1
        score += index * player1.pop()
    print(score)
    while player2:
        index += 1
        score += index * player2.pop()
    print(score)


if __name__ == '__main__':
    # unittest.main()
    dec22_2()
