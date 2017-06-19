
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUEISH = (0, 179, 60)
ROOF = (230, 57, 0)
SKY = (0, 0, 51)
DOOR = (255, 102, 0)
BLINDS = (0, 255, 255)
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
    screen.fill(SKY)
 
    # --- Drawing code should go here
    pygame.draw.rect(screen, BLACK, [20, 270, 300, 200], 0)
    pygame.draw.rect(screen,BLUEISH,[0,470,800,30],0)
    pygame.draw.polygon(screen, ROOF, [[170,100], [10,269], [320,270]], 0)
    pygame.draw.rect(screen, DOOR, [125, 370, 80, 100], 0)
    pygame.draw.rect(screen, WHITE, [70, 290, 60, 60], 0)
    pygame.draw.rect(screen, WHITE, [210, 290, 60, 60], 0)
    y_offset = 0
    for y_offset in range(210, 275, 1):
        pygame.draw.line(screen,BLUEISH,[130,80+y_offset],[70,80+y_offset],5)
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render("Privacy Please",True,BLINDS)
        screen.blit(text, [50, 270])
      
   

        
    
        
   
 
    # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
    # --- Limit to 60 frames per second
clock.tick(60)
 
# Close the window and quit.
pygame.quit()