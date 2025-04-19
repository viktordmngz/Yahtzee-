'''
STILL WORKING ON THIS

Created by: Viktor Dominguez
Date Created: 04/18/2025  (MM/DD/YYYY)
Last Updated: 04/18/2025  (MM/DD/YYYY)
Editor: Python IDLE


========
LICENSE
========
None, but some credit is always appreciated :)


=====
NOTE
=====

This code is intended to run in a terminal/console.
If the code does not work with your computer, try commenting out the functions that require OS.
Also, sometimes I add files to my GitHub that aren't complete just to have them there. I will mark this "COMPLETED" when finished.

======
RULES
======

Yahtzee is a two-player dice rolling game.

Players take turns rolling dice (up to 5) and try to match their dice
with the scoring categories.

Regular Scoring Categories:

1 --> score the 1s in your hand
2 --> score the 2s in your hand
3 --> score the 3s in your hand
4 --> score the 4s in your hand
5 --> score the 5s in your hand
6 --> score the 6s in your hand

If a player reaches 63 points for these categories, they receive a bonus of 35 points.

Special Scoring Categories:

3 of a kind  --> 3 or more similar dice values;    score the whole hand
4 of a kind  --> 4 or more similar dice values;    score the whole hand
Full house   --> 2 of one number and 3 of another; 25 points
Small Strait --> 4 consecutive numbers;            30 points
Large Strait --> 5 consecutive numbers;            40 points
Yahtzee      --> 5 of the same number;             50 points
Chance       --> Can be used once a game;          score the whole hand

Special Scoring Rules:
Once a Yahtzee is scored, a player can receive 100 bonus points for any other Yahtzees.
Then, the points are scored according to the rules above.
If the player has already marked the Yahtzee category with a 0, then no bonus is received.

These rules come from the Hasbro rules, so feel free to change the scoring rules in the code below for any house rules you play by.
'''

from random import randint
import sys
from time import sleep
import os

# Clear The Screen Function
def clear():
  os.system('cls' if os.name == 'nt' else 'clear')


# Delayed Text Output Function
def delay_readout(string):
  for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    sleep(0.05)


class Player:
  def __init__(self, name, wins = 0, losses = 0, streak = 0):
    self.name = name
    self.wins = wins
    self.losses = losses
    self.streak = streak

  def diceRoll(self):
    return randint(1,6)
    

if __name__ == '__main__':
  
