"""
This is a program which initializes the library pygame, then runs a loop.
"""

import pygame
from pygame.locals import *
import sys


def terminate():
    """
    Stop all functions of the program.
    """
    pygame.quit()
    sys.exit()

def initialize():
    """
    Initializes the pygame library, and creates a display window.
    """
    print('CONSOLE: Initializing loop...')
    pygame.init()
    pygame.display.set_mode((1,1))
    print('CONSOLE: Init complete. Starting loop.')

def runProgram():
    """
    Run the program main loop
    """
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

def main():
    """
    Initialize data, then run the program.
    """
    initialize()
    runProgram()

if __name__ == '__main__':
    main()
