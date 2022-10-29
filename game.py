import pygame
import time
import random
import sys
from pygame import mixer
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Car crash Racing")
icon = pygame.image.load("D:\caricon.jpeg")
pygame.display.set_icon(icon)
car = pygame.image.load("C:\\Users\\Chandrahas\\Downloads\\car (2).png")
clock=pygame.time.Clock()
grass=pygame.image.load("C:\\Users\\Chandrahas\\Downloads\\grass.jpg")
yellstr=pygame.image.load("C:\\Users\\Chandrahas\\Downloads\\yellow_strip.jpg")
stri=pygame.image.load("C:\\Users\\Chandrahas\\Downloads\\strip.jpg")
over_font = pygame.font.Font('freesansbold.ttf', 64)
over_font1 = pygame.font.Font('freesansbold.ttf', 32)
over_font2 = pygame.font.Font('freesansbold.ttf', 16)

over_text = over_font.render("GAME OVER", True, (0, 0, 0))
enem=pygame.image.load("C:\\Users\\Chandrahas\\Downloads\\car4.jpg")
enem1=pygame.image.load("C:\\Users\\Chandrahas\\Downloads\\car5.jpg")
enem2=pygame.image.load("C:\\Users\\Chandrahas\\Downloads\\car6.jpg")
enem3=pygame.image.load("C:\\Users\\Chandrahas\\Downloads\\car7.jpg")
intba=pygame.image.load("C:\\Users\\Chandrahas\\Downloads\\background.jpg")
intba1=pygame.image.load("C:\\Users\\Chandrahas\\Downloads\\background2.jpg")

def desi():
    int=True
    while int:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                int = False
                pygame.quit()
                quit()
                sys.quit()
        click=pygame.mouse.get_pressed()
        pos=pygame.mouse.get_pos()
        pos2=pygame.mouse.get_pos()
        pos3=pygame.mouse.get_pos()
        #print(pos3)
        screen.blit(intba,(0,0))
        title=over_font.render("CAR RACING", True, (0, 0, 0))
        start=over_font1.render("START", True, (0, 0, 0))
        quit  = over_font1.render("QUIT", True, (0, 0, 0))
        instr=over_font2.render("INSRTUCTION", True, (0, 0, 0))
        screen.blit(title,(200,50))
        pygame.draw.rect(screen,(10,255,50),(80,500,150,50))
        pygame.draw.rect(screen, (255, 40, 70), (300, 500, 150, 50))
        pygame.draw.rect(screen, (70, 50, 255), (550, 500, 150, 50))
        screen.blit(start, (100, 510))
        screen.blit(quit,(580,510))
        screen.blit(instr,(320,515))
        if(pos[0]>=80 and pos[0]<=230 and pos[1]>=500 and pos[1]<=550):
            pygame.draw.rect(screen, (10, 60, 90), (80, 500, 150, 50))
            screen.blit(start, (100, 510))
            if(click==(1,0,0)):
                gameloop()
        if (pos2[0] >= 550 and pos2[0] <= 698 and pos2[1] >= 502 and pos2[1] <= 550):
            pygame.draw.rect(screen, (140, 120, 105), (550, 500, 150, 50))
            screen.blit(quit,(580,510))
            if (click == (1, 0, 0)):
                pygame.quit()
                quit()
                sys.quit()
        if (pos3[0] >= 300 and pos3[0] <= 448 and pos2[1] >= 502 and pos2[1] <= 550):
            pygame.draw.rect(screen, (60, 60, 15), (300, 500, 150, 50))
            screen.blit(instr,(320,515))
            if(click==(1,0,0)):
                instru()
        pygame.display.update()


def carin(x,y):
    screen.blit(car, (x, y))
def backgr():
    screen.blit(grass, (0, 0))
    screen.blit(grass, (700, 0))
    screen.blit(yellstr,(400,0))
    screen.blit(yellstr, (400, 100))
    screen.blit(yellstr, (400, 200))
    screen.blit(yellstr, (400, 300))
    screen.blit(yellstr, (400, 400))
    screen.blit(yellstr, (400, 500))
    screen.blit(stri, (120, 0))
    screen.blit(stri, (680, 0))

def enemy(x,y,obs):
    if obs==0:
        screen.blit(enem, (x, y))
    elif obs==1:
        screen.blit(enem1, (x, y))
    elif obs==2:
        screen.blit(enem2, (x, y))
    elif obs==3:
        screen.blit(enem3, (x, y))
def score_card(carpass,score,level):
    score_text = over_font1.render("Score:"+str(score), True, (0, 0, 0))
    cars=over_font1.render("passed:"+str(carpass), True, (200, 200, 200))
    le = over_font1.render("level:" + str(level), True, (200, 200, 200))
    screen.blit(score_text, (0, 50))
    screen.blit(cars, (0, 100))
    screen.blit(le, (0, 150))

