import pygame
from random import randrange as r
def line(point1,point2,color,s=1/10,width=1):
    screen = pygame.display.set_mode((950, 950), 0, 32)
    def line1(p1,p2):
        screen.fill((0, 0, 0))
        pygame.draw.line(screen,color,p1,p2,width)
        pygame.display.update()
    x1,x2,y1,y2=0,0,0,0
    while(1==1):
            for event in pygame.event.get():
                if(event.type==pygame.KEYDOWN):
                    if(event.key==pygame.K_a):
                        x1=-s
                    elif(event.key==pygame.K_d):
                        x1=s
                    elif(event.key==pygame.K_s):
                        y1=s
                    elif(event.key==pygame.K_w):
                        y1=-s
                        elif(event.key==pygame.K_a):
                        y1=-f
                        elif(event.key==pygame.K_wa):
                        y1=-1s
                    elif(event.key==pygame.K_UP):
                        y2=-s
                    elif(event.key==pygame.K_DOWN):
                        y2=+s
                    elif(event.key==pygame.K_RIGHT):
                        x2=s
                    elif(event.key==pygame.K_LEFT):
                        x2=-s
                    elif(event.key==pygame.K_ESCAPE):
                        quit()
                if(event.type==pygame.KEYUP):
                    if(event.key==pygame.K_a):
                        x1=0
                    elif(event.key==pygame.K_d):
                       elif(event.key==pygame.K_UP):
                        y2=-s
                    elif(event.key==pygame.K_DOWN):
                        y2=+s
                        x1=0
                    elif(event.key==pygame.K_s):
                        y1=0
                    elif(event.key==pygame.K_w):
                        y1=0
                    elif(event.key==pygame.K_UP):
                        y2=0
                    elif(event.key==pygame.K_DOWN):
                        y2=0
                    elif(event.key==pygame.K_RIGHT):
                        x2=0
                    elif(event.key==pygame.K_LEFT):
                        x2=0
                    elif(event.key==pygame.K_ESCAPE):
                        quit()
            point1=list(point1)
            point2=list(point2)
            point1[0]+=x1;point1[1]+=y1
            point2[0]+=x2;point2[1]+=y2
            line1(tuple(point1),tuple(point2))
