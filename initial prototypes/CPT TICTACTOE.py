import pygame
import random
import sys

#define colours
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

pygame.init()

#set height & width of screen
size = [1000, 600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("CPT GAME")

#functions!
def board_draw():
    for offset in range (2):
        pygame.draw.line(screen,BLACK,[250+166*offset,50],[250+166*offset,548],5)
        pygame.draw.line(screen,BLACK,[84,216+166*offset],[582,216+166*offset],5)

def mouse_hover(x_hover,y_hover,x_click,y_click):
    global turn, tile
    for y in range (3):
        for x in range(3):
            if 250+x*166 > x_hover > 84+x*166 and 216+y*166 > y_hover > 50+y*166 and turn == 1 and tile[y*3+x] == 0:
                pygame.draw.ellipse(screen,RED,[96+x*166,62+y*166,142,142],5)
            elif 250+x*166 > x_hover > 84+x*166 and 216+y*166 > y_hover > 50+y*166 and turn == 2 and tile[y*3+x] == 0:
                pygame.draw.line(screen,GREEN,[96+x*166,62+y*166],[238+x*166,204+y*166],5)
                pygame.draw.line(screen,GREEN,[238+x*166,62+y*166],[96+x*166,204+y*166],5)

            if 250+x*166 > x_click > 84+x*166 and 216+y*166 > y_click > 50+y*166 and turn == 1 and tile[y*3+x] == 0:
                o_input.append([96+x*166,62+y*166])
                mouse_click.insert(0,[-10000,-10000])
                tile[y*3+x] = 1
                turn = 2
            elif 250+x*166 > x_click > 84+x*166 and 216+y*166 > y_click > 50+y*166 and turn == 2 and tile[y*3+x] == 0:
                x_input.append([96+x*166,62+y*166])
                mouse_click.insert(0,[-10000,-10000])
                tile[y*3+x] = -1
                turn = 1

def xo_draw(o_input,x_input):
    for entry in o_input:
        pygame.draw.ellipse(screen,RED,[entry[0],entry[1],142,142],5)
    for entry in x_input:
        pygame.draw.line(screen,GREEN,[entry[0],entry[1]],[entry[0]+142,entry[1]+142],5)
        pygame.draw.line(screen,GREEN,[entry[0]+142,entry[1]],[entry[0],entry[1]+142],5)

def win_check():
    wins = [[tile[0],tile[1],tile[2]],[tile[3],tile[4],tile[5]],\
            [tile[6],tile[7],tile[8]],[tile[0],tile[3],tile[6]],\
            [tile[1],tile[4],tile[7]],[tile[2],tile[5],tile[8]],\
            [tile[0],tile[4],tile[8]],[tile[2],tile[4],tile[6]]]
    for i in range (len(wins)):
        sum = 0
        for space in wins[i]:
            sum += space
        if sum == 3:
            return "o"
        elif sum == -3:
            return "x"

def point_counter():
    global o_win, x_win, tile, game_done
    if win_check() == "o":
        o_win += 1
    elif win_check() == "x":
        x_win += 1
    tile = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    game_done = True

def keep_playing(x,y):
    pygame.draw.rect(screen,BLACK, [100,100,800,400])
    for button_offset in range (2):
        pygame.draw.rect(screen,RED,[200+button_offset*400,300,200,100])
        if 400 >= x >= 200 and 400 >= y >= 300:
            pygame.draw.rect(screen,GREEN,[200,300,200,100])
        elif 800 >= x >= 600 and 400 >= y >= 300:
            pygame.draw.rect(screen,GREEN,[600,300,200,100])
    back_check(mouse_click[0][0],mouse_click[0][1])

def back_check(x,y):
    if 400 >= x >= 200 and 400 >= y >= 300:
        pygame.quit()
        sys.exit()
    elif 800 >= x >= 600 and 400 >= y >= 300:
        reset()

def reset():
    global turn, o_input, x_input, o_win, x_win, game_done
    turn = random.randint(1,2)
    o_input = []
    x_input = []
    game_done = False

def main():
    print "o", o_win
    print "x", x_win
    board_draw()
    if game_done == False:
        mouse_hover(x_pos,y_pos,mouse_click[0][0],mouse_click[0][1])
    xo_draw(o_input,x_input)
    if win_check() != None or len(o_input)+len(x_input) == 9:
        point_counter()
    if game_done == True:
        keep_playing(x_pos,y_pos)

#loop until the user clicks the close button.
done = False
mouse_click = [[-10000,-10000]]

turn = random.randint(1,2)
tile = [0, 0, 0, 0, 0, 0, 0, 0, 0]
o_input = []
x_input = []
o_win = 0
x_win = 0
game_done = False

#Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    #get mouse coordinates
    pos = pygame.mouse.get_pos()
    x_pos = pos[0]
    y_pos = pos[1]

# ----- Main Event Loop -----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("User asked to quit.")
            done = True
        elif event.type == pygame.KEYDOWN:
            print("User pressed a key.")
        elif event.type == pygame.KEYUP:
            print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button")
            mouse_click.insert(0,[x_pos,y_pos])

    #set the screen background colour
    screen.fill(WHITE)

    main()

    #limit to 30 frames per second
    clock.tick(30)

    #update screen with drawings
    pygame.display.flip()

#idle friendly, anti-hang quit line
pygame.quit()