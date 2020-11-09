import pygame
from pygame.draw import *

pygame.init()
FPS = 30

# Size of screen
x = 800
y = 1000
screen = pygame.display.set_mode((x, y))

a = 1  # Scale coefficient for an abscissas' axis
b = 1  # Scale coefficient for an ordinates' axis

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (201, 54, 54)  # For an apple
GREEN = (121, 153, 41)  # For an apple
DARK_GREEN = (35, 46, 8)  # For a grass
DARK_BLUE = (6, 40, 54)  # For a sky
LIGHT_GREEN = (213, 230, 147)  # For an alien
LIGHT_GREY_CLOUDS = (99, 99, 99)  # For clouds
DARK_GREY_CLOUDS = (46, 46, 46)  # For clouds
LIGHTEST_GREY_UFO = (181, 181, 181)  # For a UFO's porthole
LIGHT_GREY_UFO = (119, 120, 116)  # For a UFO's carcass


# Draw a sky with clouds
def sky_with_clouds():
    image_sky_with_clouds = pygame.Surface((int(x * a), int(y * b)))
    image_sky_with_clouds.set_colorkey(BLACK)
    image_sky_with_clouds.set_alpha(200)
    rect(image_sky_with_clouds, DARK_GREEN, (0, int(y / 2), x, y))
    rect(image_sky_with_clouds, DARK_BLUE, (0, 0, x, int(y / 2)))
    ellipse(image_sky_with_clouds, DARK_GREY_CLOUDS, (200, 300, 700, 100))
    ellipse(image_sky_with_clouds, LIGHT_GREY_CLOUDS, (-100, 50, 700, 100))
    ellipse(image_sky_with_clouds, LIGHT_GREY_CLOUDS, (-100, 150, 700, 100))
    ellipse(image_sky_with_clouds, LIGHT_GREY_CLOUDS, (500, 00, 700, 100))
    ellipse(image_sky_with_clouds, LIGHT_GREY_CLOUDS, (300, 50, 700, 100))
    ellipse(image_sky_with_clouds, LIGHT_GREY_CLOUDS, (400, 200, 700, 100))
    ellipse(image_sky_with_clouds, LIGHT_GREY_CLOUDS, (-200, 50, 700, 100))
    ellipse(image_sky_with_clouds, LIGHT_GREY_CLOUDS, (-200, 250, 700, 100))
    ellipse(image_sky_with_clouds, LIGHT_GREY_CLOUDS, (500, 250, 700, 100))
    ellipse(image_sky_with_clouds, LIGHT_GREY_CLOUDS, (500, 350, 700, 100))
    ellipse(image_sky_with_clouds, DARK_GREY_CLOUDS, (100, 50, 700, 100))
    surf = pygame.transform.smoothscale(image_sky_with_clouds, (int(x * a / 60), int(y * b / 60)))
    image_sky_with_clouds = pygame.transform.smoothscale(surf, (int(x * a), int(y * b)))
    screen.blit(image_sky_with_clouds, (0, 0))


# Draw an ufo in particular place (d,e) with a given scale (a,b)
def ufo(a, b, d, e):
    image_light_of_ufo = pygame.Surface((int(x * a), int(y * b)))
    image_light_of_ufo.set_colorkey(BLACK)
    image_light_of_ufo.set_alpha(100)
    polygon(image_light_of_ufo, WHITE, [(int(20 * a), int(b * 800)), (int(a * 200), int(b * 450)), (int(a * 400),
                                                                                                    int(b * 800))
                                        ])
    image_ufo = pygame.Surface((int(x * a), int(y * b)))
    image_ufo.set_colorkey(BLACK)
    image_ufo.set_alpha(255)
    ellipse(image_ufo, LIGHT_GREY_UFO, (int(a * 10), int(b * 400), int(a * 380), int(b * 120)))
    ellipse(image_ufo, LIGHTEST_GREY_UFO, (int(a * 60), int(b * 390), int(a * 280), int(b * 90)))
    ellipse(image_ufo, WHITE, (int(a * 30), int(b * 450), int(a * 40), int(b * 15)))
    ellipse(image_ufo, WHITE, (int(a * 340), int(b * 450), int(a * 40), int(b * 15)))
    ellipse(image_ufo, WHITE, (int(a * 80), int(b * 475), int(a * 40), int(b * 15)))
    ellipse(image_ufo, WHITE, (int(a * 300), int(b * 475), int(a * 40), int(b * 15)))
    ellipse(image_ufo, WHITE, (int(a * 150), int(b * 490), int(a * 40), int(b * 15)))
    ellipse(image_ufo, WHITE, (int(a * 230), int(b * 490), int(a * 40), int(b * 15)))
    screen.blit(image_light_of_ufo, (d, e))
    screen.blit(image_ufo, (d, e))


