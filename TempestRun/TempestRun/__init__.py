from .Game import GAME
import sys, os

def run():
    sys.path.append(os.getcwd() + r"\assets")
    GAME()
