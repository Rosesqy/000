# -*- coding: UTF-8 -*-

import pygame
import random

pygame.init()
screen=pygame.display.set_mode([700,600])
pygame.display.set_caption("PONG")

ballPic=pygame.image.load("ball.png")
padPic=pygame.image.load('WechatIMG2.png')
bgPic=pygame.image.load('WechatIMG10.jpeg')
firstScene=pygame.image.load('begin.png')

hitWallSound=pygame.mixer.Sound("hitWall.wav")
hitPadSound=pygame.mixer.Sound('hitPaddle-old1.wav')
liveLoss=pygame.mixer.Sound('lifeLoss.wav')
gameOverSound=pygame.mixer.Sound('gameOver.wav')

keepGoing=True
capital=False

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
state=0
name=''
scoreRecord=[]
rank=0

font=pygame.font.SysFont("Times",24)

timer=pygame.time.Clock()

def binarySearch(myList,item):
    low=0
    high=len(myList)-1
    
    while low<=high:
        mid=(low+high)/2
        if myList[mid]<item:
            high=mid-1
        elif myList[mid]>item:
            low=mid+1
        else: #when myList[mid]=item
            return mid
    return -1

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

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE and state==0:
                state=1
            if state==1:
                if event.key==pygame.K_RSHIFT:
                    capital=True
                    
                if event.key>=48 and event.key<=122:
                    if capital==False:
                        name+=chr(event.key) #The chr() function returns a character from the specified ASCII value.
                    else:
                        name+=chr(event.key-32) #capitalized
                if event.key==pygame.K_BACKSPACE:
                    name=name[:-1]
                if event.key==pygame.K_RETURN:
                    state=2
                
            if event.key==pygame.K_F1 and state==3:
                state=0
                live=5
                points=0
                speedX=0
                speedY=0
                bounceCounter=0
                name=''
                rank=0
                ballStartMove=False
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_RSHIFT:
                    capital=False

    if state==0:
        firstScene=pygame.transform.scale(firstScene,(700,600))
        screen.blit(firstScene,(0,0))
        draw_string='Press space to start'
        text=font.render(draw_string,True,WHITE)
        text_rect=text.get_rect()
        text_rect.centerx=screen.get_rect().centerx
        text_rect.y=500
        screen.blit(text,text_rect)

    elif state==1:
        screen.fill(BLACK)
        draw_string='Please enter your name:'+name
        text=font.render(draw_string,True,WHITE)
        text_rect=text.get_rect()
        text_rect.centerx=screen.get_rect().centerx
        text_rect.y=300
        screen.blit(text,text_rect)

    elif state==2:


        ballx+=speedX
        bally+=speedY

        if ballStartMove: #if it is false, dont run the following; vice versa
            if ballx<=ballRad or ballx>=700-ballRad:
                speedX=-speedX
                hitWallSound.play()
            if bally<=ballRad:
                speedY=-speedY
                hitWallSound.play()
            if bally>=600:
                ballStartMove=False #return to the pad
                lives-=1
                ballx=padx+padw/2
                bally=pady-ballRad
                speedX=0
                speedY=0
                points=0
                bouncecounter=0
                liveLoss.play()
                if lives==0:
                    gameOverSound.play()


        if bally+ballRad>=pady and bally+ballRad<=pady+padh and speedY>0: ##difficult
            if ballx >=padx and ballx <=padx+padw:
                speedY=-speedY
                points+=1
                bouncecounter+=1
                hitPadSound.play()
        if bouncecounter>=10:
            if speedX<=0:
                speedX-=1
            else:
                speedX+=1
            speedY-=10
            bouncecounter=0

        screen.fill(BLACK)
        screen.blit(bgPic,(0,0))

        #draw the pad
        padx=pygame.mouse.get_pos()[0] #get the position of mouse through pygame, ignore the y value because pad here just move left and right, 0 refers to x which is the first value of the postion of mouse
        padx-=padw/2
    ##    pygame.draw.rect(screen,WHITE,(padx,pady,padw,padh))
    ##    padPic=pygame.transform.scale(padPic,((padx,pady)))
        screen.blit(padPic,(padx,pady,padw,padh))

        #draw the ball
        if ballStartMove==False:
            ballx=padx+padw/2
    ##    pygame.draw.circle(screen,WHITE,(int(ballx),int(bally)),ballRad)
        ballPic=pygame.transform.scale(ballPic,(ballRad*2,ballRad*2))
        screen.blit(ballPic,(int(ballx-ballRad),int(bally-ballRad)))

        draw_string="Lives:"+str(lives)+"||"+"Points"+str(points) #+"||"+"bouncecounter"+str(bouncecounter) #str:change number into string
        text=font.render(draw_string,True,WHITE)
        text_rect=text.get_rect()
        text_rect.centerx=screen.get_rect().centerx
        text_rect.y=100
        screen.blit(text,text_rect)

#gameover
        if lives<=0:
            state=3
            screen.fill(BLACK)
            scoreRecord.append(points)
            if len(scoreRecord)>1:
                for i in range(len(scoreRecord)-1):
                    for j in range(len(scoreRecord)-i-1):
                        if scoreRecord[j]<scoreRecord[j+1]:
                            temp=scoreRecord[j]
                            scoreRecord[j]=scoreRecord[j+1]
                            scoreRecord[j+1]=temp
            rank=binarySearch(scoreRecord,points)+1
    
    elif state==3:
            draw_string="GameOver"+'name'+str(name)+"||"+"points"+str(points)+"||"+"rank"+str(rank)
            text=font.render(draw_string,True,WHITE)
            text_rect=text.get_rect()
            text_rect.centerx=screen.get_rect().centerx
            text_rect.y=300
            screen.blit(text,text_rect)
    

    pygame.display.update()
    timer.tick(60)
pygame.quit()
