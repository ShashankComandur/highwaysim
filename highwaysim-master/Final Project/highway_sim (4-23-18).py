# APCS-P PT
# 4-30-18
# Shashank Comandur

#--------------------------------------------------------------------------------------------------------------------

# Imports
import pygame
import random

# Game Engine 
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Highway Simulator"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Clock / Refresher
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
GREY = (40, 40, 40)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0 ,0)
ORANGE = (255,165,0)
YELLOW = (255, 255, 0)
GREEN = (55, 230, 55)
BLUE = (0, 0, 255)
PURPLE = (98,39,174)
PINK = (238,130,238)


#--------------------------------------------------------------------------------------------------------------------

# Make Cars
num_cars = 1
cars = []
for i in range(num_cars):
    x = 235
    y = random.randrange(-800, -200)
    a = 465
    b = random.randrange(800, 1400)

    # Randomizer
    n = random.randrange(1, 10)
    if n == 1:
        color_l = WHITE
        color_r = BLACK
    if n == 2:
        color_l = BLACK
        color_r = RED
    if n == 3:
        color_l = RED
        color_r = ORANGE
    if n == 4:
        color_l = ORANGE
        color_r = YELLOW
    if n == 5:
        color_l = YELLOW
        color_r = GREEN
    if n == 6:
        color_l = GREEN
        color_r = BLUE
    if n == 7:
        color_l = BLUE
        color_r = PURPLE
    if n == 8:
        color_l = PURPLE
        color_r = PINK
    if n == 9:
        color_l = PINK
        color_r = WHITE

loc = [x, y, color_l, color_r, a, b]
cars.append(loc)               
    
def draw_cars(loc):
    x = loc[0]
    y = loc[1]
    color_l = loc[2]
    color_r = loc[3]
    a = loc[4]
    b = loc[5]
    pygame.draw.rect(screen, color_l, [x + 20, y + 20, 60, 40])
    pygame.draw.rect(screen, color_r, [a + 20, b + 20, 60, 40])

print(color_l)
print(color_r)
    
#--------------------------------------------------------------------------------------------------------------------

# Make Trucks
num_trucks = 1
trucks = []
for i in range(num_trucks):
    x = 110
    y = random.randrange(-500, -200)
    a = 595
    b = random.randrange(-800, -200)
    loc = [x, y, a, b]
    trucks.append(loc)

def draw_trucks(loc):
    x = loc[0]
    y = loc[1]
    a = loc[2]
    b = loc[3]
    pygame.draw.rect(screen, GREEN, [x + 20, y + 20, 60, 40])
    pygame.draw.rect(screen, GREEN, [a + 20, b + 20, 60, 40])

#--------------------------------------------------------------------------------------------------------------------
   
# Game Loop
done = False

while not done:
    # Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Game Logic
    
    for c in cars:
        c[1] += 3.5
        if c[1] > 600:
            c[1] = random.randrange(-800, -200)

    for c in cars:
        c[4] -= 3.5
        if c[4] < -600:
            c[4] = random.randrange(800, 1400)
                         
    for c in trucks:
        c[1] += 2.5
        if c[1] > 650:
           c[1] = random.randrange(-800, -200)

    for c in trucks:
        c[3] -= 2.5
        if c[3] < -600:
           c[3] = random.randrange(1000, 1600)
                                   
    # Drawing Code

    ''' Ground '''
    screen.fill(GREEN)

    ''' Highway Border '''
    pygame.draw.line(screen, WHITE, [100, 0], [100, 600], 8)
    pygame.draw.line(screen, WHITE, [340, 0], [340, 600], 8)
    pygame.draw.line(screen, WHITE, [460, 0], [460, 600], 8)
    pygame.draw.line(screen, WHITE, [700, 0], [700, 600], 8)

    ''' Road '''
    pygame.draw.rect(screen, GREY, [105, 0, 232, 600])
    pygame.draw.rect(screen, GREY, [465, 0, 232, 600])

    ''' Dashed Lane Stripes (Left Side) '''
    x = 220
    for y in range(0 , 600 , 60):
        pygame.draw.line(screen, WHITE, [x, y], [x, y+30], 10)
    pygame.draw.line(screen, WHITE, [220, 595], [220, 620], 10)

    ''' Dashed Lane Stripes (Right Side)'''
    x = 580
    for y in range(0 , 600 , 60):
        pygame.draw.line(screen, WHITE, [x, y], [x, y+30], 10)
    pygame.draw.line(screen, WHITE, [580, 595], [580, 620], 10)

    ''' Cars '''
    for c in cars:
        draw_cars(c)

    ''' Trucks '''
    for c in trucks:
        draw_trucks(c)


    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

#--------------------------------------------------------------------------------------------------------------------

# Close window on quit
pygame.quit()


