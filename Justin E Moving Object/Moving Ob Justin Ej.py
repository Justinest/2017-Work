import pygame
 
#Functions
def draw_mike(screen, x, y):
    pygame.draw.rect(screen, GOLD, [150+x, 50+y, 230, 100])
    pygame.draw.circle(screen, GRAY, (200+x, 150+y), 20, 0)
    pygame.draw.circle(screen, GRAY, (330+x, 150+y), 20, 0)
    pygame.draw.line(screen, SKYROCKETBLUE, [150+x, 150+y], [150+x, 50+y], 50)
    pygame.draw.line(screen, GRAY, [150+x, 150+y], [150+x, 50+y], 25)
    pygame.draw.rect(screen, RED, [200+x, 69+y, 25, 25])
    pygame.draw.rect(screen, RED, [250+x, 69+y, 25, 25])
    pygame.draw.rect(screen, RED, [300+x, 69+y, 25, 25])
    pygame.draw.rect(screen, RED, [350+x, 69+y, 25, 25])
    pygame.draw.circle(screen, MIKE, (212+x, 84+y), 10, 0)
    pygame.draw.circle(screen, BLACK, (262+x, 84+y), 10, 0)
    pygame.draw.circle(screen, MIKE, (312+x, 84+y), 10, 0)
    pygame.draw.circle(screen, WHITE, (362+x, 84+y), 10, 0)
    

def draw_sun(screen, x, y):
    pygame.draw.circle(screen, GOLD, (300+x, 300+y), 70, 10)
    pygame.draw.circle(screen, SUN, (300+x, 300+y), 60, 0)
    pygame.draw.line(screen, YELLOW, [110+x, 340+y], [225+x, 300+y], 10)
    pygame.draw.line(screen, YELLOW, [110+x, 300+y], [225+x, 300+y], 10)
    pygame.draw.line(screen, YELLOW, [110+x, 380+y], [225+x, 300+y], 10)
    pygame.draw.line(screen, YELLOW, [110+x, 260+y], [225+x, 300+y], 10)
    pygame.draw.line(screen, YELLOW, [380+x, 300+y], [495+x, 300+y], 10)
    pygame.draw.line(screen, YELLOW, [380+x, 300+y], [445+x, 340+y], 10)
    pygame.draw.line(screen, YELLOW, [380+x, 300+y], [445+x, 380+y], 10)
    pygame.draw.line(screen, YELLOW, [380+x, 300+y], [445+x, 260+y], 10)    

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GOLD = (255, 215, 0)
GRAY = (119,136,153)
SKYROCKETBLUE = (30,144,255)
MIKE = (205,133,63)
YELLOW = (255,255,0)
SUN = (0, 0, 124)
SILVER = (192,192,192)

 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Speed of pixels
x_speed = 0
y_speed = 0

#Current Position
x_coord = 10
y_coord = 10
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            # User pressed down on a key
 
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3
 
        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0    
 
    # --- Game logic should go here
    pygame.mouse.set_visible(False)
    pos = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]    
    x_coord = x_coord + x_speed    
    y_coord = y_coord + y_speed    
    
    #Borders
    if x_coord > 200:
        x_coord = 200
    if x_coord < -100:
        x_coord = -100
    if y_coord > 125:
        y_coord = 125
    if y_coord < -250:
        y_coord = -250
    
    
        
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(SILVER)
 
    # --- Drawing code should go here
    #road
    pygame.draw.rect(screen, BLACK, [1, 400, 800, 100])
    pygame.draw.line(screen, YELLOW, [1, 445], [800, 445], 15)
    draw_sun(screen, x_coord, y_coord)
    draw_mike(screen, x, y)
    
    
    
  
    
    

    
    
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()