import pygame
import random
import math

pygame.init()
ground = (500, 600)
goal_position = (210, 290)
open_ground = 20
global players
global center_player
global middle_player
screen = pygame.display.set_mode(ground)
red_player_image = pygame.transform.scale(pygame.image.load('red.png'),(30,30))
blue_player_image = pygame.transform.scale(pygame.image.load('blue.png'),(25,25))
ball_image = pygame.transform.scale(pygame.image.load('football-ball.png'),(10,10))
global ball_position_update_by

class player:
    def __init__(self): 
        self.position = None
        self.goal_position = None
        self.huristic = None
        self.team = None
        self.id = None

class ground_layout:
    def __init__(self): 
        self.ground_background = (57,120,25)
        self.layout_color = (255,255,255)
        self.goal_red_color = (255,0,0)
        self.goal_blue_color = (7,55,99)
        self.red_area_box = (
            (ground[0] - int(ground[0] * 0.8), open_ground),
            (int(ground[0] * 0.8), open_ground), 
            (ground[0] - int(ground[0] * 0.8), int(ground[1] * 0.2)),
            (int(ground[0] * 0.8), int(ground[1] * 0.2)))
        self.blue_area_box = (
            (ground[0] - int(ground[0] * 0.8), ground[1] - open_ground),
            (int(ground[0] * 0.8), ground[1] - open_ground), 
            (ground[0] - int(ground[0] * 0.8), ground[1] - int(ground[1] * 0.2)),
            (int(ground[0] * 0.8), ground[1] - int(ground[1] * 0.2)))
        self.playing_area_box = (
            (open_ground, open_ground),
            (ground[0] - open_ground, open_ground),
            (open_ground, ground[1] - open_ground),
            (ground[0] - open_ground, ground[1] - open_ground))
        
