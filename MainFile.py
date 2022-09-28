import pygame   
from pygame_functions import *
import random
from math import *
from pygame import mixer
pygame.init()
backgroundmusic=mixer.Sound("D:\\Project pygame\\background.wav")
backgroundmusic.play(-1)
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invader")
icon=pygame.image.load("D:\\Project pygame\\ship.png")
pygame.display.set_icon(icon)
playerIMG=pygame.image.load("D:\\Project pygame\\spaceship.png")
bulletIMG=pygame.image.load("D:\\Project pygame\\shot.png")
Lose=pygame.image.load("D:\\Project pygame\\Lose.png")
Win=pygame.image.load("D:\\Project pygame\\Win.png")
stat="main"
colx,coly,colz=255,0,255
colox , coloy , coloz=255,255,255
lx,ly,lz=255,0,255
col1 , col2 , col3=255,255,255
Playerx=370.0
Playery=480.0
Playerxchange,counter,aliencounter,score,Bulletx=0,0,0,0,0
Bullety=420
starx=300
stary,stary1=250,250
alienlist,alienxlist,alienylist,xchangelist,motion=[],[],[],[],[]
working=True
level="Medium"
state="ready"
alist=["D:\\Project pygame\\alien.png","D:\\Project pygame\\alien1.png","D:\\Project pygame\\alien2.png","D:\\Project pygame\\ufo.png","D:\\Project pygame\\falcon.png"]
alienxchange=0.3
font = pygame.font.Font('freesansbold.ttf', 32)
font1 = pygame.font.Font('freesansbold.ttf', 45)
textX = 10
textY = 10
def alienselect():
    global aliencounter,alist,alienlist,alienxlist,alienylist,xchangelist,motion
    for i in range(0,aliencounter):
        alienx=random.randint(80,720)
        alieny=random.choice([0,80,160,240])
        movemnt=random.choice([+1,-1])
        a=random.choice(alist)
        motion.append(movemnt)
        xchangelist.append(0.1)
        alienlist.append(a)
        alienxlist.append(alienx)
        alienylist.append(alieny)
    game_run()
def levels():
    global running,stary1,stat,colx,coly,colz,colox,level,colox,coloy,coloz,aliencounter,alienxchange,lx,ly,lz,col1,col2,col3,working
    level="Medium"
    Heading=font1.render("Levels",True,(100,100,100))
    screen.blit(Heading,(310,200))
    START = font.render("Easy", True,(colx , coly , colz))
    screen.blit(START, (320,250))
    opti = font.render("Medium", True,(colox , coloy , coloz))
    screen.blit(opti, (320,280))
    level = font.render("Hard", True,(col1 , col2 , col3))
    screen.blit(level, (320,310))
    star = font.render("*", True,(lx,ly,lz))
    screen.blit(star, (starx,stary1))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:                
            if event.key == pygame.K_BACKSPACE:
                stat="main"
            if event.key == pygame.K_DOWN and stary1<310:
                stary1+=30
            if event.key == pygame.K_UP and 250<stary1:
                stary1-=30
            if event.key == pygame.K_RETURN and stary1==250:
                level="Easy"
                stat="main"
            if event.key == pygame.K_RETURN and stary1==280:
                level="Medium"
                stat="main"
            if event.key == pygame.K_RETURN and stary1==310:
                level="Hard"
                stat="main"
    if level == "Easy":
        aliencounter=6
        alienxchange=0.3        
    elif level == "Medium":
        aliencounter=8
        alienxchange=0.4        
    elif level == "Hard":
        alienxchange=0.6
        aliencounter=10        
    if stary1==250:
        lx,ly,lz=255,0,255
        colx,coly,colz=255,0,255
        colox,coloy,coloz=255,255,255
        col1,col2,col3=255,255,255        
    if stary1==280:
        lx,ly,lz=0,0,128
        colox,coloy,coloz=0,0,128
        col1,col2,col3=255,255,255
        colx,coly,colz=255,255,255        
    if stary1==310:
        lx,ly,lz=0,255,255
        col1,col2,col3=0,255,255
        colox,coloy,coloz=255,255,255
        colx,coly,colz=255,255,255
def alien():
    global aliencounter,xchangelist,alienxlist,alienylist,motion
    for i in range(0,aliencounter):
        alienxlist[i]+=xchangelist[i]*motion[i]
        if alienxlist[i]>720:
            xchangelist[i]=-alienxchange
            alienylist[i]+=80
        elif alienxlist[i]<0:
            xchangelist[i]=alienxchange
            alienylist[i]+=80
            print(alienylist)
        alienIMG=pygame.image.load(alienlist[i])
        screen.blit(alienIMG,(alienxlist[i],alienylist[i]))
def shoot(x,y):
    global Bulletx,state
    state="fire"
    Bulletx = x-18
    screen.blit(bulletIMG,(x-20,y))
    fire=mixer.Sound("D:\\Project pygame\\fireInTheHole.wav")
    fire.play()
