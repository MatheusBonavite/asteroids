import pygame
import constants

# The simplest game loop has 3 steps:
# 1 - Check for player inputs
# 2 - Update the game world
# 3 - Draw the game to the screen
# --- Remember: to create a good user experience,
# ---           such steps should happen many times per second
def main():
    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()
