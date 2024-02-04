#!/usr/bin/env python3
# Zombie Dice Bots
# Practice Project

import zombiedice
import random


class MyZombie1:
    """The First Bot

    A bot that, after the first roll,
    randomly decides if it will continue or stop.

    """
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()  # first roll

        while diceRollResults is not None:

            if random.randint(0, 1):
                diceRollResults = zombiedice.roll()  # roll again
            else:
                break


class MyZombie2:
    """The Second Bot

    A bot that stops rolling after it has rolled two brains.

    """
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()  # first roll

        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll()  # roll again
            else:
                break


class MyZombie3:
    """The Third Bot

    A bot that stops rolling after it has rolled two shotguns.

    """
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()  # first roll

        shotguns = 0
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']

            if shotguns < 2:
                diceRollResults = zombiedice.roll()  # roll again
            else:
                break


class MyZombie4:
    """The Fourth Bot

    A bot that initially decides it’ll roll the dice one to
    four times, but will stop early if it rolls two shotguns.

    """
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()  # first roll

        shotguns = 0
        numRolls = 1
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']

            if shotguns < 2 and numRolls < 4:
                diceRollResults = zombiedice.roll()  # roll again
                numRolls += 1
            else:
                break


class MyZombie5:
    """The Fifth Bot

    A bot that stops rolling after it has rolled more
    shotguns than brains.

    """
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()  # first roll

        shotguns = 0
        brains = 0
        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']
            brains += diceRollResults['brains']

            if shotguns > brains:
                break
            else:
                diceRollResults = zombiedice.roll()  # roll again


zombies = (
    MyZombie1(name='Random After First Roll'),
    MyZombie2(name='Stop at 2 Brains'),
    MyZombie3(name='Stop at 2 Shotguns'),
    MyZombie4(name='1-4 but Stop at 2 Shotguns'),
    MyZombie5(name='Stop at Shotguns > Brains'),
    # Add any other zombie players here.
)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
zombiedice.runTournament(zombies=zombies, numGames=1000)
# zombiedice.runWebGui(zombies=zombies, numGames=1000)
