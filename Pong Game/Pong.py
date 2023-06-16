# Pong Game

# Modules
import pygame
import sys
import random
from time import sleep


# Functions
# Ball animation
def ball_animation():
    # Global variables
    global ball_speed_x, ball_speed_y, player_score, opponent_score, score_timer
    
    # Balls movement
    BALL.x += ball_speed_x
    BALL.y += ball_speed_y
    
    # Conditions to bounce the ball
    if BALL.top <= 0 or BALL.bottom >= SCREEN_HEIGHT:
        ball_speed_y *= -1
        
    if BALL.left <= 0:
        # ball_restart()
        player_score += 1
        score_timer = pygame.time.get_ticks()
        
    if BALL.right >= SCREEN_WIDTH:
        # ball_restart()
        opponent_score += 1
        score_timer = pygame.time.get_ticks()
    
    # if BALL.left <= 0 or BALL.right >= SCREEN_WIDTH:
    #     ball_restart()
        
    if BALL.colliderect(PLAYER) or BALL.colliderect(OPPONENT):
        ball_speed_x *= -1

# Player animation
def player_animation():
    PLAYER.y += player_speed
    if PLAYER.top <= 0:
        PLAYER.top = 0
    if PLAYER.bottom >= SCREEN_HEIGHT:
        PLAYER.bottom = SCREEN_HEIGHT

# Opponent animation
def opponent_animation():
    if OPPONENT.top < BALL.y:
        OPPONENT.top += opponent_speed
    if OPPONENT.bottom > BALL.y:
        OPPONENT.bottom -= opponent_speed
    if OPPONENT.top <= 0:
        OPPONENT.top = 0
    if OPPONENT.bottom >= SCREEN_HEIGHT:
        OPPONENT.bottom = SCREEN_HEIGHT
    
# Restart ball position
def ball_restart():
    global ball_speed_x, ball_speed_y, score_timer
    current_time = pygame.time.get_ticks()
    BALL.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    if current_time - score_timer < 2100:
        # print("if currnt score")
        ball_speed_x, ball_speed_y = 0, 0
    else:
        # print("else currnt score")
        ball_speed_y = 7 * random.choice((1, -1))
        ball_speed_x = 7 * random.choice((1, -1))
        score_timer = None
        

# Colors
BG_COLOR = pygame.Color("black")
COLOR = (220, 220, 220)

# General setup
pygame.init()
clock = pygame.time.Clock()


# Setting up the main window
SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768
# SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
SCREEN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Pong Game!")


# Game Rectangles
BALL = pygame.Rect(SCREEN_WIDTH/2 -15, SCREEN_HEIGHT/2 -15, 30, 30)
PLAYER = pygame.Rect(SCREEN_WIDTH-20, SCREEN_HEIGHT/2-70, 10, 140)
OPPONENT = pygame.Rect(10, SCREEN_HEIGHT/2-70, 10, 140)
# Draw the rectangles to the screen =>   pygame.draw(surface, color, red)


# Speed variables
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7


# Text variables
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 20)


# Score timer
score_timer = None

sleep(1)
# Game loop
while True:
    # Handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            # Quit by pressing ESC
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        
        # Button pressed
        if event.type == pygame.KEYDOWN:
            # Down
            if event.key == pygame.K_DOWN:
                player_speed += 7
            # Up
            if event.key == pygame.K_UP:
                player_speed -= 7

        # Button released
        if event.type == pygame.KEYUP:
            # Down
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            # Up
            if event.key == pygame.K_UP:
                player_speed += 7
                
    
    ball_animation()
    player_animation()
    opponent_animation()
    
    
    # Visuals
    SCREEN.fill(BG_COLOR)
    pygame.draw.rect(SCREEN, COLOR, PLAYER)
    pygame.draw.rect(SCREEN, COLOR, OPPONENT)
    pygame.draw.ellipse(SCREEN, COLOR, BALL)
    pygame.draw.aaline(SCREEN, COLOR, (SCREEN_WIDTH/2, 0), (SCREEN_WIDTH/2, SCREEN_HEIGHT))

    # Ball restart
    if score_timer:
        ball_restart()
    
    
    # Surface text
    player_text = game_font.render(f"{player_score}", False, COLOR)
    opponent_text = game_font.render(f"{opponent_score}", False, COLOR)
    # Putting surface text on the main window
    SCREEN.blit(player_text, (707, SCREEN_HEIGHT/2 - 5)) 
    SCREEN.blit(opponent_text, (650, SCREEN_HEIGHT/2 - 5))
            
            
    # Updating the game window
    pygame.display.flip()
    clock.tick(60) # FPS = 60


import pkg_resources.py2_warn

















