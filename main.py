import pygame
import constants

# While this method returns True, the game loop will keep running
def handle_user_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

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
    pygame.init()
    if not pygame.get_init():
        raise Exception("pygame was not initialized!")
    # The pygame.display.set_mode returns a Surface
    screen = pygame.display.set_mode(constants.SCREEN_TUPLE)
    # Let's create a clock to help the game run at 60 FPS
    # This way, we won't consume too much CPU
    clk = pygame.time.Clock()
    # Variable to save the delta time
    dt = 0
    # The delta time represent the amount of time it has passed since
    # the last frame was drawn
    while handle_user_input():
        screen.fill(constants.SOLID_BLACK_COLOR)
        pygame.display.update()
        dt = clk.tick(60) / 1000

if __name__ == "__main__":
    main()
