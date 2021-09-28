import pygame
import random
import math
import itertools
import sys

global playerx,playery,b_playery,b_playerx

pygame.init()
#screen = pygame.display.set_mode((570,726))
win = pygame.display.set_mode((600,600))
#background = pygame.image.load('soccer.png')



def drawGrid(w,rows,surface):
        sizeBtwn = w // rows
        x=0 
        y=0
        for l in range(rows):
             x=x+sizeBtwn
             y = y+sizeBtwn
             pygame.draw.line(surface,(255,255,255),(x,0),(x,w))
             pygame.draw.line(surface,(255,255,255),(0,y),(w,y))

rplayer = pygame.image.load('red.png')
redplayer = pygame.transform.scale(rplayer,(30,30))

bplayer = pygame.image.load('blue.png')
blueplayer = pygame.transform.scale(bplayer,(30,30))

ball = pygame.image.load('football-ball.png')
ball = pygame.transform.scale(ball,(20,20))



playerx=random.randint(20,400)
playery=random.randint(40,280)

b_playerx=random.randint(30,400)
b_playery=random.randint(40,300)



p1_x,p1_y  = 300,20
center_player_x ,center_player_y = 300, 300
p3_x,p3_y  = b_playerx+100,b_playery+40
p4_x,p4_y  = b_playerx+150,b_playery+40

r1_x,r1_y = 280,20
r2_x,r2_y = playerx+100,playery+10
r3_x,r3_y = playerx+150,playery+50


def create_blueplayer():
    global b_playery,b_playerx

    
    
        
    win.blit(blueplayer,(p1_x,p1_y))
    win.blit(blueplayer,(center_player_x,center_player_y))
    win.blit(blueplayer,(p3_x,p3_y))
    win.blit(blueplayer,(p4_x,p4_y ))

def create_redplayer():
     global playery,playerx

     win.blit(redplayer,(r1_x,r1_y))
     win.blit(redplayer,(r2_x,r2_y))
     win.blit(redplayer,(r3_x,r3_y))

def create_ball(ball,x):
    win.blit(ball,(x[0],x[1]))
    

   
def euclidean_dis (x1,x2,y1,y2):
    dis = math.sqrt((x2-x1)**2+(y2-y1)**2)
    print(dis)
    return dis


#Calculating the distance between center player and other team mates


def dis(start,end):
    dist = math.dist(start,end)
    return int(dist)

def clearscreen(b):
    b.set_alpha(0)
    


list_blueteam = [[p3_x,p3_y],[p4_x,p4_y],[p1_x,p1_y]]
d=[]
 



for coords in list_blueteam:
    distance = euclidean_dis(center_player_x,coords[0],center_player_y,coords[1])
    print(center_player_x,coords[0],center_player_y,coords[1])
    d.append(distance)
    print(d)




def combination_length(startpoint,combination):
        length=0
        previous = startpoint
        for elem in combination:
            length+= dis(previous,elem)

        return int(length)

def get_shortest_path(start_point,list_of_point):
        min = sys.maxsize
        combination_min = None
        list_of_combinations = list(itertools.permutations(list_blueteam))
        for combination in list_of_combinations:
            length = combination_length(start_point,combination)
            if length<min:
                min=length
                combination_min=combination
        return combination_min

path = get_shortest_path([center_player_x,center_player_y],list_blueteam )
print(path)

    

dead = False
while(dead==False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True
    #screen.blit(background,[0,0])
    drawGrid(600,10,win)
    create_redplayer()
    create_blueplayer()
    create_ball(ball,[300,280])
    
    pygame.display.update()

    events = pygame.event.get()
    for event in events:
        if event.type==pygame.KEYDOWN:

           if event.key == pygame.K_UP: 
                for i in path:
                    
                    create_ball(ball,i)
                    pygame.display.update()
    
                
    
        

        
    
                
                    
                
            
                
        
                
            
    
    
    
    

