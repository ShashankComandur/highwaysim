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

def rng():
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
    
               


print(color_l)
print(color_r)
