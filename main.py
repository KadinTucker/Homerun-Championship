"""
This is a program which initializes the library pygame, then runs a loop.
"""

import pygame
from pygame.locals import *
import sys

class button():
    """
    A button class to have a width and coordinates. Also has a pressed state.

    Takes in location, which is the location of the button.
    Takes in button ID, which determines where the button takes you when pressing it.
    """
    def __init__(self, location, identity):
        self.location = location
        self.identity = identity
        self.pressed = False

def initButtons():
    """
    Initializes the buttons for the main menu.

    Returns a list of all buttons in the main menu.
    """
    buttons = []
    buttons.append(button((250, 200), 'quit'))

def buttonPressed(buttons):
    """
    Checks whether or not a button has been clicked.
    Takes in the list of buttons.

    Returns a slightly modified list of buttons, modifying whether or not the button has been pressed.
    """
    mouse = pygame.mouse.get_pos()
    for i in buttons:
        if i.location[0] - mouse[0] <= 200 and i.location[0] - mouse[0] >= 0:
            if i.location[1] - mouse[1] <= 50 and i.location[1] - mouse[1] >= 0:
                i.pressed = True
    return buttons
    
def terminate():
    """
    Stop all functions of the program.
    """
    pygame.quit()
    sys.exit()

def initialize():
    """
    Initializes the pygame library, and creates a display window.

    Returns a list of buttons in the main menu, and the starting game state.
    """
    print('CONSOLE: Initializing loop...')
    pygame.init()
    pygame.display.set_mode((500, 400))
    buttons = initButtons()
    gamestate = 1 #Gamestate 1 is the main menu.
    print('CONSOLE: Init complete. Starting loop.')
    return buttons, gamestate

def runProgram(buttons, gamestate):
    """
    Run the program main loop

    Takes in a list of buttons in the main menu, and the starting game state.
    """
    while True:
        if gamestate == 1:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        buttons = buttonPressed(buttons)
                if event.type == QUIT:
                    terminate()         

def main():
    """
    Initialize data, then run the program.
    """
    buttons, gamestate = initialize()
    runProgram(buttons, gamestate)

if __name__ == '__main__':
    main()
