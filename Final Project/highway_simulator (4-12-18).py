# APCS-P PT
# 4-30-18
# Shashank Comandur 

#--------------------------------------------------------------------------------------------------------------------

# Imports
import pygame
import random

# Game Engine Initialization
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Highway Simulator"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 30

# Colors
GREEN = (55, 230, 55)
WHITE = (255, 255, 255)
GREY = (40, 40, 40)

#--------------------------------------------------------------------------------------------------------------------

# Make Cars
num_cars = 8
cars_left = []
cars_right = []
for i in range(num_cars):
    x = 235
    y = random.randrange(-50, 200)
    a = 595
    b = random.randrange(-50, 200)
    loc_left = [x, y]
    loc_right = [a, b]
    cars_left.append(loc_left)
    cars_right.append(loc_right)
    

def draw_cars(loc_left):
    x = loc_left[0]
    y = loc_left[1]
    a = loc_right[0]
    b = loc_right[1]
    pygame.draw.rect(screen, WHITE, [x + 20, y + 20, 60, 40])
    pygame.draw.rect(screen, WHITE, [a + 20, b + 20, 60, 40])

#--------------------------------------------------------------------------------------------------------------------

# Make Trucks
num_trucks = 4
trucks = []
for i in range(num_trucks):
    x = 110
    y = random.randrange(-50, 200)
    loc = [x, y]
    trucks.append(loc)

def draw_trucks(loc):
    x = loc[0]
    y = loc[1]
    pygame.draw.rect(screen, GREEN, [x + 20, y + 20, 60, 40])

#--------------------------------------------------------------------------------------------------------------------
   
# Game loop
done = False

while not done:
    # Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     

    # Game Logic
    for c in cars_left:
        c[1] += 7
        if c[1] > 650:
           c[1] = random.randrange(-800, -200)
                      
    for c in cars_right:
        c[1] -= 7
        if c[1] < -50:
           c[1] = random.randrange(800, 1400)

    for c in trucks:
        c[1] += 5

        if c[1] > 650:
           c[1] = random.randrange(-800, -200)
                        
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
    for c in cars_left:
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
