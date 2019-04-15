import pygame
import random
from pygame.locals import*

pygame.init()
screen=pygame.display.set_mode([800,800])
pygame.display.set_caption('Adventure in Space')
keepGoing=True
rocMove=False

rocPic=pygame.image.load('rocket.png')
astPic=pygame.image.load('asteroid.png')
cryPic=pygame.image.load('crystal.png')
bgPic1=pygame.image.load('space1.jpg')
bgPic2=pygame.image.load('space2.jpg')
firstScene=pygame.image.load('start.jpg')

hitAstSound=pygame.mixer.Sound('8923.wav')
hitCrySound=pygame.mixer.Sound('8407.wav')
gameOverSound=pygame.mixer.Sound('gameOver.wav')
bgM=pygame.mixer.Sound('df.wav')

ROCW=40
ROCH=80
ASTSIZE=150
CRYSIZE=50

posy1=0
posy2=-1600

BLACK=(0,0,0)
WHITE=(255,255,255)

lives=3
points=0
state=0
clock=pygame.time.Clock()

font=pygame.font.SysFont("Times",24)
font2=pygame.font.Font("Felt-tipPen.otf",50)
font3=pygame.font.Font("Bubblegum.ttf",80)
font4=pygame.font.Font("Blobtastics.ttf",30)


rocPic=pygame.transform.scale(rocPic,(ROCW,ROCH))
astPic=pygame.transform.scale(astPic,(ASTSIZE,ASTSIZE))
cryPic=pygame.transform.scale(cryPic,(CRYSIZE,CRYSIZE))
bgPic1=pygame.transform.scale(bgPic1,(800,1600))
bgPic2=pygame.transform.scale(bgPic2,(800,1600))
firstScene=pygame.transform.scale(firstScene,(800,800))

class Roc:
    def __init__ (self,rocPic,size,posx=random.randint(0,(800-ROCW)/ROCW)*ROCW,posy=random.randint(0,(800-ROCH)/ROCH)*ROCH):
        self.size=size
        self.posx=400
        self.posy=700
        self.speedx = 0
        self.speedy=0
        self.img=rocPic
        
    def draw(self,screen):
        self.posx += self.speedx
        self.posy=400 #+= self.speedy
        screen.blit(self.img,(self.posx,self.posy))
        
    def randomPos(self):
        self.posx=random.randint(0,(800-ROCW)/ROCW)*ROCW
        self.posy=random.randint(0,(800-ROCH)/ROCH)*ROCH-speedy

class Ast:
    def __init__ (self,astPic,size):
        self.size=size
        self.posx=random.randint(0,800)
        self.posy=random.randint(-1600,1600)
        self.speedx=0
        self.speedy=random.randint(10,15)
        while collide(roc.posx,self.posx,roc.posy,self.posy,ROCW,ASTSIZE,ROCH,ASTSIZE):
            self.posx=random.randint(0,800)
            self.posy=random.randint(-1600,100)
        self.img=astPic

    def draw(self,screen):
        self.posx += self.speedx
        self.posy += self.speedy
        screen.blit(self.img,(self.posx,self.posy))
        
   
class Cry:
    def __init__ (self,cryPic,size):
        self.size=size
        self.posx=random.randint(0,800)
        self.posy=random.randint(-1600,100)
        self.speedx=0
        self.speedy=random.randint(10,15)
        self.img=cryPic
        self.collided = False

    def draw(self,screen):
        self.posx += self.speedx
        self.posy += self.speedy
        screen.blit(self.img,(self.posx,self.posy))
 
  

##def die(data):
##    screen.fill(WHITE)
##    f=pygame.font.SysFont('Marker Felt',40)
##    t=f.render('Your score is:'+data,True,BLACK)
##    screen.blit(t,(10,270))
##    pygame.display.update()
##    pygame.time.wait(2000) 
##    state=0 

def collide(x1,x2,y1,y2,w1,w2,h1,h2):
    if x1 + w1 > x2 and x1 < x2 + w2 and y1 + h1 > y2 and y1 < y2 + h2: #right,left,down,up
        return True
    else:
        return False

roc=Roc(rocPic,(ROCW,ROCH))
ast=Ast(astPic,(ASTSIZE,ASTSIZE))
astList=[]
for i in range(15):
    astList.append(Ast(astPic,(ASTSIZE,ASTSIZE)))
cry=Cry(cryPic,(CRYSIZE,CRYSIZE))
cryList=[]
for i in range(10):
    cryList.append(Cry(cryPic,(CRYSIZE,CRYSIZE)))

    
