
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (102, 51, 0)

def print_instructions():
    print("Welcome to Mudball! The idea is to hit the other player with a mudball.")
    print("Enter your angle (in degrees) and the amount of PSI to charge your gun")
    print("with.")
def draw_tree(screen, x, y):
    pygame.draw.rect(screen, BROWN, [60+x, 170+y, 30, 45])
    pygame.draw.polygon(screen, GREEN, [[150+x,170+y],[75+x,20+y], [x,170+y]])
    pygame.draw.polygon(screen, GREEN, [[140+x,120+y], [75+x,y], [10+x,120+y]])
def volume_sphere(radius):
    pi = 3.141592653589
    volume = (4 / 3) * pi * radius ** 3
    print("The volume is", volume)
def volume_cylinder(radius, height):
    pi = 3.141592653589
    volume = pi * radius ** 2 * height
    return volume
def sum_two_numbers(a, b):
    result = a + b
    return result
def volume_cylinder(radius, height):
    """Returns volume of a cylinder given radius, height."""
    pi = 3.141592653589
    volume = pi * radius ** 2 * height
    return volume
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
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
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    draw_tree(screen, 0, 230)
    draw_tree(screen, 200, 230)
    draw_tree(screen, 400, 230)     
    my_result = sum_two_numbers(22, 15)
    six_pack_volume = volume_cylinder(2.5, 5) * 6
    
 
    
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()