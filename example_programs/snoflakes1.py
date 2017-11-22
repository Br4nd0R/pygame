import pygame
import random
 
# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0 , 255)

COLORS = [RED, GREEN, BLUE]

def randColor():
    return COLORS[random.randrange(len(COLORS))]

# SCREEN
WIDTH = 600
HEIGHT = 600

class Snowflake:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def __iter__(self):
        return self

    def move(self):
        self.y += self.size
        if(self.y > HEIGHT):
            self.y = -10
            self.x = random.randrange(0, WIDTH)

    def render(self, screen):
        pygame.draw.circle(screen, WHITE, [self.x, self.y], self.size)



def main():
    pygame.init()
     

    # SCREEN SIZE

    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Snowflakes! ZOMG!")
     
    # Loop until the user clicks the close button.
    done = False
     
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    NUM_FLAKES = 500;
    snowflakes = []
    for i in range(NUM_FLAKES):
        x = random.randrange(0, WIDTH)
        y = random.randrange(0, HEIGHT)

        MIN_FLAKE_SIZE = 1
        MAX_FLAKE_SIZE = 5

        size = random.randrange(MIN_FLAKE_SIZE, MAX_FLAKE_SIZE)
        flake = Snowflake(x, y, size)
        snowflakes.append(flake)

    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
     
        # --- Game logic should go here
     
        # --- Screen-clearing code goes here
     
        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
     
        # If you want a background image, replace this clear with blit'ing the
        # background image.
        screen.fill(BLACK)

        for flake in snowflakes:
            flake.render(screen)
            flake.move()
     
        # --- Drawing code should go here
     
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
        # --- Limit to 60 frames per second
        clock.tick(60)
     
    # Close the window and quit.
    pygame.quit()


if __name__ == "__main__":
    main()