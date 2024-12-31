import pygame
import constants
import util.shapes.player as player

# While this method returns True, the game loop will keep running
def handle_user_input():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True
# Update everybody in the updates group
def update_all(dt):
    for updatable in constants.UPDATABLE_GROUP:
        updatable.update(dt)

# Draw everybody in the drawable group
def draw_all(screen):
    for drawable in constants.DRAWABLE_GROUP:
        drawable.draw(screen)

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

    # Instantiate a player
    player.Player.containers = (constants.UPDATABLE_GROUP, constants.DRAWABLE_GROUP)
    player_shape = player.Player(constants.PLAYER_START_X, constants.PLAYER_START_Y)
    while handle_user_input():
        screen.fill(constants.SOLID_BLACK_COLOR)
        # Update the player rotation
        update_all(dt)
        # Always re-render the player on the screen
        draw_all(screen)
        pygame.display.update()
        dt = clk.tick(60) / 1000

if __name__ == "__main__":
    main()
