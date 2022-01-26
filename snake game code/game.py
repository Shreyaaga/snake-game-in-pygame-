import pygame
import random
pygame.init()

#creating window
screen_width=500
screen_length=500
gamewindow=pygame.display.set_mode((screen_length,screen_width))

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
pink=(255,182,193)

#game title
title=pygame.display.set_caption("Snake game")
pygame.display.update()

#game specific variables
exit_game=False
game_over=False
snake_x=45
snake_y=55
snake_size=10
fps=60
vel_x=0
vel_y=0
food_x=random.randint(0,screen_width/2)
food_y=random.randint(0,screen_length/2)
score=0
clock=pygame.time.Clock()
snk_list = []
snk_length = 1
#To display score
font = pygame.font.SysFont(None, 55)
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x,y])
#To increase snake size
def plot_snake(gamewindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gamewindow, color, [x, y, snake_size, snake_size])

pygame.draw.rect(gamewindow,red,[food_x,food_y,snake_size,snake_size])
pygame.display.update()
#welcome page 
def welcome():
  exit_game=False
  while not exit_game:
    gamewindow.fill(pink)
    text_screen("Press spacebar to play",white,50,100)

    pygame.display.update()
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        exit_game=True
      elif event.type==pygame.KEYDOWN:
        if event.key==pygame.K_SPACE:
          gameloop()

#game loop
def gameloop():
    exit_game=False
    game_over=False
    snake_x=45
    snake_y=55
    snake_size=10
    fps=60
    vel_x=0
    vel_y=0
    food_x=random.randint(0,screen_width/2)
    food_y=random.randint(0,screen_length/2)
    score=0
    clock=pygame.time.Clock()
    snk_list = []
    snk_length = 1
    while not exit_game:
      if game_over:
        gamewindow.fill(white)
        text_screen("Game over !! Try again!!",red,75,130)
        text_screen("Your Score-"+ str(score),black,80,190)
      else:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    vel_y=-2
                    vel_x=0

                if event.key==pygame.K_DOWN:
                    vel_y=2
                    vel_x=0
                if event.key==pygame.K_RIGHT:
                    vel_x=2
                    vel_y=0
                if event.key==pygame.K_LEFT:
                    vel_x=-2
                    vel_y=0
        snake_x=snake_x+vel_x
        snake_y=snake_y+vel_y
        if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
            score=score+10
            food_x=random.randint(0,screen_width/2)
            food_y=random.randint(0,screen_length/2)
            snk_length += 5
            f=open("highscore.txt","r")
            hs=int(f.read())
            if hs<score:
                f=open("highscore.txt","w")
                f.write(str(score))
            f.close()

            food_x=random.randint(0,screen_width/2)
            food_y=random.randint(0,screen_length/2)
            snk_length += 5

        gamewindow.fill(white)
        text_screen("Score: " + str(score), red, 5, 5)
        pygame.display.update()
        pygame.draw.rect(gamewindow,red,[food_x,food_y,snake_size,snake_size])
        pygame.display.update()
        pygame.draw.rect(gamewindow,black,[snake_x,snake_y,snake_size,snake_size])
        pygame.display.update()

        head = []
        head.append(snake_x)
        head.append(snake_y)
        snk_list.append(head)

        if len(snk_list)>snk_length:
            del snk_list[0]
        if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_length:
          game_over=True
          
        plot_snake(gamewindow, black, snk_list, snake_size)
      pygame.display.update()
      clock.tick(fps)







welcome()
pygame.quit()
quit()
