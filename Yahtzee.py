'''
ALMOST COMPLETE

Created by: Viktor Dominguez
Date Created: 04/18/2025  (MM/DD/YYYY)
Last Updated: 04/23/2025  (MM/DD/YYYY)
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
      "Chance":None,
      "Bonus":0
      }


if __name__ == '__main__':
    # Dice Roll Function
    def diceRoll():
      delay_readout("\nRolling...")
      return randint(1,6)

    # Function for: Determine which dice to hold during Player's turn
    def humanKeepDice(rolls):
      keepers = []
      rolls.sort()
      while True:
        for iter,(k,v) in enumerate(player_user.scorecard.items(), start=1):
          if iter == 14:
            break
          print(f"{iter}) {k}: {v}")
        print('\n\n')
        for k,item in enumerate(rolls):
          delay_readout(f"{k}) {item}\n")
        delay_readout('n) None\na) All')
        sleep(0.5)
        delay_readout("\n\nWhich values do you want to keep? (0-4, 'n' for None, 'a' for All, separate with spaces):\n\n")
        choices = input().split(' ')
        if len(choices) > 5:
          delay_readout("\nYou have chosen too many dice. Please try again.")
          sleep(1.0)
          continue
        elif choices[0].lower() == 'n':
          break
        elif choices[0].lower() == 'a':
          return rolls
        elif set(choices) <= set(['0','1','2','3','4']) and choices.count(sorted(choices,key=counter(choices).get,reverse=True)[0]) == 1:
          delay_readout(f"\nKeeping ")
          for item in choices:
            keepers.append(rolls[int(item)])
          delay_readout(f"{keepers}")
          sleep(1.0)
          break
        else:
          delay_readout(f"\nYou have made an incorrect selection. Please try again.")
          sleep(1.0)
          continue
      return keepers

    # Function for: Determine which dice to hold during CPU's turn
    def cpuKeepDice(rolls,keepers):
      seq1, seq2, seq3 = [1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]
      seq4, seq5 = [1,2,3,4,5], [2,3,4,5,6]
      for _ in range(len(keepers),5):
        rolls.append(diceRoll())
        delay_readout(f"{rolls[-1]}!\n")
        sleep(0.5)
      rolls.sort()
      frequency_rolls = sorted(rolls, key=counter(rolls).get, reverse=True)
      # Large Straight
      if (rolls == seq4 or rolls == seq5) and player_cpu.scorecard["Large Straight"] == None:
        delay_readout(f"\nThe CPU is keeping: {rolls}")
        sleep(1.0)
        clear()
        return rolls
      # keep the rolls for a small straight if Large Straight has been scored
      elif (rolls == seq4 or rolls == seq5) and player_cpu.scorecard["Small Straight"] == None:
        delay_readout(f"\nThe CPU is keeping: {rolls}")
        sleep(1.0)
        clear()
        return rolls
      # Small Straights
      elif (rolls[:4] == seq1 or rolls[1:] == seq1) and player_cpu.scorecard["Small Straight"] == None:
        delay_readout(f"\nThe CPU is keeping: {seq1}")
        sleep(1.0)
        clear()
        return seq1
      elif (rolls[:4] == seq2 or rolls[1:] == seq2) and player_cpu.scorecard["Small Straight"] == None:
        delay_readout(f"\nThe CPU is keeping: {seq2}")
        sleep(1.0)
        clear()
        return seq2
      elif (rolls[:4] == seq3 or rolls[1:] == seq3) and player_cpu.scorecard["Small Straight"] == None:
        delay_readout(f"\nThe CPU is keeping: {seq3}")
        sleep(1.0)
        clear()
        return seq3
      # Full House/3 of a Kind
      elif rolls.count(frequency_rolls[0]) == 3:
        if rolls.count(frequency_rolls[3]) == 2 and player_cpu.scorecard["Full House"] == None:
          delay_readout(f"\nThe CPU is keeping: {rolls}")
          sleep(1.0)
          clear()
          return rolls
        else:
          delay_readout(f"\nThe CPU is keeping: {[frequency_rolls[0]]*3}")
          sleep(1.0)
          clear()
          return [frequency_rolls[0]]*3
      # 4 of a Kind/Yahtzee
      elif rolls.count(frequency_rolls[0]) >= 4:
        if rolls.count(frequency_rolls[0]) == 5:
          delay_readout(f"\nThe CPU is keeping: {rolls}")
          sleep(1.0)
          clear()
          return rolls
        else:
          delay_readout(f"\nThe CPU is keeping: {[frequency_rolls[0]]*4}")
          sleep(1.0)
          clear()
          return [frequency_rolls[0]]*4
      # Keep 2 like numbers
      elif rolls.count(frequency_rolls[0]) == 2:
        # if there are 2 pairs, keep the pair that hasn't been scored--?
        if rolls.count(frequency_rolls[2]) == 2:
          # Neither pair has been scored
          if player_cpu.scorecard[str(frequency_rolls[0])] == None and player_cpu.scorecard[str(frequency_rolls[2])] == None:
            # Check FULL HOUSE first, then...
            if player_cpu.scorecard["Full House"] == None:
              delay_readout(f"\nThe CPU is keeping: {[frequency_rolls[0]]*2+[frequency_rolls[2]]*2}")
              sleep(1.0)
              clear()
              return [frequency_rolls[0]]*2+[frequency_rolls[2]]*2
            # Take higher of the pairs
            else:
              delay_readout(f"\nThe CPU is keeping: {[max(frequency_rolls[0],frequency_rolls[2])]*2}")
              sleep(1.0)
              clear()
              return [max(frequency_rolls[0],frequency_rolls[2])]*2
          # If first pair hasn't been scored yet but second has
          elif player_cpu.scorecard[str(frequency_rolls[0])] == None and player_cpu.scorecard[str(frequency_rolls[2])] != None:
            delay_readout(f"\nThe CPU is keeping: {[frequency_rolls[0]]*2}")
            sleep(1.0)
            clear()
            return [frequency_rolls[0]]*2
          # If first pair has been scored but second hasn't
          elif player_cpu.scorecard[str(frequency_rolls[0])] != None and player_cpu.scorecard[str(frequency_rolls[2])] == None:
            delay_readout(f"\nThe CPU is keeping: {[frequency_rolls[2]]*2}")
            sleep(1.0)
            clear()
            return [frequency_rolls[2]]*2
          # If both pairs have been scored...
          elif player_cpu.scorecard[str(frequency_rolls[0])] != None and player_cpu.scorecard[str(frequency_rolls[2])] != None:
            # Check FULL HOUSE...
            if player_cpu.scorecard["Full House"] == None:
              delay_readout(f"\nThe CPU is keeping: {[frequency_rolls[0]]*2+[frequency_rolls[2]]*2}")
              sleep(1.0)
              clear()
              return [frequency_rolls[0]]*2+[frequency_rolls[2]]*2
            # 3 of a Kind/Chance categories
            else:
              delay_readout(f"\nThe CPU is keeping: {[max(frequency_rolls[0],frequency_rolls[2])]*2}")
              sleep(1.0)
              clear()
              return [max(frequency_rolls[0], frequency_rolls[2])]*2
        else:
          delay_readout(f"\nThe CPU is keeping: {[frequency_rolls[0]]*2}")
          sleep(1.0)
          clear()
          return [frequency_rolls[0]]*2

    # Updating Player Scorecard Function
    def updatePlayerScorecard(playerName, rolls):
      '''
      rolls is a list of int values that correspond to the rolls the player made.
      The user/CPU player will choose which category to apply the rolls to.
      The player scorecard will be updated according to the values in rolls and the category chosen.
      '''
      rolls.sort()
      while True:
        clear()
        # Display rolls for user to see
        for item in rolls:
          delay_readout(f"{item}  ")
        print()

        # Display scorecard
        for i, (k,v) in enumerate(playerName.scorecard.items(),start=1):
          if i == len(playerName.scorecard.items()):
            break
          delay_readout(f"\n{i}) {k}: {v}")
        
        # Choose which category to score
        delay_readout(f"\n\nPlease choose a category to apply your rolls to (1-13): ")
        try:
          scorecardChoice = int(input())
        except ValueError:
          delay_readout("\nYou have input something that is not a number. Please try again.")
          sleep(0.5)
          clear()
          continue
        else:
          if scorecardChoice not in range(1,14):
            delay_readout("\nPlease enter a number within the specified range.")
            sleep(0.5)
            clear()
            continue
          else:
            frequency_rolls = sorted(rolls, key=counter(rolls).get, reverse=True)
            # matching the scores with the category choice
            match scorecardChoice:
              case 1:
                # If Yahtzee has been scored already...
                if playerName.scorecard["Yahtzee"] == 50:
                  # Bonus Yahtzee check
                  if rolls == [1]*5:
                    playerName.scorecard["1"] = 5 + 100
                    delay_readout(f"\nCongrats! You scored {5} points plus the Yahtzee bonus of 100 for the 1s category")
                    sleep(1.5)
                  # If Yahtzee has been scored but player doesn't have Yahtzee
                    # Should be the same as the normal scoring
                  else:
                    playerName.scorecard["1"] = rolls.count(1)
                    delay_readout(f"\nYou scored {rolls.count(1)} points for the 1s category")
                    sleep(1.5)
                  try:
                    # 35 point bonus check for standard categories
                    sum(list(playerName.scorecard.values())[:6]) > 62
                  except:
                    clear()
                    break
                  # If bonus has been achieved...
                  else:
                    # If bonus has not already been scored...
                    if playerName.scorecard["Bonus"] == 0:
                      delay_readout(f"\nCongrats! You got the 35 point bonus!")
                      sleep(1.0)
                      playerName.scorecard["Bonus"] = 35
                    clear()
                    break
                # If Yahtzee has not been scored yet...
                else:
                  playerName.scorecard["1"] = rolls.count(1)
                  delay_readout(f"\nYou scored {rolls.count(1)} points for the 1s category")
                  sleep(1.5)
                  try:
                    # 35 point bonus check for standard categories
                    sum(list(playerName.scorecard.values())[:6]) > 62
                  except:
                    clear()
                    break
                  # If bonus has been achieved...
                  else:
                    # If bonus has not been scored yet...
                    if playerName.scorecard["Bonus"] == 0:
                      delay_readout(f"\nCongrats! You got the 35 point bonus!")
                      sleep(1.0)
                      playerName.scorecard["Bonus"] = 35
                    clear()
                    break
              case 2:
                # If Yahtzee has been scored already...
                if playerName.scorecard["Yahtzee"] == 50:
                  # Bonus Yahtzee check
                  if rolls == [2]*5:
                    playerName.scorecard["2"] = 10 + 100
                    delay_readout(f"\nCongrats! You scored {10} points plus the Yahtzee bonus of 100 for the 2s category")
                    sleep(1.5)
                  # If Yahtzee has been scored but player doesn't have Yahtzee
                  else:
                    playerName.scorecard["2"] = rolls.count(2) * 2
                    delay_readout(f"\nYou scored {rolls.count(2)*2} points for the 2s category")
                    sleep(1.5)
                  try:
                    # 35 point bonus check for standard categories
                    sum(list(playerName.scorecard.values())[:6]) > 62
                  except:
                    clear()
                    break
                  # If bonus is achieved...
                  else:
                    # If bonus has not been scored yet...
                    if playerName.scorecard["Bonus"] == 0:
                      delay_readout(f"\nCongrats! You got the 35 point bonus!")
                      sleep(1.0)
                      playerName.scorecard["Bonus"] = 35
                    clear()
                    break
                # If Yahtzee has not been scored yet...
                else:
                  playerName.scorecard["2"] = rolls.count(2) * 2
                  delay_readout(f"\nYou scored {rolls.count(2)*2} points for the 2s category")
                  sleep(1.5)
                  try:
                    # 35 point bonus check for standard categories
                    sum(list(playerName.scorecard.values())[:6]) > 62
                  except:
                    clear()
                    break
                  # If bonus is achieved...
                  else:
                    # If bonus has not been scored yet...
                    if playerName.scorecard["Bonus"] == 0:
                      delay_readout(f"\nCongrats! You got the 35 point bonus!")
                      sleep(1.0)
                      playerName.scorecard["Bonus"] = 35
                    clear()
                    break
              case 3:
                # If Yahtzee has been scored already...
                if playerName.scorecard["Yahtzee"] == 50:
                  # Yahtzee bonus check
                  if rolls == [3]*5:
                    playerName.scorecard["3"] = 15 + 100
                    delay_readout(f"\nCongrats! You scored {15} points plus the Yahtzee bonus of 100 for the 3s category")
                    sleep(1.5)
                  # If Yahtzee has been scored but player doesn't have Yahtzee
                  else:
                    playerName.scorecard["3"] = rolls.count(3) * 3
                    delay_readout(f"\nYou scored {rolls.count(3)*3} points for the 3s category")
                    sleep(1.5)
                  try:
                    # 35 point bonus check for standard categories
                    sum(list(playerName.scorecard.values())[:6]) > 62
                  except:
                    clear()
                    break
                  # If bonus is achieved...
                  else:
                    # If bonus has not been scored yet...
                    if playerName.scorecard["Bonus"] == 0:
                      delay_readout(f"\nCongrats! You got the 35 point bonus!")
                      sleep(1.0)
                      playerName.scorecard["Bonus"] = 35
                    clear()
                    break
                # If Yahtzee has not been scored yet...
                else:
                  playerName.scorecard["3"] = rolls.count(3) * 3
                  delay_readout(f"\nYou scored {rolls.count(3)*3} points for the 3s category")
                  sleep(1.5)
                  try:
                    # 35 point bonus check for standard categories
                    sum(list(playerName.scorecard.values())[:6]) > 62
                  except:
                    clear()
                    break
                  # If bonus is achieved...
                  else:
                    # If bonus has not been scored yet...
                    if playerName.scorecard["Bonus"] == 0:
                      delay_readout(f"\nCongrats! You got the 35 point bonus!")
                      sleep(1.0)
                      playerName.scorecard["Bonus"] = 35
                    clear()
                    break
              case 4:
                # If Yahtzee has been scored already...
                if playerName.scorecard["Yahtzee"] == 50:
                  # Yahtzee bonus check
                  if rolls == [4]*5:
                    playerName.scorecard["4"] = 20 + 100
                    delay_readout(f"\nCongrats! You scored {20} points plus the Yahtzee bonus of 100 for the 4s category")
                    sleep(1.5)
                  # If Yahtzee has been scored but player doesn't have Yahtzee
                  else:
                    playerName.scorecard["4"] = rolls.count(4) * 4
                    delay_readout(f"\nYou scored {rolls.count(4)*4} points for the 4s category")
                    sleep(1.5)
                  try:
                    # 35 point bonus check for standard categories
                    sum(list(playerName.scorecard.values())[:6]) > 62
                  except:
                    clear()
                    break
                  # If bonus is achieved...
                  else:
                    # If bonus has not been scored yet...
                    if playerName.scorecard["Bonus"] == 0:
                      delay_readout(f"\nCongrats! You got the 35 point bonus!")
                      sleep(1.0)
                      playerName.scorecard["Bonus"] = 35
                    clear()
                    break
                # If Yahtzee has not been scored yet...
                else:
                  playerName.scorecard["4"] = rolls.count(4) * 4
                  delay_readout(f"\nYou scored {rolls.count(4)*4} points for the 4s category")
                  sleep(1.5)
                  try:
                    # 35 point bonus check for standard categories
                    sum(list(playerName.scorecard.values())[:6]) > 62
                  except:
                    clear()
                    break
                  # If bonus is achieved...
                  else:
                    # If bonus has not been scored yet...
                    if playerName.scorecard["Bonus"] == 0:
                      delay_readout(f"\nCongrats! You got the 35 point bonus!")
                      sleep(1.0)
                      playerName.scorecard["Bonus"] = 35
                    clear()
                    break
              case 5:
                # If Yahzee has been scored already...
                if playerName.scorecard["Yahtzee"] == 50:
                  # Yahtzee bonus check
                  if rolls == [5]*5:
                    playerName.scorecard["5"] = 25 + 100
                    delay_readout(f"\nCongrats! You scored {25} points plus the Yahtzee bonus of 100 for the 5s category")
                    sleep(1.5)
                  # If Yahtzee has been scored but player doesn't have Yahtzee
                  else:
                    playerName.scorecard["5"] = rolls.count(5) * 5
                    delay_readout(f"\nYou scored {rolls.count(5)*5} points for the 5s category")
                    sleep(1.5)
                  try:
                    # 35 point bonus check for standard categories
                    sum(list(playerName.scorecard.values())[:6]) > 62
                  except:
                    clear()
                    break
                  # If bonus is achieved...
                  else:
                    # If bonus has not been scored yet...
                    if playerName.scorecard["Bonus"] == 0:
                      delay_readout(f"\nCongrats! You got the 35 point bonus!")
                      sleep(1.0)
                      playerName.scorecard["Bonus"] = 35
                    clear()
                    break
                # If Yahtzee has not been scored yet...
                else:
                  playerName.scorecard["5"] = rolls.count(5) * 5
                  delay_readout(f"\nYou scored {rolls.count(5)*5} points for the 5s category")
                  sleep(1.5)
                  try:
                    # 35 point bonus check for standard categories
                    sum(list(playerName.scorecard.values())[:6]) > 62
                  except:
                    clear()
                    break
                  # If bonus is achieved...
                  else:
                    # If bonus has not been scored yet...
                    if playerName.scorecard["Bonus"] == 0:
                      delay_readout(f"\nCongrats! You got the 35 point bonus!")
                      sleep(1.0)
                      playerName.scorecard["Bonus"] = 35
                    clear()
                    break
              case 6:
                # If Yahzee has been scored already...
                if playerName.scorecard["Yahtzee"] == 50:
                  # Yahtzee bonus check
                  if rolls == [6]*5:
                    playerName.scorecard["6"] = 30 + 100
                    delay_readout(f"\nCongrats! You scored {30} points plus the Yahtzee bonus of 100 for the 6s category")
                    sleep(1.5)
                  # If Yahtzee has been scored but player doesn't have Yahtzee
                  else:
                    playerName.scorecard["6"] = rolls.count(6) * 6
                    delay_readout(f"\nYou scored {rolls.count(6)*6} points for the 6s category")
                    sleep(1.5)
                  try:
                    # 35 point bonus check for standard categories
                    sum(list(playerName.scorecard.values())[:6]) > 62
                  except:
                    clear()
                    break
                  # If bonus is achieved...
                  else:
                    # If bonus has not been scored yet...
                    if playerName.scorecard["Bonus"] == 0:
                      delay_readout(f"\nCongrats! You got the 35 point bonus!")
                      sleep(1.0)
                      playerName.scorecard["Bonus"] = 35
                    clear()
                    break
                # If Yahtzee has not been scored yet...
                else:
                  playerName.scorecard["6"] = rolls.count(6) * 6
                  delay_readout(f"\nYou scored {rolls.count(6)*6} points for the 6s category")
                  sleep(1.5)
                  try:
                    # 35 point bonus check for standard categories
                    sum(list(playerName.scorecard.values())[:6]) > 62
                  except:
                    clear()
                    break
                  # If bonus is achieved...
                  else:
                    # If bonus has not been scored yet...
                    if playerName.scorecard["Bonus"] == 0:
                      delay_readout(f"\nCongrats! You got the 35 point bonus!")
                      sleep(1.0)
                      playerName.scorecard["Bonus"] = 35
                    clear()
                    break
              case 7:
                # If player selects "3 of a Kind", but doesn't have 3 of a Kind...
                if rolls.count(frequency_rolls[0]) < 3:
                  playerName.scorecard["3 of a Kind"] = 0
                  delay_readout("\nYou scored 0 points for the 3-of-a-kind category")
                  sleep(1.5)
                  clear()
                  break
                # If player has 3 of a Kind...
                else:
                  playerName.scorecard["3 of a Kind"] = sum(rolls)
                  delay_readout(f"\nYou scored {sum(rolls)} points for the 3-of-a-kind category")
                  sleep(1.5)
                  clear()
                  break
              case 8:
                # If player selects "4 of a Kind", but doesn't have 4 of a Kind...
                if rolls.count(frequency_rolls[0]) < 4:
                  playerName.scorecard["4 of a Kind"] = 0
                  delay_readout("\nYou scored 0 points for the 4-of-a-kind category")
                  sleep(1.5)
                  clear()
                  break
                # If player has 4 of a Kind...
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
                if (set(rolls) >= set(seq1) or set(rolls) >= set(seq2) or set(rolls) >= set(seq3)) or (set(rolls) >= set(seq1) or set(rolls) >= set(seq2) or set(rolls) >= set(seq3)):
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
                if rolls == seq1 or rolls == seq2:
                  playerName.scorecard["Large Straight"] = 40
                  delay_readout("\nYou scored 40 points for the Large Straight category")
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

    # Updating CPU Scorecard Function
    def updateOpponentScorecard(cpuPlayer, rolls):
      scoreOptions = {}
      frequency_rolls = sorted(rolls, key=counter(rolls).get, reverse=True)
      rolls.sort()
      for item in rolls:
        delay_readout(f"{item}  ")
      for i in range(1,14):
        match i:
          case 1:
            if cpuPlayer.scorecard["1"] == None:
              if cpuPlayer.scorecard["Yahtzee"] == 50:
                if rolls == [1]*5:
                  scoreOptions["1"] = 5 + 100
                else:
                  scoreOptions["1"] = rolls.count(1)
              else:
                scoreOptions["1"] = rolls.count(1)
            else:
              scoreOptions["1"] = 0
          case 2:
            if cpuPlayer.scorecard["2"] == None:
              if cpuPlayer.scorecard["Yahtzee"] == 50:
                if rolls == [2]*5:
                  scoreOptions["2"] = 10 + 100
                else:
                  scoreOptions["2"] = rolls.count(2) * 2
              else:
                  scoreOptions["2"] = rolls.count(2) * 2
            else:
                scoreOptions["2"] = 0
          case 3:
            if cpuPlayer.scorecard["3"] == None:
              if cpuPlayer.scorecard["Yahtzee"] == 50:
                if rolls == [3]*5:
                  scoreOptions["3"] = rolls.count(3) * 3 + 100
                else:
                  scoreOptions["3"] = rolls.count(3) * 3
              else:
                scoreOptions["3"] = rolls.count(3) * 3
            else:
              scoreOptions["3"] = 0
          case 4:
            if cpuPlayer.scorecard["4"] == None:
              if cpuPlayer.scorecard["Yahtzee"] == 50:
                if rolls == [4]*5:
                  scoreOptions["4"] = rolls.count(4) * 4 + 100
                else:
                  scoreOptions["4"] = rolls.count(4) * 4
              else:
                scoreOptions["4"] = rolls.count(4) * 4
            else:
              scoreOptions["4"] = 0
          case 5:
            if cpuPlayer.scorecard["5"] == None:
              if cpuPlayer.scorecard["Yahtzee"] == 50:
                if rolls == [5]*5:
                  scoreOptions["5"] = rolls.count(5) * 5 + 100
                else:
                  scoreOptions["5"] = rolls.count(5) * 5
              else:
                scoreOptions["5"] = rolls.count(5) * 5
            else:
              scoreOptions["5"] = 0
          case 6:
            if cpuPlayer.scorecard["6"] == None:
              if cpuPlayer.scorecard["Yahtzee"] == 50:
                if rolls == [6]*5:
                  scoreOptions["6"] = rolls.count(6) * 6 + 100
                else:
                  scoreOptions["6"] = rolls.count(6) * 6
              else:
                scoreOptions["6"] = rolls.count(6) * 6
            else:
              scoreOptions["6"] = 0
          case 7:
            if cpuPlayer.scorecard["3 of a Kind"] == None:
              if rolls.count(frequency_rolls[0]) < 3:
                scoreOptions["3 of a Kind"] = 0
              else:
                scoreOptions["3 of a Kind"] = sum(rolls)
            else:
              scoreOptions["3 of a Kind"] = sum(rolls)
          case 8:
            if cpuPlayer.scorecard["4 of a Kind"] == None:
              if rolls.count(frequency_rolls[0]) < 4:
                scoreOptions["4 of a Kind"] = 0
              else:
                scoreOptions["4 of a Kind"] = sum(rolls)
            else:
              scoreOptions["4 of a Kind"] = sum(rolls)
          case 9:
            if cpuPlayer.scorecard["Full House"] == None:
              if rolls.count(frequency_rolls[0]) == 3 and rolls.count(frequency_rolls[3]) == 2:
                scoreOptions["Full House"] = 25
              else:
                scoreOptions["Full House"] = 0
            else:
              scoreOptions["Full House"] = 0
          case 10:
            if cpuPlayer.scorecard["Small Straight"] == None:
              seq1, seq2, seq3 = [1,2,3,4], [2,3,4,5], [3,4,5,6]
              if (rolls[:4] == seq1 or rolls[:4] == seq2 or rolls[:4] == seq3) or (rolls[1:] == seq1 or rolls[1:] == seq2 or rolls[1:] == seq3):
                scoreOptions["Small Straight"] = 30
              else:
                scoreOptions["Small Straight"] = 0
            else:
              scoreOptions["Small Straight"] = 0
          case 11:
            if cpuPlayer.scorecard["Large Straight"] == None:
              seq1, seq2 = [1,2,3,4,5], [2,3,4,5,6]
              if rolls == seq1 or rolls == seq2:
                scoreOptions["Large Straight"] = 40
              else:
                scoreOptions["Large Straight"] = 0
            else:
              scoreOptions["Large Straight"] = 0
          case 12:
            if cpuPlayer.scorecard["Yahtzee"] == None:
              if rolls.count(rolls[0]) == 5:
                scoreOptions["Yahtzee"] = 50
              else:
                scoreOptions["Yahtzee"] = 0
            else:
              scoreOptions["Yahtzee"] = 0
          case 13:
            if cpuPlayer.scorecard["Chance"] == None:
              scoreOptions["Chance"] = sum(rolls)
            else:
              scoreOptions["Chance"] = 0
      max_score = [max(scoreOptions, key=scoreOptions.get),max(scoreOptions.values())]
      cpuPlayer.scorecard[max_score[0]] = max_score[1]
      delay_readout(f"\nThe CPU chose to score {rolls} in the {max_score[0]} category for {max_score[1]} points.")
      sleep(1.5)
      clear()
      # Delete variables to clear memory
      del seq1, seq2, seq3, frequency_rolls, max_score, scoreOptions

    # Function for: Player's turn rolling and selecting dice to keep
    def playerTurn():
      for i in range(3):
        rolls = []
        if i == 0:
          for _ in range(5):
            rolls.append(diceRoll())
            delay_readout(f"{rolls[-1]}!\n")
            sleep(0.5)
          sleep(0.5)
          keepers = humanKeepDice(rolls)
          # Make sure keepers is not full
          if len(keepers) == 5:
            return keepers
        # For second and third rolls
        elif i == 1 and len(keepers) < 5:
          for item in keepers:
            rolls.append(item)
          for _ in range(len(keepers),5):
            rolls.append(diceRoll())
            delay_readout(f"{rolls[-1]}!\n")
            sleep(0.3)
          sleep(0.5)
          keepers = humanKeepDice(rolls)
          # Make sure keepers is not full
          if len(keepers) == 5:
            return keepers
        elif i == 2 and len(keepers) < 5:
          for item in keepers:
            rolls.append(item)
          for _ in range(len(keepers),5):
            rolls.append(diceRoll())
            delay_readout(f"{rolls[-1]}!\n")
          delay_readout(f"\n\nYour final roll was: {rolls}")
          sleep(1.5)
          clear()
          return rolls

    # Function for: CPU player's turn. Rolls dice and selects which ones to keep
    def cpuTurn():
      for i in range(3):
        rolls = []
        if i == 0:
          keepers = cpuKeepDice(rolls,[])
          if keepers in [[1,2,3,4],[2,3,4,5],[3,4,5,6]]:
            return keepers
          # Make sure keepers is not full
          if len(keepers) == 5:
            return keepers
        # For second and third rolls
        elif i == 1:
          for item in keepers:
            rolls.append(item)
          keepers.sort()
          if keepers in [[1,2,3,4],[2,3,4,5],[3,4,5,6]]:
            return keepers
          keepers = cpuKeepDice(rolls,keepers)
          # Make sure keepers is not full
          if len(keepers) == 5:
            return keepers
        else:
          keepers.sort()
          for item in keepers:
            rolls.append(item)
          for _ in range(len(keepers),5):
            rolls.append(diceRoll())
            delay_readout(f"{rolls[-1]}!\n\n")
      return rolls

    # Function for: Playing the game. Includes calls for updating scorecards and updating player records at the end
    def game():
      # Gameplay Loop
      while None in player_cpu.scorecard.values():
        delay_readout(f"\n\nStarting {player_name}'s turn.\n\n")
        sleep(2.0)
        clear()
        updatePlayerScorecard(player_user,playerTurn())
        sleep(1.5)
        clear()
        delay_readout(f"\n\nStarting {player_cpu.name}'s turn.\n\n")
        sleep(2.0)
        clear()
        updateOpponentScorecard(player_cpu,cpuTurn())
        sleep(1.5)
        clear()
      # Player Wins! Update wins and streak attributes
      player_final_score = sum(player_user.scorecard.values())
      cpu_final_score = sum(player_cpu.scorecard.values())
      if player_final_score > cpu_final_score:
        delay_readout(f"\nCongratulations, {player_user.name}! You won!")
        delay_readout(f"\n\nFinal score: {player_user.name} - {player_final_score}\t{player_cpu.name} - {cpu_final_score}")
        sleep(3.0)
        clear()
        # Update wins
        player_user.wins += 1
        # Update streak
        if player_user.streak >= 0:
          player_user.streak += 1
        else:
          player_user.streak = 1
      elif player_final_score < cpu_final_score:
        delay_readout(f"\nSorry, {player_cpu.name} won.")
        delay_readout(f"\n\nFinal score: {player_user.name} - {player_final_score}\t{player_cpu.name} - {cpu_final_score}")
        sleep(3.0)
        clear()
        # Update loses
        player_user.losses += 1
        # Update streak
        if player_user.streak <= 0:
          player_user.streak -= 1
        else:
          player_user.streak = -1
      else:
        delay_readout(f"\nThe game ended in a tie!")
        delay_readout(f"\n\nFinal score: {player_user.name} - {player_final_score}\t{player_cpu.name} - {cpu_final_score}")
        sleep(3.0)
        clear()
        # Reset the streak to 0
        player_user.streak = 0

    # Main Game
    clear()
    delay_readout("Hello!...umm...")
    
    # Name loop
    while True:
      delay_readout("\nWhat is your name? ")
      player_name = input()
      sleep(0.5)
      while True:
        delay_readout(f"\nSo your name is {player_name}? (y/n): ")
        answer = input().lower()
        if len(answer) > 1:
          delay_readout("\nPlease only put a 'y' or an 'n'.\n")
          continue
        elif answer == 'y' or answer == 'n':
          if answer == 'y':
            delay_readout(f"\nExcellent! Nice to meet you, {player_name}.")
            sleep(0.5)
            break
          else:
            delay_readout("\nOh my, you forgot your name? How tragic...Ask that person behind you if they remember.")
            sleep(0.5)
            delay_readout("\nI'm guessing you asked them and they told you.\n")
            sleep(1.0)
            break
        else:
          delay_readout("\nSorry, you have entered an incorrect option. Please stick to 'y' for yes and 'n' for no.\n")
          continue
      if answer == 'y':
        break
      else:
        continue
    del answer

    # Player and CPU creations
    player_user = Player(player_name)
    player_cpu = Player("Jeff")
    clear()
    delay_readout(f"\nYou have played {sum([player_user.wins,player_user.losses])} games so far.")
    sleep(0.2)
    delay_readout(f" You have {player_user.wins} wins, {player_user.losses} losses, and a current streak of {player_user.streak}.")
    sleep(1.0)
    delay_readout("\n\nGet ready to play Yahtzee!")
    sleep(0.5)
    delay_readout(f"\nYour opponent will be {player_cpu.name}.\n\nHe's a grand-master, so good luck!")
    sleep(1.0)

    # Game Loop
    while True:
      game()
      delay_readout(f"\nYou have played {sum([player_user.wins,player_user.losses])} games so far.")
      sleep(0.2)
      delay_readout(f" You have {player_user.wins} wins, {player_user.losses} losses, and a current streak of {player_user.streak}.")
      sleep(1.0)
      # Ask to play again
      while True:
        delay_readout("Would you like to play again? (y/n): ")
        answer = input().lower()
        if len(answer) > 1:
          delay_readout("\n\nYou have entered too many characters. Please try again.\n\n")
          sleep(1.0)
          continue
        elif answer == ('y' or 'n'):
          break
        else:
          delay_readout(f"\n\nYou have entered an incorrect character. Please enter either a 'y' or 'n' to answer. Please try again.\n\n")
          sleep(1.0)
          continue
      if answer == 'y':
        delay_readout("\n\nPlaying again!")
        keys = player_user.scorecard.keys()
        player_user.scorecard = dict.fromkeys(keys,None)
        player_user.scorecard["Bonus"] = 0
        player_cpu.scorecard = dict.fromkeys(keys,None)
        player_cpu.scorecard["Bonus"] = 0
        sleep(1.0)
        clear()
        continue
      else:
        delay_readout("\n\nThanks for playing!")
        sleep(1.0)
        break
