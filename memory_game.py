import pygame
import sys
import time

from game_logic import generate_colors, change_one_color

pygame.init()

WIDTH = 1000
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Memory Game")

font = pygame.font.SysFont(None, 40)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

score = 0
player_name = input("Enter your name: ")


boxes = []

BOX_SIZE = 120
MARGIN = 30

start_x = 110
start_y = 150


def create_boxes():
    rects = []

    for row in range(2):
        for col in range(5):

            x = start_x + col * (BOX_SIZE + MARGIN)
            y = start_y + row * (BOX_SIZE + MARGIN)

            rect = pygame.Rect(x, y, BOX_SIZE, BOX_SIZE)

            rects.append(rect)

    return rects


boxes = create_boxes()


def draw_boxes(colors):

    screen.fill(WHITE)

    title = font.render("Memory Game", True, BLACK)
    screen.blit(title, (390, 40))

    score_text = font.render(f"Score: {score}/5", True, BLACK)
    screen.blit(score_text, (50, 40))

    for i in range(10):
        pygame.draw.rect(screen, colors[i], boxes[i])

    pygame.display.update()


def wait_for_click(correct_index):

    global score

    clicked = False

    while not clicked:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                mouse_pos = pygame.mouse.get_pos()

                for i, rect in enumerate(boxes):

                    if rect.collidepoint(mouse_pos):

                        if i == correct_index:
                            score += 1
                            show_message("Correct!", (0, 180, 0))
                        else:
                            show_message("Incorrect!", (200, 0, 0))

                        clicked = True


def show_message(text, color):

    message = font.render(text, True, color)

    screen.blit(message, (420, 520))

    pygame.display.update()

    time.sleep(1)

def start_screen():

    screen.fill(WHITE)

    title = font.render("Memory Game", True, BLACK)
    screen.blit(title, (380, 80))

    directions1 = font.render("Memorize the colors.", True, BLACK)
    directions2 = font.render("One box will change.", True, BLACK)
    directions3 = font.render("Click the box that changed.", True, BLACK)
    directions4 = font.render("Get 5 correct to win!", True, BLACK)

    screen.blit(directions1, (280, 200))
    screen.blit(directions2, (280, 250))
    screen.blit(directions3, (280, 300))
    screen.blit(directions4, (280, 350))

    start_text = font.render("Click anywhere to start", True, (0, 100, 200))
    screen.blit(start_text, (300, 450))

    pygame.display.update()

    waiting = True

    while waiting:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                waiting = False




def play_round():

    colors = generate_colors()

    draw_boxes(colors)

    time.sleep(2)

    new_colors, correct_index = change_one_color(colors)

    draw_boxes(new_colors)

    wait_for_click(correct_index)


def win_screen():

    screen.fill(WHITE)

    win_text = font.render("You Won the Game!", True, (0, 150, 0))

    screen.blit(win_text, (320, 250))

    pygame.display.update()

    time.sleep(3)

    pygame.quit()
    sys.exit()
    
start_screen()

while True:

    if score >= 5:
        win_screen()

    play_round()