# Draw an alien in particular place (d,e) with a given scale (a,b)
def alien(a, b, d, e):
    image_alien = pygame.Surface((int(x * a), int(y * b)), pygame.SRCALPHA)
    aln = [[int(18 * a), int(21 * b)], [int(17 * a), int(22 * b)], [int(16 * a), int(23 * b)],
           [int(16 * a), int(32 * b)],
           [int(23 * a), int(43 * b)],
           [int(20 * a), int(47 * b)], [int(21 * a), int(58 * b)], [int(24 * a), int(74 * b)],
           [int(27 * a), int(79 * b)],
           [int(30 * a), int(89 * b)], [int(38 * a), int(99 * b)],
           [int(43 * a), int(106 * b)], [int(52 * a), int(112 * b)], [int(61 * a), int(117 * b)],
           [int(84 * a), int(118 * b)],
           [int(94 * a), int(115 * b)],
           [int(102 * a), int(112 * b)], [int(108 * a), int(105 * b)], [int(115 * a), int(97 * b)],
           [int(122 * a), int(84 * b)],
           [int(135 * a), int(74 * b)],
           [int(143 * a), int(65 * b)], [int(149 * a), int(57 * b)], [int(159 * a), int(49 * b)],
           [int(161 * a), int(43 * b)],
           [int(161 * a), int(32 * b)], [int(158 * a), int(24 * b)], [int(152 * a), int(20 * b)],
           [int(140 * a), int(15 * b)],
           [int(133 * a), int(14 * b)], [int(23 * a), int(17 * b)]]
    for i in range(len(aln)):
        aln[i][0] = aln[i][0] + int(300 * a)
        aln[i][1] = aln[i][1] + int(300 * b)
    polygon(image_alien, LIGHT_GREEN, aln)
    ellipse(image_alien, BLACK, (int(a * 340), int(b * 335), int(a * 40), int(b * 40)))
    ellipse(image_alien, WHITE, (int(a * 360), int(b * 355), int(a * 10), int(b * 10)))
    ellipse(image_alien, BLACK, (int(a * 410), int(b * 335), int(a * 30), int(b * 30)))
    ellipse(image_alien, WHITE, (int(a * 425), int(b * 350), int(a * 10), int(b * 10)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 320), int(b * 295), int(a * 10), int(b * 20)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 310), int(b * 275), int(a * 20), int(b * 20)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 300), int(b * 265), int(a * 20), int(b * 10)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 300), int(b * 250), int(a * 20), int(b * 20)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 440), int(b * 305), int(a * 20), int(b * 20)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 450), int(b * 295), int(a * 10), int(b * 20)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 456), int(b * 275), int(a * 20), int(b * 20)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 480), int(b * 265), int(a * 20), int(b * 15)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 510), int(b * 265), int(a * 20), int(b * 30)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 320), int(b * 420), int(a * 100), int(b * 200)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 410), int(b * 440), int(a * 40), int(b * 40)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 430), int(b * 460), int(a * 40), int(b * 20)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 470), int(b * 470), int(a * 40), int(b * 20)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 300), int(b * 440), int(a * 40), int(b * 40)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 280), int(b * 470), int(a * 40), int(b * 20)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 260), int(b * 490), int(a * 20), int(b * 20)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 310), int(b * 570), int(a * 40), int(b * 70)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 300), int(b * 620), int(a * 30), int(b * 70)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 270), int(b * 650), int(a * 40), int(b * 40)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 400), int(b * 570), int(a * 40), int(b * 70)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 420), int(b * 620), int(a * 30), int(b * 70)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 440), int(b * 650), int(a * 40), int(b * 40)))
    ellipse(image_alien, RED, (int(a * 500), int(b * 420), int(a * 65), int(b * 65)))
    apple1 = []
    for i in range(30):
        apple1.append([int((532 + i) * a), int(b * (425 - 4 * i ** (1 / 2)))])
    lines(image_alien, BLACK, False, apple1)
    apple2 = []
    for i in range(30):
        apple2.append([int((535 - i) * a), int(b * (415 - 4 * i ** (1 / 2)))])
    polygon(image_alien, GREEN, apple2)
    screen.blit(image_alien, (d, e))


