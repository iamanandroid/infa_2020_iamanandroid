import pygame
import numpy
from pygame.draw import *
from random import randint

pygame.init()

# Constants
HEIGHT = 700
WIDTH = 1200
FPS = 60
DT = 0.5
ALPHA = 0
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (234, 0, 255)
LIGHTBLUE = (0, 196, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, PURPLE, LIGHTBLUE]

# Global constant
points = 0

# Functions

# Creating squares
def new_square():
    global square, speed
    square = []
    speed = []
    for i in range(5):
        x = randint(200, WIDTH - 350)
        y = randint(200, HEIGHT - 350)
        vx = DT * randint(3, 10) * (-1) ** (randint(1, 2))
        vy = DT * randint(3, 10) * (-1) ** (randint(1, 2))
        r = randint(60, 200)
        color = COLORS[randint(0, 7)]
        click = False
        angle = randint(0, 360)
        square.append([x, y, vx, vy, r, color, click, angle])
        v0 = DT * randint(1, 2) * (-1) ** (randint(1, 2))
        speed.append([square[i][2], square[i][3], v0])


# Creating balls
def new_ball():
    global ball
    ball = []
    for i in range(10):
        x = randint(200, WIDTH - 200)
        y = randint(200, HEIGHT - 200)
        vx = DT * randint(3, 10) * (-1) ** (randint(1, 2))
        vy = DT * randint(3, 10) * (-1) ** (randint(1, 2))
        r = randint(60, 200)
        color = COLORS[randint(0, 7)]
        click = False
        ball.append([x, y, vx, vy, r, color, click])


# Balls' reflection
def reflection_balls():
    for i in range(len(ball)):
        if ball[i][0] + ball[i][4] >= WIDTH or ball[i][0] <= ball[i][4]:
            ball[i][2] = -1 * ball[i][2]
            ball[i][0] = ball[i][0] + ball[i][2]
        elif ball[i][1] + ball[i][4] >= HEIGHT or ball[i][1] <= ball[i][4]:
            ball[i][3] = -1 * ball[i][3]
            ball[i][1] = ball[i][1] + ball[i][3]


# Squares' reflection

def reflection_squares():
    for i in range(len(square)):
        if square[i][0] + square[i][4] >= WIDTH or square[i][0] <= 0:
            square[i][2] = -1 * square[i][2]
            square[i][7] = square[i][7] + 180
            square[i][0] = square[i][0] + square[i][2]
        elif square[i][1] + square[i][4] >= HEIGHT or square[i][1] <= 0:
            square[i][3] = -1 * square[i][3]
            square[i][7] = square[i][7] + 180
            square[i][1] = square[i][1] + square[i][3]


# balls' movements
def move_ball():
    for i in range(len(ball)):
        circle(screen, ball[i][5], (ball[i][0], ball[i][1]), ball[i][4] // 2)
        ball[i][0] = ball[i][0] + ball[i][2]
        ball[i][1] = ball[i][1] + ball[i][3]


# Squares' movements
def move_square():
    global rect1
    rect1 = []
    for i in range(len(square)):
        rect1.append(pygame.Rect(square[i][0], square[i][1], square[i][4], square[i][4]))
        rect(screen, square[i][5], rect1[i])
        circle(screen, WHITE, rect1[i].center, square[i][4] // 2)
        square[i][7] = square[i][7] + 1
        square[i][0] = square[i][0] + square[i][2]
        square[i][1] = square[i][1] + square[i][3]
        square[i][2] = speed[i][0] * numpy.cos(square[i][7] * numpy.pi / 180) + speed[i][2]
        square[i][3] = speed[i][1] * numpy.sin(square[i][7] * numpy.pi / 180)


# Points for clicking on balls
def score_ball():
    global points
    for i in range(len(ball)):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if (event.pos[0] - ball[i][0]) ** 2 + (event.pos[1] - ball[i][1]) ** 2 <= ball[i][4] ** 2 / 4:
                ball[i][6] = True
                points += 1


# Giving points for clicking on squares
def score_square():
    global points
    for i in range(len(square)):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if 1 / 2 * (square[i][4]) ** 2 > (event.pos[0] - rect1[i].center[0]) ** 2 + (
                    event.pos[1] - rect1[i].center[1]) ** 2 > (square[i][4] // 2) ** 2:
                square[i][6] = True
                points += 2


# Creating new objects after clicking on them
def blow(ball):
    for i in range(len(ball)):
        if ball[i][6]:
            ball[i][0] = randint(200, WIDTH - 200)
            ball[i][1] = randint(200, HEIGHT - 200)
            ball[i][2] = DT * randint(3, 10) * (-1) ** (randint(1, 2))
            ball[i][3] = DT * randint(3, 10) * (-1) ** (randint(1, 2))
            ball[i][4] = randint(60, 200)
            ball[i][5] = COLORS[randint(0, 7)]
            ball[i][6] = False
            v0 = DT * randint(1, 2) * (-1) ** (randint(1, 2))
            speed.append([ball[i][2], ball[i][3], v0])


# Players' score
def leaders():
    A = []
    with open('leaders.txt') as file:
        for line in file:
            A.append(line.split())
    A.append([str(text), str(points)])
    for i in range(len(A)):
        if len(A[i]) > 2:
            num = ''.join(A[i][-1::])
            A[i] = [' '.join(A[i][:-1:])]
            A[i].append(num)

    def number_of_point(point):
        name_text, number = point
        return int(number)

    points_by_number = sorted(A, key=number_of_point, reverse=True)
    for i in range(len(points_by_number)):
        points_by_number[i] = ' '.join(points_by_number[i])
    points_by_number_str = '\n'.join(points_by_number)
    output = open('leaders.txt', 'w')
    output.write(points_by_number_str)
    output.close()


# Settings
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.mixer.music.load('sponge_bob.mp3')
pygame.mixer.music.play(-1)
clock = pygame.time.Clock()
font_surface = pygame.font.SysFont('comic sans', 48)
text = ' '
finished = False

# Main menu
while not finished:
    clock.tick(FPS)
    title = font_surface.render('Write your name, warrior! ', True, BLACK)
    name = font_surface.render(text, True, BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
            pygame.mixer.music.pause()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                finished = True
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            elif event.key == pygame.K_RETURN:
                finished = True
                pygame.mixer.music.pause()
            else:
                text += event.unicode

    screen.blit(title, (WIDTH // 2 - 230, HEIGHT // 2 - 160))
    screen.blit(name, (WIDTH // 2 - 230, HEIGHT // 2 - 100))
    pygame.display.update()
    screen.fill(WHITE)

# The game
finished = False
pygame.mixer.music.load('14th sonata.mp3')
pygame.mixer.music.play(-1)
new_ball()
new_square()
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                finished = True
    title = font_surface.render('Score:', True, BLACK)
    screen.blit(title, (20, 10))
    score = font_surface.render(str(points), True, BLACK)
    screen.blit(score, (150, 10))
    reflection_balls()
    reflection_squares()
    score_square()
    score_ball()
    blow(ball)
    blow(square)
    move_square()
    move_ball()
    pygame.display.update()
    screen.fill(WHITE)
leaders()
pygame.quit()
