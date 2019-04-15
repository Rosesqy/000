import pygame
import random

pygame.init()
screen=pygame.display.set_mode([700,600])
pygame.display.set_caption("PONG")

keepGoing=True

BLACK=(0,0,0)
WHITE=(255,255,255)

padx=300
pady=550
padw=200
padh=25

ballRad=25
ballx=padx+padw/2
bally=pady-ballRad
speedX=0
speedY=0
ballStartMove=False #this is a flag, like a control

points=0
lives=5
bouncecounter=0

font=pygame.font.SysFont("Times",24)

timer=pygame.time.Clock()

while keepGoing:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            keepGoing=False
        if event.type==pygame.MOUSEBUTTONDOWN:
            if ballStartMove==False:
                ballStartMove=True
                speedY=random.randint(-8,-6)
                while speedX==0: #prevent speedX==0, another way: speedX=random.randint(2,5)*(random.randint(0,1)*2-1)
                    speedX=random.randint(-15,15)
    ballx+=speedX
    bally+=speedY

    
    if ballStartMove: #if it is false, dont run the following; vice versa
        if ballx<=ballRad or ballx>=700-ballRad:
            speedX=-speedX
        if bally<=ballRad:
            speedY=-speedY
        if bally>=600:
            ballStartMove=False #return to the pad
            lives-=1
            ballx=padx+padw/2
            bally=pady-ballRad
            speedX=0
            speedY=0
            
    if bally+ballRad>=pady and bally+ballRad<=pady+padh and speedY>0: ##difficult
        if ballx >=padx and ballx <=padx+padw:
            speedY=-speedY
            points+=1
            bouncecounter+=1
    if bouncecounter>=10:
        if speedX<=0:
            speedX-=1
        else:
            speedX+=1
        speedY-=10
        bouncecounter=0
    
    screen.fill(BLACK)
    #draw the pad
    padx=pygame.mouse.get_pos()[0] #get the position of mouse through pygame, ignore the y value because pad here just move left and right, 0 refers to x which is the first value of the postion of mouse
    padx-=padw/2
    pygame.draw.rect(screen,WHITE,(padx,pady,padw,padh))

    #draw the ball
    if ballStartMove==False:
        ballX=padx+padw/2
    pygame.draw.circle(screen,WHITE,(int(ballx),int(bally)),ballRad)
    
    draw_string="Lives:"+str(lives)+"||"+"Points"+str(points)+"||"+"bouncecounter"+str(bouncecounter) #str:change number into string
    text=font.render(draw_string,True,WHITE)
    text_rect=text.get_rect()
    text_rect.centerx=screen.get_rect().centerx
    text_rect.y=100
    screen.blit(text,text_rect)
    
    pygame.display.update()
    timer.tick(60)
pygame.quit()
