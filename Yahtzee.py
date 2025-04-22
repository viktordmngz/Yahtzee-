'''
STILL WORKING ON THIS

Created by: Viktor Dominguez
Date Created: 04/18/2025  (MM/DD/YYYY)
Last Updated: 04/21/2025  (MM/DD/YYYY)
Editor: Python IDLE, Visual Studio


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
from collections import Counter as counter

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
    self.scorecard = {
      "1":None,
      "2":None,
      "3": None,
      "4":None,
      "5":None,
      "6":None,
      "3 of a Kind":None,
      "4 of a Kind":None,
      "Full House":None,
      "Small Straight":None,
      "Large Straight":None,
      "Yahtzee":None,
      "Chance":None
      }

  

  

if __name__ == '__main__':
    # Dice Roll Function
    def diceRoll():
      return randint(1,6)

    # Updating Scorecard Function
    def updatePlayerScorecard(playerName, rolls):
      '''
      rolls is a list of int values that correspond to the rolls the player made.
      The user/CPU player will choose which category to apply the rolls to.
      The player scorecard will be updated according to the values in rolls and the category chosen.
      '''
      while True:
        # Display scorecard
        for i, (k,v) in enumerate(playerName.scorecard.items(),start=1):
          delay_readout(f"\n{i}) {k}: {v}")
        
        # Choose which category to score
        delay_readout(f"\n\nPlease choose a category to apply your rolls to (1-{len(playerName.scorecard)}): ")
        try:
          scorecardChoice = int(input())
        except ValueError:
          delay_readout("\nYou have input something that is not a number. Please try again.")
          sleep(0.5)
          clear()
          continue
        else:
          if scorecardChoice not in range(1,len(playerName.scorecard)+1):
            delay_readout("\nPlease enter a number within the specified range.")
            sleep(0.5)
            clear()
            continue
          else:
            frequency_rolls = sorted(rolls, key=counter(rolls).get, reverse=True)
            rolls.sort()
            match scorecardChoice:
              case 1:
                if playerName.scorecard["Yahtzee"] == 50:
                  playerName.scorecard["1"] = rolls.count(1) + 100
                  delay_readout(f"\nCongrats! You scored {rolls.count(1)} points plus the Yahtzee bonus of 100 for the 1s category")
                  sleep(1.5)
                  clear()
                  break
                else:
                  playerName.scorecard["1"] = rolls.count(1)
                  delay_readout(f"\nYou scored {rolls.count(1)} points for the 1s category")
                  sleep(1.5)
                  clear()
                  break
              case 2:
                if playerName.scorecard["Yahtzee"] == 50:
                  playerName.scorecard["2"] = rolls.count(2)*2 + 100
                  delay_readout(f"\nCongrats! You scored {rolls.count(2)*2} points plus the Yahtzee bonus of 100 for the 2s category")
                  sleep(1.5)
                  clear()
                  break
                else:
                  playerName.scorecard["2"] = rolls.count(2) * 2
                  delay_readout(f"\nYou scored {rolls.count(2)*2} points for the 2s category")
                  sleep(1.5)
                  clear()
                  break
              case 3:
                if playerName.scorecard["Yahtzee"] == 50:
                  playerName.scorecard["3"] = rolls.count(3)*3 + 100
                  delay_readout(f"\nCongrats! You scored {rolls.count(3)*3} points plus the Yahtzee bonus of 100 for the  category")
                  sleep(1.5)
                  clear()
                  break
                else:
                  playerName.scorecard["3"] = rolls.count(3) * 3
                  delay_readout(f"\nYou scored {rolls.count(3)*3} points for the 3s category")
                  sleep(1.5)
                  clear()
                  break
              case 4:
                if playerName.scorecard["Yahtzee"] == 50:
                  playerName.scorecard["4"] = rolls.count(4)*4 + 100
                  delay_readout(f"\nCongrats! You scored {rolls.count(4)*4} points plus the Yahtzee bonus of 100 for the  category")
                  sleep(1.5)
                  clear()
                  break
                else:
                  playerName.scorecard["4"] = rolls.count(4) * 4
                  delay_readout(f"\nYou scored {rolls.count(4)*4} points for the 4s category")
                  sleep(1.5)
                  clear()
                  break
              case 5:
                if playerName.scorecard["Yahtzee"] == 50:
                  playerName.scorecard["5"] = rolls.count(5)*5 + 100
                  delay_readout(f"\nCongrats! You scored {rolls.count(5)*5} points plus the Yahtzee bonus of 100 for the  category")
                  sleep(1.5)
                  clear()
                  break
                else:
                  playerName.scorecard["5"] = rolls.count(5) * 5
                  delay_readout(f"\nYou scored {rolls.count(5)*5} points for the 5s category")
                  sleep(1.5)
                  clear()
                  break
              case 6:
                if playerName.scorecard["Yahtzee"] == 50:
                  playerName.scorecard["6"] = rolls.count(6)*6 + 100
                  delay_readout(f"\nCongrats! You scored {rolls.count(6)*6} points plus the Yahtzee bonus of 100 for the  category")
                  sleep(1.5)
                  clear()
                  break
                else:
                  playerName.scorecard["6"] = rolls.count(6) * 6
                  delay_readout(f"\nYou scored {rolls.count(6)*6} points for the 6s category")
                  sleep(1.5)
                  clear()
                  break
              case 7:
                if rolls.count(frequency_rolls[0]) < 3:
                  playerName.scorecard["3 of a Kind"] = 0
                  delay_readout("\nYou scored 0 points for the 3-of-a-kind category")
                  sleep(1.5)
                  clear()
                  break
                else:
                  playerName.scorecard["3 of a Kind"] = sum(rolls)
                  delay_readout(f"\nYou scored {sum(rolls)} points for the 3-of-a-kind category")
                  sleep(1.5)
                  clear()
                  break
              case 8:
                if rolls.count(frequency_rolls[0]) < 4:
                  playerName.scorecard["4 of a Kind"] = 0
                  delay_readout("\nYou scored 0 points for the 4-of-a-kind category")
                  sleep(1.5)
                  clear()
                  break
                else:
                  playerName.scorecard["4 of a Kind"] = sum(rolls)
                  delay_readout(f"\nYou scored {sum(rolls)} points for the 4-of-a-kind category")
                  sleep(1.5)
                  clear()
                  break
              case 9:
                if rolls.count(frequency_rolls[0]) == 3 and rolls.count(frequency_rolls[3]) == 2:
                  playerName.scorecard["Full House"] = 25
                  delay_readout("\nYou scored 25 points for the Full House category")
                  sleep(1.5)
                  clear()
                  break
                else:
                  playerName.scorecard["Full House"] = 0
                  delay_readout("\nYou scored 0 points for the Full House category")
                  sleep(1.5)
                  clear()
                  break
              case 10:
                seq1, seq2, seq3 = [1,2,3,4], [2,3,4,5], [3,4,5,6]
                if rolls[:4] == (seq1 or seq2 or seq3) or rolls[1:] == (seq1 or seq2 or seq3):
                  playerName.scorecard["Small Straight"] = 30
                  delay_readout("\nYou scored 30 points for the Small Straight category")
                  sleep(1.5)
                  clear()
                  break
                else:
                  playerName.scorecard["Small Straight"] = 0
                  delay_readout("\nYou scored 0 points for the Small Straight category")
                  sleep(1.5)
                  clear()
                  break
              case 11:
                seq1, seq2 = [1,2,3,4,5], [2,3,4,5,6]
                if rolls == (seq1 or seq2):
                  playerName.scorecard["Large Straight"] = 40
                  delay_readout("\nYou scored 30 points for the Large Straight category")
                  sleep(1.5)
                  clear()
                  break
                else:
                  playerName.scorecard["Large Straight"] = 0
                  delay_readout("\nYou scored 0 points for the Large Straight category")
                  sleep(1.5)
                  clear()
                  break
              case 12:
                if rolls.count(rolls[0]) == 5:
                  playerName.scorecard["Yahtzee"] = 50
                  delay_readout("\nYAHTZEE! Way to go! 50 points!")
                  sleep(1.5)
                  clear()
                  break
                else:
                  playerName.scorecard["Yahtzee"] = 0
                  delay_readout("\nYou scored 0 points for the Yahtzee category")
                  sleep(1.5)
                  clear()
                  break
              case 13:
                playerName.scorecard["Chance"] = sum(rolls)
                delay_readout(f"\nYou scored {sum(rolls)} points for the Chance category")
                sleep(1.5)
                clear()
                break

    def updateOpponentScorecard(cpuPlayer, rolls):
      scoreOptions = {}
      frequency_rolls = sorted(rolls, key=counter(rolls).get, reverse=True)
      rolls.sort()
      for i in range(1,14):
        match i:
          case 1:
            if cpuPlayer.scorecard["1"] == None:
              if cpuPlayer.scorecard["Yahtzee"] == 50:
                scoreOptions["1"] = rolls.count(1) + 100
              else:
                scoreOptions["1"] = rolls.count(1)
          case 2:
            if cpuPlayer.scorecard["2"] == None:
              if cpuPlayer.scorecard["Yahtzee"] == 50:
                scoreOptions["2"] = rolls.count(2) * 2 + 100
              else:
                scoreOptions["2"] = rolls.count(2) * 2
          case 3:
            if cpuPlayer.scorecard["3"] == None:
              if cpuPlayer.scorecard["Yahtzee"] == 50:
                scoreOptions["3"] = rolls.count(3) * 3 + 100
              else:
                scoreOptions["3"] = rolls.count(3) * 3
          case 4:
            if cpuPlayer.scorecard["4"] == None:
              if cpuPlayer.scorecard["Yahtzee"] == 50:
                scoreOptions["4"] = rolls.count(4) * 4 + 100
              else:
                scoreOptions["4"] = rolls.count(4) * 4
          case 5:
            if cpuPlayer.scorecard["5"] == None:
              if cpuPlayer.scorecard["Yahtzee"] == 50:
                scoreOptions["5"] = rolls.count(5) * 5 + 100
              else:
                scoreOptions["5"] = rolls.count(5) * 5
          case 6:
            if cpuPlayer.scorecard["6"] == None:
              if cpuPlayer.scorecard["Yahtzee"] == 50:
                scoreOptions["6"] = rolls.count(6) * 6 + 100
              else:
                scoreOptions["6"] = rolls.count(6) * 6
          case 7:
            if cpuPlayer.scorecard["3 of a Kind"] == None:
              if rolls.count(frequency_rolls[0]) < 3:
                scoreOptions["3 of a Kind"] = 0
              else:
                scoreOptions["3 of a Kind"] = sum(rolls)
          case 8:
            if cpuPlayer.scorecard["4 of a Kind"] == None:
              if rolls.count(frequency_rolls[0]) < 4:
                scoreOptions["4 of a Kind"] = 0
              else:
                scoreOptions["4 of a Kind"] = sum(rolls)
          case 9:
            if cpuPlayer.scorecard["Full House"] == None:
              if rolls.count(frequency_rolls[0]) == 3 and rolls.count(frequency_rolls[3]) == 2:
                scoreOptions["Full House"] = 25
              else:
                scoreOptions["Full House"] = 0
          case 10:
            if cpuPlayer.scorecard["Small Straight"] == None:
              seq1, seq2, seq3 = [1,2,3,4], [2,3,4,5], [3,4,5,6]
              if rolls[:4] == (seq1 or seq2 or seq3) or rolls[1:] == (seq1 or seq2 or seq3):
                scoreOptions["Small Straight"] = 30
              else:
                scoreOptions["Small Straight"] = 0
          case 11:
            if cpuPlayer.scorecard["Large Straight"] == None:
              seq1, seq2 = [1,2,3,4,5], [2,3,4,5,6]
              if rolls == (seq1 or seq2):
                scoreOptions["Large Straight"] = 40
              else:
                scoreOptions["Large Straight"] = 0
          case 12:
            if cpuPlayer.scorecard["Yahtzee"] == None:
              if rolls.count(rolls[0]) == 5:
                scoreOptions["Yahtzee"] = 50
              else:
                scoreOptions["Yahtzee"] = 0
          case 13:
            if cpuPlayer.scorecard["Chance"] == None:
              scoreOptions["Chance"] = sum(rolls)
      max_score = [max(scoreOptions, key=scoreOptions.get),max(scoreOptions.values())]
      cpuPlayer.scorecard[max_score[0]] = max_score[1]


    
    clear()
    delay_readout("Hello!...umm...")
    
    # Name loop
    while True:
      player_name = input(delay_readout("What was your name?\t"))
      sleep(0.5)
      answer = input(delay_readout(f"\nSo your name is {player_name}? (y/n): ")).lower()
      if len(answer) != 1:
        delay_readout("Please only put a 'y' or an 'n'.\n")
        continue
      elif answer != 'y' or answer != 'n':
        delay_readout("Sorry, you have entered an incorrect option. Please stick to 'y' for yes and 'n' for no.\n")
        continue
      else:
        if answer == 'y':
          delay_readout(f"Excellent! Nice to meet you, {player_name}.")
          sleep(0.5)
          break
        else:
          delay_readout(f"Oh my, you forgot your name? How tragic...Ask that person behind you if they remember.")
          sleep(0.5)
          delay_readout(f"I'm guessing you asked them and they told you.\n")
          continue

    player_user = Player(player_name)
    player_cpu = Player("Fred")
    sleep(0.5)
    clear()
    delay_readout(f"Well, it looks like you have played {sum([player_user.wins,player_user.losses])} games so far.")
    sleep(0.2)
    delay_readout(f"You have {player_user.wins} wins, {player_user.losses} losses, and a current streak of {player_user.streak}.")
    sleep(0.2)
    delay_readout(f"Get ready to play Yahtzee!")
    sleep(0.5)
    clear()

