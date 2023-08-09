import pygame
from pygame.locals import *
# to start a pygame:
pygame.init()
clock = pygame.time.Clock()
fps = 60
screenwidth = 1000
screenheight = 640
screen = pygame.display.set_mode((screenwidth,screenheight))
tilesize = 50
gameover = 0

pygame.display.set_caption("Mario Platformer Game") 
# loading images
sun_image = pygame.image.load("mario_images/sun.png")
bg_image = pygame.image.load("mario_images/sky.png")
restartimage = pygame.image.load("mario_images/restart_btn.png")
class Button():
    def __init__(self,x,y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self):
        screen.blit(self.image,self.rect)
def drawgrid():
    for line in range(0,):
        pygame.draw.line(screen,(255,255,255),(0,line*tilesize),(screenwidth,line*tilesize))
        pygame.draw.line(screen,(255,255,255),(line*tilesize,0),(line*tilesize,screenheight))
# self is everything you make in class       
class Player():
    def __init__(self,x,y):
        self.images_right=[]
        self.images_left=[]
        
        self.index = 0
        self.counter = 0
        for num in range(1 ,5):
            imgright = pygame.image.load(f"mario_images/guy{num}.png")
            imgright = pygame.transform.scale(imgright,(40,80))
            imgleft = pygame.transform.flip(imgright,True,False)
            self.images_right.append(imgright)
            self.images_left.append(imgleft)
        self.deadimage= pygame.image.load("mario_images/ghost.png")
            
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vely = 0
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.jump = False
        self.direction = 0
        
        dx = 0
        dy = 0
        walkcooldown = 20
        if gameover == 0:
            
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] and self.jump == False:
                self.vely = -15
                self.jump = True
            if key[pygame.K_SPACE] == False:
                
                self.jump = False
            if key[pygame.K_LEFT]:
                dx -= 5
                self.counter += 1
                self.direction = -1
            if key[pygame.K_RIGHT] :
                dx += 5  
                self.counter += 1
                self.direction = +1
            if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
                self.counter = 0
                self.index = 0
                self.image = self.images_right[self.index]
            #handling animation
            self.counter += 1
            if self.counter > walkcooldown:
                self.counter = 0
                self.index+=1
                if self.index >= len(self.images_right):
                    self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]
            # adding gravity
            self.vely += 1
            if self.vely > 10:
                self.vely = 10
            dy+=self.vely
            # checking for collision
            for tile in world.tilelist:
                if tile[1].colliderect(self.rect.x+dx,self.rect.y,self.width,self.height):
                    dx = 0
                if tile[1].colliderect(self.rect.x,self.rect.y+dy,self.width,self.height):
                    if self.vely<0:
                        dy = tile[1].bottom-self.rect.top
                        self.vely = 0
                    elif self.vely>= 0:
                        dy = tile[1].top-self.rect.bottom
                        self.vely = 0
            
            if pygame.sprite.spritecollide(self,blob_group,False):
                gameover = -1
            if pygame.sprite.spritecollide(self,lava_group,False):
                gameover = -1
            
            # updating player cordinates
            
            self.rect.x += dx
            self.rect.y += dy
            if self.rect.bottom > screenheight:
                self.rect.bottom = screenheight
                dy = 0
        elif gameover == -1:
            self.image = self.deadimage
            self.rect.y-= 5
            
        
        screen.blit(self.image,self.rect)
        pygame.draw.rect(screen,(255,255,255),self.rect,2)
        return gameover
        
class World():
    def __init__(self,data):
        self.tilelist=[]
        #append = adding something into the list
        # loading images
        drtimage = pygame.image.load("mario_images/dirt.png")
        grassimage= pygame.image.load("mario_images/grass.png")
        rowcount = 0
        
        for row in data:
            colomncount = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(drtimage,(tilesize,tilesize))
                    imgrect = img.get_rect()
                    # x is always colomn
                    imgrect.x = colomncount*tilesize
                    imgrect.y = rowcount*tilesize
                    tile=(img,imgrect)
                    self.tilelist.append(tile)
                    
                if tile == 2:
                    img = pygame.transform.scale(grassimage,(tilesize,tilesize))
                    imgrect = img.get_rect()
                    # x is always colomn
                    imgrect.x = colomncount*tilesize
                    imgrect.y = rowcount*tilesize
                    tile=(img,imgrect)
                    self.tilelist.append(tile)
                if tile == 3:
                    blob = Enemy(colomncount*tilesize,rowcount*tilesize+15)
                    blob_group.add(blob)
                if tile == 6:
                    lava = Lava(colomncount*tilesize,rowcount*tilesize+(tilesize//2))
                    lava_group.add(lava)
                    
                colomncount+=1
            rowcount+=1
    def draw(self):    
      for tile in self.tilelist:
          screen.blit(tile[0],tile[1])
          pygame.draw.rect(screen,(255,255,255),tile[1],2)  
class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("mario_images/blob.png")
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0
    def update(self):
        self.rect.x += self.move_direction
        self.move_counter+=1
        if self.move_counter > 50:
            self.move_direction*=-1
            self.move_counter = 0
class Lava(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load("mario_images/lava.png")
        self.image = pygame.transform.scale(img,(tilesize,tilesize))
        self.rect=self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0
                  
worlddata=[
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 1], 
 
[1, 7, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2,2 , 1], 
[1, 2, 0, 0, 0, 0, 0, 2,2, 0, 0, 0, 0, 0, 0, 0, 0, 0,  0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0, 7, 0, 0, 0, 0, 1], 
[1, 0, 2, 0, 0, 7, 0, 7, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 1], 
[1, 0, 0, 2, 0, 0, 4, 0, 0, 0, 0, 3, 0, 0, 3, 0, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 1], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 2, 2, 2, 2, 1], 
[1, 0, 0, 0, 0, 0, 2, 2, 2, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1],
 
[1, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
[1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]
# 0 is a blank space where you can also see the sky, 1 is a drt image, 2 is a drt with grass image, 6 is lava.   
player = Player(100,screenheight - 130)
blob_group=pygame.sprite.Group()
lava_group = pygame.sprite.Group()
world = World(worlddata)
restartbutton = Button(screenwidth//2,screenheight//2,restartimage)
run = True

while run:
    # blit is used to draw images on screen
    clock.tick(fps)
    screen.blit(bg_image,(0,0))
    screen.blit(sun_image,(80,80))
    world.draw()
    if gameover == 0:
        blob_group.update()
    blob_group.draw(screen)
    lava_group.draw(screen)
    gameover = player.update(gameover)
    if gameover == -1:
        restartbutton.draw()
        
    player.update(gameover)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    drawgrid()  
    
    
        # for refreshing the screen, we use update command
    pygame.display.update()
    
pygame.quit()