def main_menu():
    global running,stary,stat,colx,coly,colz,lx,ly,lz,col1,col2,col3,alienlist,alienxlist,alienylist,xchangelist,counter,colox,coloy,coloz
    if counter==0:
        start = font.render("Start Game", True,(colx , coly , colz))
        screen.blit(start, (320,250))
        level = font.render("Level", True,(col1 , col2 , col3))
        screen.blit(level, (320,280))
        star = font.render("*", True,(lx,ly,lz))
        screen.blit(star, (starx,stary))
        FrontLine = font1.render("Welcome To Space Invaders", True,(0 , 255 , 255))
        screen.blit(FrontLine, (100,200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and stary<280:
                    stary+=30
                if event.key == pygame.K_UP and 250<stary:
                    stary-=30
                if event.key == pygame.K_RETURN and stary==250:
                    stat="START GAME"
                    alienlist,alienxlist,alienylist,xchangelist=[],[],[],[]
                    counter+=1
                if event.key == pygame.K_RETURN and stary==280:
                    stat="LEVEL"
                if stary==250:
                    lx,ly,lz=255,0,255
                    colx,coly,colz=255,0,255
                    col1,col2,col3=255,255,255
                if stary==280:
                    lx,ly,lz=0,255,0
                    col1,col2,col3=0,255,0
                    colx,coly,colz=255,255,255
    elif counter>0:
        resume = font.render("RESUME", True,(colx,coly,colz))
        screen.blit(resume, (320,250))
        start = font.render("Start Game", True,(colox , coloy , coloz))
        screen.blit(start, (320,280))
        level = font.render("Level", True,(col1 , col2 , col3))
        screen.blit(level, (320,310))
        star = font.render("*", True,(lx,ly,lz))
        screen.blit(star, (starx,stary))
        FrontLine = font1.render("Welcome To Space Invaders", True,(0 , 255 , 255))
        screen.blit(FrontLine, (100,200))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and stary<310:
                    stary+=30
                if event.key == pygame.K_UP and 250<stary:
                    stary-=30
                if event.key == pygame.K_RETURN and stary==280:
                    stat="START GAME"
                    alienlist,alienxlist,alienylist,xchangelist=[],[],[],[]
                    counter+=1
                if event.key == pygame.K_RETURN and stary==310:
                    stat="LEVEL"
                if event.key == pygame.K_RETURN and stary==250:
                    stat="START GAME"
                if stary==250:
                    lx,ly,lz=255,0,255
                    colx,coly,colz=255,0,255
                    colox,coloy,coloz=255,255,255
                    col1,col2,col3=255,255,255        
                if stary==280:
                    lx,ly,lz=0,0,128
                    colox,coloy,coloz=0,0,128
                    col1,col2,col3=255,255,255
                    colx,coly,colz=255,255,255        
                if stary==310:
                    lx,ly,lz=0,255,0
                    col1,col2,col3=0,255,0
                    colox,coloy,coloz=255,255,255
                    colx,coly,colz=255,255,255
    if stat == "LEVEL":
        levels()
def game_run():
    global score,state,Playerx,Playery,Bulletx,Bullety,stat,Playerxchange,running,aliencounter,alist,alienlist,alienxlist,alienylist
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Playerxchange=-0.5
            if event.key == pygame.K_RIGHT:
                Playerxchange=0.5
            if event.key == pygame.K_SPACE:
                if state=="ready":
                    shoot(Playerx,Bullety)
            if event.key == pygame.K_BACKSPACE:
                stat="main"
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                Playerxchange=0
    Playerx+=Playerxchange
    if Playerx>710:
        Playerx=710        
    if Playerx<0:
        Playerx=0

    if state == "fire":
        screen.blit(bulletIMG,(Bulletx,Bullety))
        Bullety-=0.9
    if Bullety<-40:
        state="ready"
        Bullety=480            
    for i in range(0,aliencounter):
        d=sqrt(((Bulletx-alienxlist[i])**2)+((Bullety-alienylist[i])**2))
        if d<35:
            score+=1
            hits=mixer.Sound("D:\\Project pygame\\kills.wav")
            hits.play()
            alienxlist[i],alienylist[i],alienlist[i]=random.randint(0,700),random.choice([0,80]),random.choice(alist)
            state="ready"
            Bullety=420
    screen.blit(playerIMG,(Playerx,Playery))
    score_display = font.render("Score : " + str(score), True, (255, 255, 255))
    screen.blit(score_display, (textX, textY))
    if score>9:
        screen.blit(Win,(100,120))
        backgroundmusic.stop()
        Wins=mixer.Sound("D:\\Project pygame\\Wins.wav")
        Wins.play()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running= False
            if event.type == pygame.KEYDOWN:                
                if event.key == pygame.K_BACKSPACE:
                    stat = "main"
                    Wins.stop()                        
    elif max(alienylist)>470:
        screen.blit(Lose,(100,120))
        backgroundmusic.stop()
        lost=mixer.Sound("D:\\Project pygame\\lost.wav")
        lost.play()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running= False
            if event.type == pygame.KEYDOWN:                
                if event.key == pygame.K_BACKSPACE or event.key == pygame.K_ESCAPE:
                    stat = "main"
                    lost.stop()
                    backgroundmusic.play()
    else:
        alien()
running = True
background=pygame.image.load("D:\\Project pygame\\ground.jpg")
while running:
    screen.blit(background,(0,0))
    if stat == "main":
        main_menu()
    if stat =="START GAME":
        alienselect()
    if stat == "LEVEL":
        levels()  
    pygame.display.update()
