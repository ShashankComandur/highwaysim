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

def rng(x, y):
    return random.randrange(x, y)

num_cars = 1
cars = []
for i in range(num_cars):
    x = 235
    y = rng(-800, -200)
    a = 465
    b = rng(800, 1400)


def color_randomizer(n):
    if n == 1:
        color = WHITE
    if n == 2:
        color = BLACK
    if n == 3:
        color = RED
    if n == 4:
        color = ORANGE
    if n == 5:
        color = YELLOW
    if n == 6:
        color = GREEN
    if n == 7:
        color = BLUE
    if n == 8:
        color = PURPLE
    if n == 9:
        color = PINK
    return color

n = rng(1, 10)
color = color_randomizer(n)
loc = [x, y, color, a, b]
cars.append(loc)               
    
def draw_cars(loc):
    x = loc[0]
    y = loc[1]
    color = loc[2]
    a = loc[3]
    b = loc[4]
    pygame.draw.rect(screen, color, [x + 20, y + 20, 60, 40])
    pygame.draw.rect(screen, color, [a + 20, b + 20, 60, 40])
    
#--------------------------------------------------------------------------------------------------------------------

# Make Trucks
num_trucks = 1
trucks = []
for i in range(num_trucks):
    x = 110
    y = rng(-500, -200)
    a = 595
    b = rng(-800, -200)
    loc = [x, y, color, a, b]
    trucks.append(loc)

n = rng(1, 10)
color = color_randomizer(n)
loc = [x, y, color, a, b]
trucks.append(loc)

def draw_trucks(loc):
    x = loc[0]
    y = loc[1]
    color = loc[2]
    a = loc[3]
    b = loc[4]
    pygame.draw.rect(screen, color, [x + 20, y + 20, 60, 40])
    pygame.draw.rect(screen, color, [a + 20, b + 20, 60, 40])

#--------------------------------------------------------------------------------------------------------------------
   
# Game Loop
done = False

while not done:
    # Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Game Logic
    
    # Cars (Left Side)
    for a in cars:
        a[1] += 3.5
        if a[1] > 600:
            a[1] = rng(-800, -200)

    # Cars (Right Side)
    for a in cars:
        a[4] -= 3.5
        if a[4] < -600:
            a[4] = rng(800, 1400)

    # Trucks (Right Side)                 
    for a in trucks:
        a[1] += 2.5
        if a[1] > 650:
           a[1] = rng(-800, -200)

    # Trucks (Left Side)
    for a in trucks:
        a[3] -= 2.5
        if a[3] < -600:
           a[3] = rng(1000, 1600)
                                   
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

#--------------------------------------------------------------------------------------------------------------------