while keepGoing:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type==QUIT:
            keepGoing=False
        if event.type==KEYDOWN:
            if event.key==pygame.K_SPACE and state==0:
                state=1
                bgM.play()

            if state==1:
                if event.key==K_RIGHT:
                    roc.speedx+=10
                elif event.key==K_LEFT:
                    roc.speedx-=10
            if event.key==K_F1 and state==2:
                state=0
                points=0
                lives=3
                roc.speedx=0
                roc.speedy=0
                roc.posx=400
                roc.posy=700

                ast=Ast(astPic,(ASTSIZE,ASTSIZE))
                astList=[]
                for i in range(15):
                    astList.append(Ast(astPic,(ASTSIZE,ASTSIZE)))
                cry=Cry(cryPic,(CRYSIZE,CRYSIZE))
                cryList=[]
                for i in range(10):
                    cryList.append(Cry(cryPic,(CRYSIZE,CRYSIZE)))
##                ast.speedx=0
##                ast.speedy=random.randint(8,14)
##                ast.posx=random.randint(0,800)
##                ast.posy=random.randint(-1600,1600)
##                cry.speedx=0
##                cry.speedy=random.randint(8,14)
        if event.type==KEYUP:
            roc.speedx=0
            

    if state==0:
        screen.blit(firstScene,(0,0))

        draw_string='ADVENTURE IN SPACE'
        text=font3.render(draw_string,True,BLACK)
        text_rect=text.get_rect()
        text_rect.x=28
        text_rect.y=398
        screen.blit(text,text_rect)
        draw_string='ADVENTURE IN SPACE'
        text=font3.render(draw_string,True,WHITE)
        text_rect=text.get_rect()
        text_rect.centerx=screen.get_rect().centerx
        text_rect.y=400
        screen.blit(text,text_rect)
        
        draw_string='Press space to start'
        text=font2.render(draw_string,True,WHITE)
        text_rect=text.get_rect()
        text_rect.centerx=screen.get_rect().centerx
        text_rect.y=500
        screen.blit(text,text_rect)

    elif state==1:
        
    #collide with crystal
        for i in range(len(cryList)):
            if collide(roc.posx,cryList[i].posx,roc.posy,cryList[i].posy,ROCW,CRYSIZE,ROCH,CRYSIZE):
                points+=1
                cryList[i].collided=True
                hitCrySound.play()
            
        #collide with asteroid
        for i in range(len(astList)):
            if collide(roc.posx,astList[i].posx,roc.posy,astList[i].posy,ROCW,ASTSIZE,ROCH,ASTSIZE):
                lives-=1
                roc.posx=400
                roc.posy=700
                roc.speedx = 0
                roc.speedy=random.randint(-7,-5)
                hitAstSound.play()
    ##            astList[i].posx=random.randint(0,800)
    ##            astList[i].posy=random.randint(0,800)
    ##            astList[i].speedx=0
    ##            astList[i].speedy=random.randint(1,5)
    ##            cryList[i].posx=random.randint(0,800)
    ##            cryList[i].posy=random.randint(0,800)
    ##            cryList[i].speedx=0
    ##            cryList[i].speedy=random.randint(1,5)
                if lives<=0:
                    state=2
                    gameOverSound.play()
##                    die(str(points))
        screen.fill(BLACK)
        posy1+=20
        posy2+=20
        if posy1>=1600:
            posy1=-1600
        if posy2>=1600:
            posy2=-1600
        screen.blit(bgPic1,(0,posy1))
        screen.blit(bgPic2,(0,posy2))
        

        draw_string="Lives:"+str(lives) 
        text=font4.render(draw_string,True,WHITE)
        text_rect=text.get_rect()
        text_rect.x=0
        text_rect.y=0
        screen.blit(text,text_rect)

        draw_string="Points:"+str(points) 
        text=font4.render(draw_string,True,WHITE)
        text_rect=text.get_rect()
        text_rect.x=600
        text_rect.y=0
        screen.blit(text,text_rect)

        roc.draw(screen)
        
        for i in range(len(astList)):
            if astList[i].posy >= 800:
                astList[i].posy = random.randint(-1600,-800)
        for i in range(len(cryList)):
            if cryList[i].posy>=800:
                cryList[i].posy=random.randint(-1600,-800)
        
        i = 0
        while i < len(cryList):
            if cryList[i].collided == True:
                cryList.pop(i)
    ##            print len(cryList)
            i += 1
        for i in range(len(astList)):
            astList[i].draw(screen)
        for i in range(len(cryList)):
            cryList[i].draw(screen)
#gameover
    elif state==2:
        bgM.stop()
        draw_string='GameOver'
        text=font2.render(draw_string,True,WHITE)
        text_rect=text.get_rect()
        text_rect.centerx=screen.get_rect().centerx
        text_rect.y=300
        screen.blit(text,text_rect)
        
        
        draw_string="Your points is:"+str(points)
        text=font2.render(draw_string,True,WHITE)
        text_rect=text.get_rect()
        text_rect.centerx=screen.get_rect().centerx
        text_rect.y=500
        screen.blit(text,text_rect) 
    
    pygame.display.update()
pygame.quit()
