import pygame as pg
from pygame.locals import *
 
# COLORS
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED =   (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE =  (  0,   0, 255)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450

GAME_NAME = "GAME_NAME_HERE"

def main():

	pg.init() 
	clock = pg.time.Clock()
	# SCREEN SIZE
	size = (SCREEN_WIDTH, SCREEN_HEIGHT)
	screen = pg.display.set_mode(size)
	pg.display.set_caption(GAME_NAME)
	 
	# Loop until the user clicks the close button.
	done = False

	# -------- Main Program Loop -----------
	while not done:
		# --- Main event loop
		for event in pg.event.get():
			if event.type == pg.QUIT:
				done = True
			if event.type == KEYUP:
				if event.key == K_ESCAPE or event.key == K_q:
				   done = True
	 
		# --- Game logic should go here
	 
		# --- Clear the Screen (or fill with BG)
		screen.fill(WHITE)
	 
		# --- Drawing code should go here
	 
		# --- Go ahead and update the screen with what we've drawn.
		pg.display.flip()
	 
		# --- Limit to 60 frames per second
		clock.tick(60)
	 
	# Close the window and quit.
	pg.quit()


if __name__ == "__main__":
	main()
