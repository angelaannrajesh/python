import pygame
import random
import math
from pygame import mixer
# to initialize python module we write init
pygame.init()
# making screen
screen = pygame.display.set_mode((800,600))
bg = pygame.image.load("spaceship_imgs/background.png")
mixer.music.load("spaceship_imgs/background.wav")
mixer.music.play(-1)
pygame.display.set_caption("Space Game")
icon = pygame.image.load("spaceship_imgs/spaceimg.png")
pygame.display.set_icon(icon)
playerimage = pygame.image.load("spaceship_imgs/player.png")
playerx = 500
playery = 500
playerxchange = 0
def player(x,y):
    screen.blit(playerimage,(x,y))
enemyimage=[]
enemyx=[]
enemyy=[]
enemyxchange=[]
enemyychange=[]
numenemies=4
for i in range(numenemies):
    enemyimage.append(pygame.image.load("spaceship_imgs/enemy.png"))
    enemyx.append(random.randint(0,750))
    enemyy.append(random.randint(50,150))
    enemyxchange.append(4)
    enemyychange.append(40)
def enemy(x,y,i):
    screen.blit(enemyimage[i],(x,y))
    
    
    
    
# making multiple enemies
# enemyimage = []
# enemyx = []
# enemyy = []
# enemyxchange = []
# enemyychange = []
# numenemies = 5
# for i in range(numenemies):
#     enemyimage.append(pygame.image.load("spaceship_imgs/enemy.png")) 
#     enemyx = random.randint(0,800)
#     enemyy = random.randint(50,100)
bulletimage = pygame.image.load("spaceship_imgs/bullet.png")
bulletx = 0
bullety = 500
bulletxchange = 0
bulletychange = 10
bulletstate = "ready"
score = 0
font = pygame.font.Font("freesansbold.ttf",30)
scorex = 10
scorey = 10
def showscore(x,y):
    myscore = font.render("score : " + str(score),True,(255,255,255))
    screen.blit(myscore,(x,y))
    
def bullet(x,y):
    global bulletstate
    bulletstate = "fire"
    screen.blit(bulletimage,(x+15,y+10))
    
def collision(enemyx,enemyy,bulletx,bullety):
    #d=√((x2 – x1)² + (y2 – y1)²)
    distance = math.sqrt(math.pow(enemyx-bulletx,2)+(math.pow(enemyy-bullety,2)))
    if distance<25:
        return True
    else:
        return False
gameoverfont = pygame.font.Font("freesansbold.ttf",100)
def gameoverfont1():
    overtext = gameoverfont.render("GAME OVER",True,(255,255,255))
    screen.blit(overtext,(110,250))
    
# def enemy(x,y,i):
#     screen.blit(enemyimage[i],(x,y))
running = True

while running: 
    screen.fill((27,34,129))
    screen.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerxchange = -1
            if event.key == pygame.K_RIGHT:
                playerxchange = 1
                
            if event.key == pygame.K_SPACE:
                if bulletstate == "ready":
                    bulletsound=mixer.Sound("spaceship_imgs/laser.wav")
                    bulletsound.play()
                    bulletx = playerx
                    bullet(bulletx,bullety)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerxchange = 0
            
                  
    playerx += playerxchange
    if playerx <= 0 :
        playerx = 0
    elif playerx >= 730:
        playerx = 730
    for i in range(numenemies):
        if enemyy[i]>440:
            for j in range(numenemies):
                enemyy[j]=2000
            gameoverfont1()
            break
        enemyx[i]+=enemyxchange[i]
        if enemyx[i]<=0:
            enemyxchange[i]=4
            enemyy[i]+=enemyychange[i]
        elif enemyx[i]>750:
            enemyxchange[i] = -4
            enemyy[i]+=enemyychange[i]
        mycollision=collision(enemyx[i],enemyy[i],bulletx,bullety)
        if mycollision :
            explosionsound = mixer.Sound("spaceship_imgs/explosion.wav")
            explosionsound.play()
            bullety = 500
            bulletstate = "ready"
            score += 1
            enemyx[i]=random.randint(0,750)
            enemyy[i]=random.randint(50,150)
        enemy(enemyx[i],enemyy[i],i)
            
        
            
                
    
        
    # for i in range(numenemies):
    #     if enemyy[i]>450:
    #         for j in range(numenemies):
    #             enemy[j] = 2000
    #         break
    #     enemyx[i]+=enemyxchange[i]
    #     if enemyx[i]<= 0:
    #         enemyxchange[i]=4
    #         enemyy[i]= enemyychange[i]
    #     elif enemyx[i] >= 750:
    #         enemyxchange[i]=-4
    #         enemyy[i] += enemyychange[i]
    #     enemy(enemyx[i],enemyy[i],i)
    
            
            
                
    if bullety <= 0:
        
        bullety = 480
        bulletstate = "ready"
        
    if bulletstate == "fire":
        bullet(bulletx,bullety)
        bullety -= bulletychange
         
                
            
    player(playerx,playery)
    showscore(scorex,scorey)
    pygame.display.update()

    



