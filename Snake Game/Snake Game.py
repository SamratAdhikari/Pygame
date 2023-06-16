# Snake Game

# modules
import pygame
import random
import os


#FPS
fps = 40

# music
pygame.mixer.init()

pygame.init()

# Colours
# name = (red, green, blue)
white = (255, 255, 255)
red = (223, 0, 9)
green = (0, 200, 0)
blue = (9, 0, 223)
black = (0, 0, 0)

screen_width = 900
screen_height = 600

# Window
game_window = pygame.display.set_mode((screen_width, screen_height))

# Background image
bgimg = pygame.image.load("background.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()

# Game Title
pygame.display.set_caption("Snake Game")
pygame.display.update()

clock = pygame.time.Clock()

# FUNCTIONS
    # to print score in game

font = pygame.font.SysFont(None, 55)
def text_screen(text, colour, x, y):
    screen_text = font.render(text, True, colour)
    game_window.blit(screen_text, [x, y])

    # to plot snakes
def plot_snake(game_window, colour, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(game_window, colour, [x, y, snake_size, snake_size])

# welcome
def welcome():
    exit_game = False
    while not exit_game:
        game_window.fill(white)
        text_screen("Welcome to Snake Game", black, 260, 250)
        text_screen("Press Enter to Play", green, 300, 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.load("BG.mp3")
                    pygame.mixer.music.play()
                    game_loop()
        pygame.display.update()
        clock.tick(fps)

#Game Loop and process
def game_loop():
    # Game Specific Variables
    exit_game = False
    game_over = False

    # Snake motion variables
    snake_x = 45
    snake_y = 45

    # size of snake
    snake_size = 15

    # velocity of snake
    init_velocity = 5
    velocity_x = 0
    velocity_y = 0

    # Food variable
    food_x = random.randint(20, screen_width / 1.5)
    food_y = random.randint(20, screen_height / 1.5)
    # growing the snake
    snk_list = []
    snk_length = 1
    # score
    score = 0

    # highscore check
    if not os.path.exists("Highscore.txt"):
        with open("Highscore.txt", "w") as f:
            f.write("0")
    with open("Highscore.txt", "r") as f:
        highscore = f.read()

    # while loop
    while not exit_game:
        # game over
        if game_over:
            with open("Highscore.txt", "w") as f:
                f.write(str(highscore))
            game_window.fill(white)
            text_screen("Game Over! Press Enter to Continue", red, 100, 250)

            for event in pygame.event.get():
                # to quit
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:
            for event in pygame.event.get():
                # to quit
                if event.type == pygame.QUIT:
                    print("\nQUIT")
                    exit_game = True

                # to detect pressed keys
                if event.type == pygame.KEYDOWN:
                    # right key
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                        # print("RIGHT Key")

                    # left key
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                        # print("LEFT Key")

                    # up key
                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0
                        # print("UP Key")

                    # down key
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                        # print("DOWN Key")

                    # CHEATS
                    if event.key == pygame.K_q:
                        score += 10


            # velocity update
            snake_x += velocity_x
            snake_y += velocity_y

            # Update score
            if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
                #pygame.mixer.music.load("beep.mp3")
                #pygame.mixer.music.play()
                score += 10

                # pygame.mixer.init(buffer=2048)
                #pygame.mixer.music.load("BG.mp3", )
                #pygame.mixer.music.play()

                # update position of the food
                food_x = random.randint(20, screen_width/1.5)
                food_y = random.randint(20, screen_height/1.5)

                # change the length of snake
                snk_length += 3

                # highscore
                if score>int(highscore):
                    highscore = score

            game_window.fill(white)
            game_window.blit(bgimg, (0, 0))
            text_screen(f"Score: {score}                  Highscore: {highscore}", blue, 3, 3)
            pygame.draw.rect(game_window, red, [food_x, food_y, snake_size, snake_size])

            # snake's head
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if len(snk_list)> snk_length:
                del snk_list[0]

            # to handle collision with itself
            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load("gameover.mp3")
                pygame.mixer.music.play()

            # game over functions
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load("gameover.mp3")
                pygame.mixer.music.play()

            plot_snake(game_window, black, snk_list, snake_size)

        pygame.display.update()
        clock.tick(fps)


    # quit the game
    pygame.quit()
    quit()
welcome()


import pkg_resources.py2_warn