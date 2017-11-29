import pygame
import math
 
# -- Global constants
 
# Colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE  = ( 50,  50, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
 
# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def getDistance(x1, y1, x2, y2):
    return math.sqrt(((x1 - x2)**2) + ((y1 - y2)**2))

class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.surface([2, 2])
        self.imgage.fill(RED)


class Enemy(pygame.sprite.Sprite):
    # Constructor function
    def __init__(self, x, y, targetSprite):
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(GREEN)

        # Set the thing we are going to head towards
        self.target = targetSprite
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        self.walls = None
 
    def __iter__(self):
        return self

    """    
    def setTarget(targetSprite):
        self.target = targetSprite
    """
    def changespeed(self):

        #Find the direction of our target
        #(change in x / change in y)
        dir_x = (self.target.rect.x - self.rect.x) * 0.03
        dir_y = (self.target.rect.y - self.rect.y) * 0.03

        if dir_x < 1 and dir_x > 0:
            dir_x = 1
        elif dir_x < 0 and dir_x > -1:
            dir_x = -1

        if dir_y < 1 and dir_y > 0:
            dir_y = 1
        elif dir_y < 0 and dir_y > -1:
            dir_y = -1

        self.change_x = dir_x
        self.change_y = dir_y
 
    def update(self):
        """ Update the player position. """
        # Move left/right
        self.rect.x += self.change_x
 
        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, target_x, target_y):
        super().__init__()
        self.image = pygame.Surface([5, 5])
        self.image.fill(RED)

        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

        #calculate direction (change in x / change in y)
        self.change_x = (target_x - self.rect.x) * 0.07
        self.change_y = (target_y - self.rect.y) * 0.07

        self.walls = None

    def __iter__(self):
        return self

    def changespeed(self, x, y):
        """ Change the speed of the player. """
        self.change_x += x
        self.change_y += y
 
    def update(self):
        """ Update the player position. """
        # Move left/right
        self.rect.x += self.change_x
        # Move up/down
        self.rect.y += self.change_y
        
    def collidesWith(self, spritesToCheck):
        hit_list = pygame.sprite.spritecollide(self, spritesToCheck, False)
        if hit_list: 
            return True
        else: 
            return False
 
class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the player
    controls. """
 
    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(WHITE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
        # Set speed vector
        self.change_x = 0
        self.change_y = 0
        self.walls = None
 
    def __iter__(self):
        return self

    def changespeed(self, x, y):
        """ Change the speed of the player. """
        self.change_x += x
        self.change_y += y
 
    def update(self):
        """ Update the player position. """
        # Move left/right
        self.rect.x += self.change_x
 
        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
 
 
class Wall(pygame.sprite.Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()
 
        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(BLUE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
 
    def __iter__(self):
        return self
 
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
 
# Set the title of the window
pygame.display.set_caption('Test')
 
# List to hold all the sprites
all_sprite_list = pygame.sprite.Group()
 
# Make the walls. (x_pos, y_pos, width, height)
wall_list = pygame.sprite.Group()
# Bullets flying around the screen
bullets = pygame.sprite.Group()
 
wall = Wall(0, 0, 10, 600)
wall_list.add(wall)
all_sprite_list.add(wall)
 
wall = Wall(10, 0, 790, 10)
wall_list.add(wall)
all_sprite_list.add(wall)
 
wall = Wall(10, 200, 100, 10)
wall_list.add(wall)
all_sprite_list.add(wall)
 
# Create the player paddle object
player = Player(50, 50)
player.walls = wall_list
all_sprite_list.add(player)

enemy = Enemy (400, 300, player)
enemy.walls = wall_list
enemy_list = pygame.sprite.Group()
enemy_list.add(enemy)
all_sprite_list.add(enemy)

 
clock = pygame.time.Clock()
 
done = False

 
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                done = True
 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, -3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, 3)
            elif event.key == pygame.K_f:
                mouse_pos = pygame.mouse.get_pos()
                bullet = Projectile(player.rect.x, player.rect.y, mouse_pos[0], mouse_pos[1])
                bullet.walls = wall_list
                bullets.add(bullet)
                all_sprite_list.add(bullet)
 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(3, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-3, 0)
            elif event.key == pygame.K_UP:
                player.changespeed(0, 3)
            elif event.key == pygame.K_DOWN:
                player.changespeed(0, -3)

    enemy.changespeed()


    for bullet in bullets:
        if bullet.collidesWith(wall_list):
            bullets.remove(bullet)
            all_sprite_list.remove(bullet)

        if bullet.collidesWith(enemy_list):
            bullets.remove(bullet)
            all_sprite_list.remove(bullet)


    all_sprite_list.update()
    screen.fill(BLACK)
    all_sprite_list.draw(screen) 
    pygame.display.flip()
    clock.tick(60)
 
pygame.quit()