import numpy as np
import pygame
import random
import time


class rock():
    def __init__(self,a=1000):
        self.height=random.randrange(10,200)

        self.posx=a
        self.posy=650

        self.dsp=np.full((50, 20, 3), (150, 150, 150))


        self.sr1=pygame.surfarray.make_surface(self.dsp)
        self.sr2 = pygame.surfarray.make_surface(np.full((50, 20,3),(0,200,50)))
        return None
    def mov(self):
        self.posx=self.posx-30
        if self.posx<35:

            self.__init__()

        screen.blit(self.sr1, (self.posx, self.posy))





class tree():
    def __init__(self):
        self.height=random.randrange(10,200)

        self.posx=1000
        self.posy=340

        self.dsp=np.full((30, 300, 3), (200, 20, 100))
        for i in range(30):
            for j in range(100):
                self.dsp[i][300-self.height-j]=(200,100,150)

        self.sr1=pygame.surfarray.make_surface(self.dsp)
        self.sr2 = pygame.surfarray.make_surface(np.full((30, 300,3),(0,200,50)))
        return None
    def mov(self,bn):
        self.posx=self.posx-20
        if self.posx<bn.posx:
            bn.points =bn.points +1
            self.__init__()

        screen.blit(self.sr1, (self.posx, self.posy))


class bunny:
    def __init__(self):
        self.points=0
        self.hover=0
        self.dir=0
        self.h=0
        self.state=False
        self.astate=0
        self.posx=100
        self.posy=600
        self.an1 = pygame.image.load("bunny1.1.jpg")
        self.an2 = pygame.image.load("bunny1.2.jpg")
        self.an5 = pygame.image.load("bunny1.5.jpg")
        return None
    def blt(self,screen):

        if self.astate==0:

            screen.blit(self.an1,(self.posx,self.posy))
            self.astate=1

        elif self.astate==1:

            screen.blit(self.an2,(self.posx,self.posy))
            if self.posy == 600:
                self.astate=0

        return  None

    def progress(self):
        if self.points>10:
            self.an1 = pygame.image.load("bunny1.6.jpg")
            self.an2 = pygame.image.load("bunny1.7.jpg")
        return None





    def jump(self,a):
        self.h=a


        return None

    def anm_jump(self):
        if self.h!=0:
            if self.dir==-1 and self.hover==0:

                if  600-self.posy<self.h:
                    self.posy=600
                    self.h = 0
                    self.dir=0

                else:
                    self.posy=self.posy+self.h//2
                    self.h = self.h *2
            elif self.dir==-1 and self.hover>0:
                self.hover=self.hover-1
            else:
                self.posy=self.posy-self.h
                self.h=self.h//2
                if self.h // 2 < 2 and self.dir == 0:
                    self.hover=4
                    self.dir = -1
def check(a,b):

    if abs(a.posx-b.posx)<30:
        print( b.posy+300-b.height)
        print(a.posy)
        print(b.posy + 400 - b.height)

        print()

        if (a.posy<b.posy+200-b.height) or (a.posy>b.posy+275-b.height):

            pygame.quit()
            exit()



pygame.init()
surf1=np.full((1500,300,3),(0,150,255))
surf2=np.full((1500,600,3),(0,200,50))
surf3 = pygame.surfarray.make_surface(surf1)
surf4 = pygame.surfarray.make_surface(surf2)

screen = pygame.display.set_mode((1500,800))
font = pygame.font.Font('freesansbold.ttf', 20)
Running=True


pl=bunny()
pl.__init__()
screen.blit(surf3,(0,0))
screen.blit(surf4,(0,300))
pygame.display.flip()
t=tree()
temp=0

r1=rock(350)
r2=rock()

while Running:
    pl.progress()
    screen.blit(surf4, (0, 300))
    pl.anm_jump()
    r1.mov()
    r2.mov()
    t.mov(pl)
    pl.blt(screen)
    text = font.render(str(pl.points), True, (255, 255, 255), (0, 150, 255))
    screen.blit(text, (0, 0))
    pygame.display.flip()



    check(pl,t)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                temp=temp*1.35+3
                if temp>130:
                    temp=130
            if event.key == pygame.K_s:

                pl.jump(temp)
                temp = 0
            if event.key == pygame.K_r:
                pl.points=pl.points+10


    time.sleep(0.1)
