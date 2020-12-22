# coding=utf-8
import copy
import hashlib
import json
import re
import sys
import unittest
import itertools

from operator import attrgetter



min_mana = 10000


class SnS:

    def __init__(self, state):
        self.hp = state['hp']
        self.mana = state['mana']
        self.ehp = state['ehp']
        self.edam = state['edam']
        self.shield = state['shield']
        self.poison = state['poison']
        self.recharge = state['recharge']
        self.spell = ''
        self.armor = 0
        self.total_mana = 0
        if self.shield:
            self.armor = 7

    def __str__(self):
        output = ''
        output += f'- Player has {self.hp} hit point, {self.armor} armor, {self.mana} mana\n'
        output += f'- Boss has {self.ehp} hit points'
        return output

    def __repr__(self):
        output = f'{self.hp} {self.mana} vs {self.ehp} {self.spell} '
        return str(output)

states = []


def sns_turn(game):
    # Take turn
    output = '-- Player turn --\n'
    output += str(game) + '\n'

    if game.poison:
        game.poison -= 1
        game.ehp -= 3
        output += f'Poison deals 3 damage; its timer is now {game.poison}\n'
    if game.recharge:
        game.recharge -= 1
        game.mana += 101
        output += f'Recharge provides 101 mana; its timer is now {game.recharge}.\n'
    if game.shield:
        game.shield -= 1
        output += f'Shields timer is now {game.shield}\n'
        if game.shield == 0:
            game.armor = 0
            output += f'Shield wears off, decreasing armor by 7.\n'

    if not game.spell:
        # print('Do nothing')
        pass
    elif game.spell == 'Missile':
        game.ehp -= 4
        game.mana -= 53
        game.total_mana += 53
        output += 'Player casts Magic Missile, dealing 4 damage'
    elif game.spell == 'Drain':
        game.ehp -= 2
        game.hp += 2
        game.mana -= 73
        game.total_mana += 73
        output += 'Player casts Drain, dealing 2 damage, and healing 2 hit points'
    elif game.spell == 'Shield':
        game.shield = 6
        game.armor = 7
        game.mana -= 113
        game.total_mana += 113
        output += 'Player cast Shield, increasing armor by 7.'
    elif game.spell == 'Poison':
        game.poison = 6
        game.mana -= 173
        game.total_mana += 173
        output += 'Player casts Poison'
    elif game.spell == 'Recharge':
        game.recharge = 5
        game.mana -= 229
        game.total_mana += 229
        output += 'Player casts Recharge'

    output += '\n-- Boss turn-- \n'
    output += str(game) + '\n'
    if game.poison:
        game.poison -= 1
        game.ehp -= 3
        output += f'Poison deals 3 damage; its timer is now {game.poison}\n'
    if game.recharge:
        game.recharge -= 1
        game.mana += 101
        output += f'Recharge provides 101 mana; its timer is now {game.recharge}.\n'
    if game.shield:
        game.shield -= 1
        output += f'Shields timer is now {game.shield}.\n'
        if game.shield == 0:
            game.armor = 0
            output += f'Shield wears off, decreasing armor by 7.\n'

    damage = game.edam - game.armor
    output += f'Boss attacks for {damage} damage\n'
    game.hp -= damage
    # print(output)


# Magic Missile costs 53 mana. It instantly does 4 damage.
# Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
# Shield costs 113 mana. It starts an effect that lasts for 6 turns. While it is active, your armor is increased by 7.
# Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the start of each turn while it is active, it deals the boss 3 damage.
# Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At the start of each turn while it is active, it gives you 101 new mana.

lowest_win = 1415

def add_turns(game):
    global states
    global lowest_win
    # Queue up next turn
    if game.ehp <= 0:
        if game.total_mana <= lowest_win:
            print('I WIN!', game.total_mana)
            lowest_win = game.total_mana
        # sys.exit()
    elif game.hp <= 0:
        #print('Loser')
        pass
    else:
        spells = [{'name': 'Missile', 'mana': 53},
                  {'name': 'Drain', 'mana': 73},
                  {'name': 'Shield', 'mana': 113},
                  {'name': 'Poison', 'mana': 173},
                  {'name': 'Recharge', 'mana': 229}]
        for spell in spells:
            next_game = copy.deepcopy(game)

            if next_game.mana < spell['mana']:
                # print('Skip negative mana')
                pass
            elif next_game.shield > 0 and spell['name'] == 'Shield':
                # print('Skip shield, one is active')
                pass
            elif next_game.poison > 0 and spell['name'] == 'Poison':
                # print('Skip Poison, one is active')
                pass
            elif next_game.recharge > 0 and spell['name'] == 'Recharge':
                # print('Skip Recharge, one is active')
                pass
            else:
                # print('Adding', spell['name'])
                next_game.spell = spell['name']
                states.append(next_game)

    # states = sorted(states, key=attrgetter('total_mana'))


def play_sns():
    global lowest_win
    global states
    spells = [{'name': 'Missile', 'mana': 53},
              {'name': 'Drain', 'mana': 73},
              {'name': 'Shield', 'mana': 113},
              {'name': 'Poison', 'mana': 173},
              {'name': 'Recharge', 'mana': 229}]

    lowest_win = 1415
    while len(states) > 0:
        # print(len(states), states[0].total_mana)
        game = states.pop(0)
        if game.total_mana <= lowest_win:

            sns_turn(game)
            add_turns(game)



def dec22():
    global states
    game_state = {'hp': 50, 'mana': 500, 'ehp': 59, 'edam': 9, 'shield': 0, 'poison': 0, 'recharge': 0}
    # game_state = {'hp': 10, 'mana': 250, 'ehp': 14, 'edam': 8, 'shield': 0, 'poison': 0, 'recharge': 0}
    sns = SnS(game_state)
    add_turns(sns)

    play_sns()



# class TestAll(unittest.TestCase):
#     def test_dec5_ids(self):
#         self.assertEqual(get_id('FBFBBFFRLR'), 357)
#         self.assertEqual(get_id('BFFFBBFRRR'), 567)
#         self.assertEqual(get_id('FFFBBBFRRR'), 119)
#         self.assertEqual(get_id('BBFFBBFRLL'), 820)

if __name__ == '__main__':
    # unittest.main()
    dec22()