def drawGrid(grnd):
    #background
    screen.fill(grnd.ground_background)
    #outer Line
    pygame.draw.line(screen, grnd.layout_color, grnd.playing_area_box[0], grnd.playing_area_box[1])
    pygame.draw.line(screen, grnd.layout_color, grnd.playing_area_box[0], grnd.playing_area_box[2])
    pygame.draw.line(screen, grnd.layout_color, grnd.playing_area_box[3], grnd.playing_area_box[1])
    pygame.draw.line(screen, grnd.layout_color, grnd.playing_area_box[3], grnd.playing_area_box[2])
    #Red Player Box
    pygame.draw.line(screen, grnd.layout_color, grnd.red_area_box[0], grnd.red_area_box[1])
    pygame.draw.line(screen, grnd.layout_color, grnd.red_area_box[0], grnd.red_area_box[2])
    pygame.draw.line(screen, grnd.layout_color, grnd.red_area_box[3], grnd.red_area_box[1])
    pygame.draw.line(screen, grnd.layout_color, grnd.red_area_box[3], grnd.red_area_box[2])
    #Blue Player Box
    pygame.draw.line(screen, grnd.layout_color, grnd.blue_area_box[0], grnd.blue_area_box[1])
    pygame.draw.line(screen, grnd.layout_color, grnd.blue_area_box[0], grnd.blue_area_box[2])
    pygame.draw.line(screen, grnd.layout_color, grnd.blue_area_box[3], grnd.blue_area_box[1])
    pygame.draw.line(screen, grnd.layout_color, grnd.blue_area_box[3], grnd.blue_area_box[2])
    #Center Circle
    pygame.draw.circle(screen, grnd.layout_color, (ground[0] // 2, ground[1] // 2), 30)
    pygame.draw.circle(screen, grnd.ground_background, (ground[0] // 2, ground[1] // 2), 28)
    #center Line
    pygame.draw.line(screen, grnd.layout_color, (open_ground, ground[1] // 2), (ground[0] - open_ground, ground[1] // 2))
    #Goal Post
    pygame.draw.rect(screen, grnd.goal_red_color, pygame.Rect(goal_position[0], 0, goal_position[1] - goal_position[0], open_ground))
    pygame.draw.rect(screen, grnd.goal_blue_color, pygame.Rect(goal_position[0], ground[1] - open_ground, goal_position[1] - goal_position[0], open_ground))
        


def initPlayer(grnd):
    global center_player
    center_player = createPlayers('BLUE', 0, (ground[0] // 2, ground[1] // 2))
    global players
    players = []
    # Red Box Player
    players.append(createPlayers('BLUE', 1, 
        (random.randint(grnd.red_area_box[0][0]+15, grnd.red_area_box[1][0]-15), random.randint(grnd.red_area_box[0][1]+15, grnd.red_area_box[2][1]-15))))
    players.append(createPlayers('RED', 1, 
        (random.randint(grnd.red_area_box[0][0]+15, grnd.red_area_box[1][0]-15), random.randint(grnd.red_area_box[0][1]+15, grnd.red_area_box[2][1]-15))))
    # Outer Player
    players.append(createPlayers('BLUE', 2, 
        (random.randint(open_ground+15, ground[0] - open_ground-15), random.randint(grnd.red_area_box[2][1]+15, ground[0]//2 -15))))
    players.append(createPlayers('RED', 2, 
        (random.randint(open_ground+15, ground[0] - open_ground-15), random.randint(grnd.red_area_box[2][1]+15, ground[0]//2 -15))))
    players.append(createPlayers('BLUE', 3, 
        (random.randint(open_ground+15, ground[0] - open_ground-15), random.randint(grnd.red_area_box[2][1]+15, ground[0]//2 -15))))
    players.append(createPlayers('RED', 3, 
        (random.randint(open_ground+15, ground[0] - open_ground-15), random.randint(grnd.red_area_box[2][1]+15, ground[0]//2 -15))))
        
def createPlayers(team, id, position):
    p = player()
    p.position = position
    p.team = team
    p.id = id
    if p.position[0] < goal_position[0]:
        p.goal_position = (goal_position[0], open_ground)
    elif p.position[0] > goal_position[1]:
        p.goal_position = (goal_position[1], open_ground)
    else:
        p.goal_position = (p.position[0], open_ground)
    p.huristic = math.sqrt((p.position[0] - p.goal_position[0]) ** 2 + (p.position[1] - p.goal_position[1]) ** 2)
    return p

def display_players():
    global players
    for p in players:
        img = red_player_image
        if p.team == 'BLUE':
            img = blue_player_image
        pos = (p.position[0] - 15, p.position[1] - 15)
        screen.blit(img, pos)

    pos = (center_player.position[0]-15, center_player.position[1] + 5)
    screen.blit(blue_player_image, pos)
    
def find_path():
    global center_player
    global players
    global middle_player
    cost = ground[1]
    middle_player = None
    for p in players:
        if center_player.team == p.team:
            tmp = p.huristic + math.sqrt((p.position[0] - center_player.position[0]) ** 2 + (p.position[1] - center_player.position[1]) ** 2)
            if cost > tmp:
                cost = tmp
                middle_player = p
 

def play_game(grnd, ball_position):
    drawGrid(grnd)
    display_players()
    screen.blit(ball_image, ball_position)

def init_game(grnd):
    global middle_player
    initPlayer(grnd)
    ball_latest_position = (ground[0] // 2-5, ground[1] // 2-5)
    find_path()
    cost = (math.sqrt((middle_player.position[0] - center_player.position[0]) ** 2 + (middle_player.position[1] - center_player.position[1]) ** 2)) // 4
    return ball_latest_position, ((middle_player.position[0] - center_player.position[0])/cost, (middle_player.position[1] - center_player.position[1])/cost, cost, True)

def forward_ball():
    global middle_player
    cost = middle_player.huristic // 4
    return ((middle_player.goal_position[0] - middle_player.position[0])/cost, (middle_player.goal_position[1] - middle_player.position[1])/cost, cost, False)


def main():
    global ball_position_update_by
    grnd = ground_layout()
    ball_latest_position, ball_position_update_by = init_game(grnd)
    play_game(grnd, ball_latest_position)

    clk = pygame.time.Clock()
    flag = True
    while flag:
        pygame.display.update()
        ball_latest_position = (ball_latest_position[0] + ball_position_update_by[0], ball_latest_position[1] + ball_position_update_by[1])
        ball_position_update_by = (ball_position_update_by[0], ball_position_update_by[1], ball_position_update_by[2]-1, ball_position_update_by[3])
        if ball_position_update_by[2] < 0:
            if ball_position_update_by[3]:
                ball_position_update_by = forward_ball()
                pygame.time.delay(150)
                clk.tick(5)
            else:
                ball_latest_position, ball_position_update_by = init_game(grnd)
                pygame.time.delay(250)
                clk.tick(5)
        else:
            pygame.time.delay(25)
            clk.tick(5)
        
        play_game(grnd, ball_latest_position)
        

if __name__ == '__main__':
    main()
