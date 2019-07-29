import random

import pygame
import cx_Freeze

pygame.init()

display_width = 800
display_height = 600

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)
purple = (128, 0, 128)


gameScreen = pygame.display.set_mode((display_width,display_height))

gameClose = False


lead_x_change = 0
lead_y_change = 0
size_of_block = 20
clock = pygame.time.Clock()
FPS = 30
direction = "right"

font = pygame.font.SysFont(None, 25)
smallFont = pygame.font.SysFont("Comicsansms", 25)
medFont = pygame.font.SysFont("Comicsansms", 50)
largeFont = pygame.font.SysFont("Comicsansms", 80)

pygame.display.set_caption("snek")
icon = pygame.image.load("./apple.png")
pygame.display.set_icon(icon)

img = pygame.image.load('./snekhead.png')
appleimg = pygame.image.load('./apple.png')

def game_intro():
    intro = True
    while True:
        gameScreen.fill(white)
        message_to_screen("Welcome", purple, -100, size="large")
        message_to_screen("To the 90's", black, -30, size="medium")
        message_to_screen("We played this four hours", black, 10, size="medium")
        message_to_screen("If you run into yourself or the edge, you'll die", black, 50, size="small")
        message_to_screen("Press Space to Play and Q to quite", black, 70, size="small")
        pygame.display.update()
        clock.tick(15)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = False
                    gameLoop()
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

def text_objects(text, color, size):
    if size == "small":
        textSurface = smallFont.render(text, True, color)
    elif size == "medium":
        textSurface = medFont.render(text, True, color)
    elif size == "large":
        textSurface = largeFont.render(text, True, color)

    return textSurface, textSurface.get_rect()


def message_to_screen(msg, color, y_displace = 0, size = "small"):
    textSurf, textRect = text_objects(msg, color, size)
    # screen_text = font.render(msg, True, color)
    # gameDisplay.blit(screen_text, [display_width/2, display_height/2])

    textRect.center = (display_width / 2), (display_height / 2) + y_displace
    gameScreen.blit(textSurf, textRect)

def snake(size_of_block, snakelist):
    if direction == "right":
        head = img
    if direction == "left":
        head = pygame.transform.rotate(img, 180)
    if direction == "up":
        head = pygame.transform.rotate(img, 90)
    if direction == "down":
        head = pygame.transform.rotate(img, 270)
    gameScreen.blit(img,(snakelist[-1][0],snakelist[-1][1]))

    for XY in snakelist[:-1]:
        pygame.draw.rect(gameScreen, green, [XY[0],XY[1],size_of_block,size_of_block])



def gameLoop():
    global direction
    gameClose = False
    gameOver = False

    lead_x_change = 10
    lead_y_change = 0
    snakeList = []
    snakeLength = 1

    randomAppleX = round(random.randrange(0,display_width-size_of_block)/20)*20
    randomAppleY = round(random.randrange(0,display_height-size_of_block)/20)*20

    lead_x = display_width / 2
    lead_y = display_height / 2

    while not gameClose:
        while gameOver == True:
            gameScreen.fill(white)
            message_to_screen("Game Over", red, -50, size="large")
            message_to_screen("Press Space to play again or Q to quit", black, 50, size="medium")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameClose = True
                        gameOver = False
                    if event.key == pygame.K_SPACE:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameClose = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -size_of_block
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = size_of_block
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -size_of_block
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = size_of_block
                    lead_x_change = 0



        if lead_x >= display_width or lead_x < size_of_block or lead_y >= display_height or lead_y < 0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameScreen.fill(white)

        pygame.draw.rect(gameScreen, white, (randomAppleX, randomAppleY, size_of_block, size_of_block))
        gameScreen.blit(appleimg, (randomAppleX, randomAppleY, size_of_block, size_of_block))

        pygame.draw.rect(gameScreen, green, (lead_x, lead_y, size_of_block, size_of_block))
        pygame.display.update()
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True

        snake(size_of_block, snakeList)
        pygame.display.update()


        if lead_x == randomAppleX and lead_y == randomAppleY:
            randomAppleX = round(random.randrange(0, display_width - size_of_block) / 20) * 20
            randomAppleY = round(random.randrange(0, display_height - size_of_block) / 20) * 20
            snakeLength += 1
        clock.tick(FPS)

    pygame.quit()

    quit()

game_intro()
gameLoop()