def instru():
    intq = True
    while intq:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intq = False
                pygame.quit()
                quit()
                sys.exit()
        click1 = pygame.mouse.get_pressed()
        pos4 = pygame.mouse.get_pos()
        screen.blit(intba1,(0,0))
        cont=over_font.render("CONTROLS",True,(0,0,0))
        ww=over_font1.render("BACK",True,(0,0,0))
        screen.blit(cont,(100,100))

        pygame.draw.rect(screen, (70, 50, 255), (550, 120, 150, 50))
        screen.blit(ww, (570, 130))
        if (pos4[0] >= 550 and pos4[0] <= 698 and pos4[1] >= 120 and pos4[1] <= 170):
        #print(pos4)

            if (click1 == (1, 0, 0)):
                desi()
        pygame.display.update()

def pause():
    intqq = True
    while intqq:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intqq = False
                pygame.quit()
                quit()
                sys.exit()
        #click1 = pygame.mouse.get_pressed()
        #pos4 = pygame.mouse.get_pos()
        pos6=pygame.mouse.get_pos()
        conti = over_font2.render("CONTINUE", True, (0, 0, 0))
        rest = over_font2.render("RESTART", True, (0, 0, 0))
        mainme = over_font2.render("MAIN MENU", True, (0, 0, 0))
        screen.blit(intba1, (0, 0))
        cont33 = over_font.render("GAMEPAUSED", True, (0, 0, 0))
        screen.blit(cont33, (180, 100))
        pygame.draw.rect(screen, (10, 255, 50), (80, 500, 150, 50))
        pygame.draw.rect(screen, (255, 40, 70), (300, 500, 150, 50))
        pygame.draw.rect(screen, (241, 166, 89), (550, 500, 150, 50))
        screen.blit(conti, (110, 517))
        screen.blit(rest, (580, 515))
        screen.blit(mainme, (330, 517))
        click7 = pygame.mouse.get_pressed()
        #print(pos6)
        if (pos6[0] >= 80 and pos6[0] <= 230 and pos6[1] >= 500 and pos6[1] <= 550):

            if (click7 == (1, 0, 0)):
                intqq=False


        if (pos6[0] >= 300 and pos6[0] <= 450 and pos6[1] >= 500 and pos6[1] <= 550):

            if (click7 == (1, 0, 0)):
                desi()


        if (pos6[0] >= 550 and pos6[0] <= 700 and pos6[1] >= 500 and pos6[1] <= 550):

            if (click7 == (1, 0, 0)):
                gameloop()

        #clock.tick(30)
        pygame.display.update()


def gameloop():
    playx = 400
    playy = 470
    plachan = 0
    running = True
    enemX = random.randrange(200,600)
    enemY = -750
    obsspe=8
    obse=0
    level=0
    carpass=0
    score=0

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    plachan = -5
                if event.key == pygame.K_RIGHT:
                    plachan = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    plachan = 0
        screen.fill((119, 119, 119))



        playx += plachan

        backgr()
        enemY -= (obsspe / 4)
        enemy(enemX,enemY,obse)
        enemY+=obsspe
        if enemY==600:
            enemY=0
            enemX = random.randrange(200, 600)
            obse = random.randrange(0, 3)
            carpass+=1
            score=carpass*10
            if(carpass%10==0):
                level+=1
                obsspe=obsspe+2
                time.sleep(2)




        score_card(carpass,score,level)
        if playy-100< enemY:
            if playx>enemX and playx < enemX+50 or playx+50 > enemX and playx+50 < enemX+50:
                screen.blit(over_text, (200, 200))
                pygame.display.update()
                running = False
                time.sleep(5)
                gameloop()

        if playx <= 80:
            playx = 80

        elif (playx >= 600):
            playx = 600
        carin(playx, playy)
        if playx<=80 or playx>=600:
            screen.blit(over_text, (200, 200))
            pygame.display.update()
            running=False
            time.sleep(5)
            gameloop()
        pos5 = pygame.mouse.get_pos()
        click2 = pygame.mouse.get_pressed()
        cont1 = over_font1.render("PAUSE", True, (0, 0, 0))
        pygame.draw.rect(screen, (116, 140, 94), (680, 0, 150, 50))
        screen.blit(cont1, (680, 0))
        #print(pos5)

        if (pos5[0] >= 660 and pos5[0] <= 800 and pos5[1] >= 3 and pos5[1] <= 51):


            if (click2 == (1, 0, 0)):
                pause()

        pygame.display.update()
        clock.tick(100)
desi()
gameloop()
pygame.quit()
quit()