# Draw a flipped alien in particular place (d,e) with a given scale (a,b)
def flipped_alien(a, b, d, e):
    image_alien = pygame.Surface((int(x * a), int(y * b)), pygame.SRCALPHA)
    aln = [[int(18 * a), int(21 * b)], [int(17 * a), int(22 * b)], [int(16 * a), int(23 * b)],
           [int(16 * a), int(32 * b)],
           [int(23 * a), int(43 * b)],
           [int(20 * a), int(47 * b)], [int(21 * a), int(58 * b)], [int(24 * a), int(74 * b)],
           [int(27 * a), int(79 * b)],
           [int(30 * a), int(89 * b)], [int(38 * a), int(99 * b)],
           [int(43 * a), int(106 * b)], [int(52 * a), int(112 * b)], [int(61 * a), int(117 * b)],
           [int(84 * a), int(118 * b)],
           [int(94 * a), int(115 * b)],
           [int(102 * a), int(112 * b)], [int(108 * a), int(105 * b)], [int(115 * a), int(97 * b)],
           [int(122 * a), int(84 * b)],
           [int(135 * a), int(74 * b)],
           [int(143 * a), int(65 * b)], [int(149 * a), int(57 * b)], [int(159 * a), int(49 * b)],
           [int(161 * a), int(43 * b)],
           [int(161 * a), int(32 * b)], [int(158 * a), int(24 * b)], [int(152 * a), int(20 * b)],
           [int(140 * a), int(15 * b)],
           [int(133 * a), int(14 * b)], [int(23 * a), int(17 * b)]]
    for i in range(len(aln)):
        aln[i][0] = aln[i][0] + int(300 * a)
        aln[i][1] = aln[i][1] + int(300 * b)
    polygon(image_alien, LIGHT_GREEN, aln)
    ellipse(image_alien, BLACK, (int(a * 340), int(b * 335), int(a * 40), int(b * 40)))
    ellipse(image_alien, WHITE, (int(a * 360), int(b * 355), int(a * 10), int(b * 10)))
    ellipse(image_alien, BLACK, (int(a * 410), int(b * 335), int(a * 30), int(b * 30)))
    ellipse(image_alien, WHITE, (int(a * 425), int(b * 350), int(a * 10), int(b * 10)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 320), int(b * 295), int(a * 10), int(b * 20)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 310), int(b * 275), int(a * 20), int(b * 20)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 300), int(b * 265), int(a * 20), int(b * 10)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 300), int(b * 250), int(a * 20), int(b * 20)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 440), int(b * 305), int(a * 20), int(b * 20)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 450), int(b * 295), int(a * 10), int(b * 20)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 456), int(b * 275), int(a * 20), int(b * 20)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 480), int(b * 265), int(a * 20), int(b * 15)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 510), int(b * 265), int(a * 20), int(b * 30)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 320), int(b * 420), int(a * 100), int(b * 200)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 410), int(b * 440), int(a * 40), int(b * 40)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 430), int(b * 460), int(a * 40), int(b * 20)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 470), int(b * 470), int(a * 40), int(b * 20)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 300), int(b * 440), int(a * 40), int(b * 40)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 280), int(b * 470), int(a * 40), int(b * 20)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 260), int(b * 490), int(a * 20), int(b * 20)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 310), int(b * 570), int(a * 40), int(b * 70)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 300), int(b * 620), int(a * 30), int(b * 70)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 270), int(b * 650), int(a * 40), int(b * 40)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 400), int(b * 570), int(a * 40), int(b * 70)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 420), int(b * 620), int(a * 30), int(b * 70)))
    ellipse(image_alien, LIGHT_GREEN, (int(a * 440), int(b * 650), int(a * 40), int(b * 40)))
    ellipse(image_alien, RED, (int(a * 500), int(b * 420), int(a * 65), int(b * 65)))
    apple1 = []
    for i in range(30):
        apple1.append([int((532 + i) * a), int(b * (425 - 4 * i ** (1 / 2)))])
    lines(image_alien, BLACK, False, apple1)
    apple2 = []
    for i in range(30):
        apple2.append([int((535 - i) * a), int(b * (415 - 4 * i ** (1 / 2)))])
    polygon(image_alien, GREEN, apple2)
    image_alien = pygame.transform.flip(image_alien, True, False)
    screen.blit(image_alien, (d, e))


# Functions
circle(screen, WHITE, (x * 6 // 8, y // 5), 150)  # Draw the Moon
sky_with_clouds()  # Draw sky with clouds
rect(screen, DARK_GREEN, (0, y // 2, x, y))  # Draw a grass
flipped_alien(0.3, 0.3, 100, 450)  # Draw an alien
ufo(0.3, 0.3, 300, 300)  # Draw an ufo
ufo(0.5, 0.5, 500, 200)
ufo(1, 1, 0, -100)
flipped_alien(0.4, 0.4, 200, 700)
flipped_alien(0.4, 0.4, -60, 550)
alien(0.8, 0.8, 300, 400)

# Initialize picture
pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
