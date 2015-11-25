"""
This is a program which initializes the library pygame, then runs a loop.
"""

import random
import pygame
from pygame.locals import *
import sys

SOUND_NAMES = ['fanfare']
SOUND_FILES = {'fanfare' : 'start_fanfare.wav'}

PLAYER_FACES = ['confidenceFace.png', 'determineFace.png']

class player():
    """
    A player class, with playing statistics, various methods of play, and images to display.
    """
    def __init__(self):
        try:
            import names
        except:
            print('ERROR: Missing file \'names.py\'. Terminating...')
            terminate()
        self.name = random.choice(names.firstnames) + ' ' + random.choice(names.lastnames)
        self.stamina = 0
        self.speed = 0
        self.field = 0
        self.batting = 0
        
    def setStats(self):
        trials = 15
        while trials > 0:
            stat = random.randint(1, 4)
            if stat == 1 and self.stamina <= 5:
                self.stamina += 1
                trials -= 1
            elif stat == 2 and self.speed <= 5:
                self.stamina += 1
                trials -= 1
            elif stat == 3 and self.field <= 5:
                self.stamina += 1
                trials -= 1
            elif stat == 4 and self.batting <= 5:
                self.stamina += 1
                trials -= 1

class button():
    """
    A button class to have a width and coordinates. Also has a pressed state.

    Takes in location, which is the location of the button.
    Takes in button ID, which determines where the button takes you when pressing it.
    Takes in image, the image in which it displays on the screen.
    """
    def __init__(self, location, identity, image):
        self.location = location
        self.identity = identity
        self.image = image
        self.pressed = False
        
    def buttonPressed(self):
        """
        Checks whether or not a button has been clicked.

        Returns a slightly modified list of buttons, modifying whether or not the button has been pressed.
        """
        mouse = pygame.mouse.get_pos()
        print('CONSOLE: Clicked at point '+str(mouse))
        if mouse[0] - self.location[0] <= 200 and mouse[0] - self.location[0] >= 0:
            if mouse[1] - self.location[1] <= 50 and mouse[1] - self.location[1] >= 0:
                self.pressed = True
                print('CONSOLE: Button of ID %s has been pressed.' % self.identity)

    def displayButtons(self, display):
        """
        Displays the button on the screen as self.image. All button images should be 200px X 50px
        to have proper dimensions.

        Takes in the main game display screen.
        """
        display.blit(self.image, self.location)

def terminate():
    """
    Stop all functions of the program.
    """
    pygame.quit()
    sys.exit()

def checkButtons(buttons, sounds):
    """
    Checks whether the ID of all buttons being pressed checks out with any pre-determined functions
    of specific buttons. If the function goes through and nothing happens, the button becomes un-pressed.

    Takes in the list of all buttons.

    Ex: A 'quit' button will terminate the game when pressed.

    Returns the new game state.
    """
    for i in buttons:
        if i.pressed == True:
            if i.identity == 'quit':
                print('CONSOLE: Quit Button pressed.')
                return 0
                print('ERROR: Quit not gone through.')
            if i.identity == 'play':
                print('CONSOLE: Play button pressed.')
                sounds['fanfare'].play()
                return 2
        else:
            i.pressed == False
    return 1

def draftPlayers():
    """
    Creates random players 
    """
    team = []
    while len(team) < 8:
        draftpicks = [player(), player(), player()]
        for i in draftpicks:
            i.setStats()
        

def initButtons():
    """
    Initializes the buttons for the main menu.

    Returns a list of all buttons in the main menu.
    """
    buttons = []
    buttons.append(button((150, 210), 'quit', pygame.image.load('quitbutton.png')))
    buttons.append(button((100, 20), None, pygame.image.load('title.png')))
    buttons.append(button((150, 150), 'play', pygame.image.load('playbutton.png')))
    return buttons

def initSounds():
    """
    Adds a list of sounds to be used in the game.
    """
    sounds = {}
    for sound_name in SOUND_NAMES:
        sounds[sound_name] = pygame.mixer.Sound(SOUND_FILES[sound_name])
    return sounds

def initialize():
    """
    Initializes the pygame library, and creates a display window.

    Returns a list of buttons in the main menu, and the starting game state.
    """
    print('CONSOLE: Initializing loop...')
    pygame.init()
    pygame.mixer.init()
    sounds = initSounds()
    display = pygame.display.set_mode((500, 400))
    buttons = initButtons()
    gamestate = 1 #Gamestate 1 is the main menu.
    print('CONSOLE: Init complete. Starting loop.')
    return buttons, gamestate, display, sounds

def runProgram(buttons, gamestate, display, sounds):
    """
    Run the program main loop

    Takes in a list of buttons in the main menu, and the starting game state.
    """
    while True:
        if gamestate == 1:
            display.fill((50, 95, 25))
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for i in buttons:    
                            i.buttonPressed()
                if event.type == QUIT:
                    terminate()
            gamestate = checkButtons(buttons, sounds)
            for i in buttons:
                i.displayButtons(display)
                
        elif gamestate == 2:
            display.fill((30, 75, 5))
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                    
        elif gamestate == 0:
            print('CONSOLE: Quitting game.')
            terminate()

        pygame.display.update()

def main():
    """
    Initialize data, then run the program.
    """
    buttons, gamestate, display, sounds = initialize()
    runProgram(buttons, gamestate, display, sounds)

if __name__ == '__main__':
    main()
