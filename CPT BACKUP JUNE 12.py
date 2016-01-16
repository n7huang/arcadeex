import pygame
import random
import sys
import pygame.mixer

#define colours
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
GREY     = ( 200, 200, 200)

pygame.init()#initialize game engine
pygame.mixer.init()#initialize sound engine

#set height & width of screen
size = [1000, 600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ultimate Arcade Extreme v1.1")

#images imported
button_0 = pygame.image.load("images/button_0.png")
button_1 = pygame.image.load("images/button_1.png")
button_2 = pygame.image.load("images/button_2.png")
title = pygame.image.load("images/titlecard.png")
cursor = pygame.image.load("images/eunjicursor.png")
exit_0 = pygame.image.load("images/exit_0.png")
exit_1 = pygame.image.load("images/exit_1.png")
bg_img = pygame.image.load("images/bg_image.png")
mute_0 = pygame.image.load("images/mute_0.png")
mute_1 = pygame.image.load("images/mute_1.png")
board = pygame.image.load("images/board.png")
o_tile = pygame.image.load("images/o.png")
x_tile = pygame.image.load("images/x.png")
tictactoe = pygame.image.load("images/tictactoetitle.png")
score_bg = pygame.image.load("images/score_bg.png")
score_o = pygame.image.load("images/score_o.png")
score_x = pygame.image.load("images/score_x.png")
back_0 = pygame.image.load("images/back_0.png")
back_1 = pygame.image.load("images/back_1.png")
info = pygame.image.load("images/info_button.png")
music_0 = pygame.image.load("images/music_0.png")
music_1 = pygame.image.load("images/music_1.png")

shutdown_0 = pygame.image.load("images/shutdown1.png")
shutdown_1 = pygame.image.load("images/shutdown2.png")
shutdown_2 = pygame.image.load("images/shutdown3.png")
shutdown_3 = pygame.image.load("images/shutdown4.png")
shutdown_4 = pygame.image.load("images/shutdown5.png")
shutdown_5 = pygame.image.load("images/shutdown6.png")
shutdown_6 = pygame.image.load("images/shutdown7.png")
shutdown_7 = pygame.image.load("images/shutdown8.png")
shutdown_8 = pygame.image.load("images/shutdown9.png")
shutdown_9 = pygame.image.load("images/shutdown10.png")
shutdown_10 = pygame.image.load("images/shutdown11.png")

#sounds
bg_music = pygame.mixer.Sound("audio/unconditional.ogg")
back_sound = pygame.mixer.Sound("audio/back_button.ogg")
button_hover = pygame.mixer.Sound("audio/button_hover.ogg")
button_press = pygame.mixer.Sound("audio/button_press.ogg")
blue_button = pygame.mixer.Sound("audio/soundonoff.ogg")
xo_enter = pygame.mixer.Sound("audio/xopress.ogg")
door_open = pygame.mixer.Sound("audio/door_open.ogg")
door_close = pygame.mixer.Sound("audio/door_close.ogg")

#functions!
#main menu
def cursor_draw(x,y):
    screen.blit(cursor,[x,y])

def button_draw(x,y,menu_check):
    global button_hover_played, open_sound, close_sound
    font = pygame.font.SysFont('Courier New', 23, True, False)
    if menu_check == True:
        screen.blit(title,[150,63])
        screen.blit(exit_0,[945,545])
        for button_offset in range (2):
            screen.blit(button_0,[200+button_offset*400,350])
        text = font.render("TIC TAC TOE",True,WHITE)
        screen.blit(text, [223,388])
        text = font.render("HANGMAN",True,WHITE)
        screen.blit(text, [653,388])
        if 400 >= x >= 200 and 450 >= y >= 350:
            screen.blit(button_1,[200,350])
            text = font.render("TIC TAC TOE",True,WHITE)
            screen.blit(text, [223,388])
            if button_hover_played == False:
                button_hover.play()
                button_hover_played = True
        elif 800 >= x >= 600 and 450 >= y >= 350:
            screen.blit(button_1,[600,350])
            text = font.render("HANGMAN",True,WHITE)
            screen.blit(text, [653,388])
            if button_hover_played == False:
                button_hover.play()
                button_hover_played = True
        elif x >= 950 and y >= 550:
            screen.blit(exit_1,[945,545])
            if open_sound == False:
                door_open.play()
                open_sound = True
        else:
            button_hover_played = False
            open_sound = False
    elif menu_check == False:
        if 100 >= x >= 0 and y >= 545:
            screen.blit(back_1,[0,545])
        else:
            screen.blit(back_0,[0,545])

def press_check(x_click,y_click,menu_check):
    global screen_state
    if 400 >= x_click >= 200 and 450 >= y_click >= 350 and menu_check == True:
        button_press.play()
        print "PLAY TTT"
        mouse_click.insert(0,[-10000,-10000])
        screen_state = 1
    elif 800 >= x_click >= 600 and 450 >= y_click >= 350 and menu_check == True:
        button_press.play()
        print "PLAY HM"
        mouse_click.insert(0,[-10000,-10000])
        screen_state = 2

def exit_check(x,y):
    global screen_state, menu_check, close_sound
    if menu_check == True:
        if x >= 950 and y >= 550:
            if close_sound == False:
                door_close.play()
                close_sound = True
            return True
    elif menu_check == False:
        if 100 >= x >= 0 and y >= 545:
            back_sound.play()
            menu_check = True
            screen_state = 0
            reset_TTT()
            score_reset()

def music_button(x,y):
    global music_mute
    if music_mute == False:
        screen.blit(music_0,[950,0])
    elif music_mute == True:
        screen.blit(music_1,[950,0])
    if x >= 950 and y <= 50:
        music_mute = not(music_mute)
        blue_button.play()
        mouse_click.insert(0,[-10000,-10000])

def sound_button(x,y):
    global sound_mute
    if sound_mute == False:
        screen.blit(mute_0,[890,0])
    elif sound_mute == True:
        screen.blit(mute_1,[890,0])
    if 940 >= x >= 890 and y <= 50:
        sound_mute = not(sound_mute)
        blue_button.play()
        mouse_click.insert(0,[-10000,-10000])

def info_button(x,y):
    global info_screen, blue_hover_played
    screen.blit(info,[1,0])
    info_screen = False
    if 51 >= x >= 0 and 50 >= y >= 0:
        if blue_hover_played == False:
            blue_button.play()
            blue_hover_played = True
            info_screen = True
        mouse_click.insert(0,[-10000,-10000])
    else:
        blue_hover_played = False
        info_screen = False

def info_show():
    if info_screen == True:
        screen.blit(score_bg,[360,100])

def sound_player():
    global bg_played
    if bg_played == False:
        bg_music.play(-1)
        bg_played = True

def shut_down():
    global shutdown_timer
    if shutdown_timer < 1:
        screen.blit(shutdown_0,[0,0])
        shutdown_timer += 1
    elif shutdown_timer < 2:
        screen.blit(shutdown_1,[0,0])
        shutdown_timer += 1
    elif shutdown_timer < 3:
        screen.blit(shutdown_2,[0,0])
        shutdown_timer += 1
    elif shutdown_timer < 4:
        screen.blit(shutdown_3,[0,0])
        shutdown_timer += 1
    elif shutdown_timer < 5:
        screen.blit(shutdown_4,[0,0])
        shutdown_timer += 1
    elif shutdown_timer < 6:
        screen.blit(shutdown_5,[0,0])
        shutdown_timer += 1
    elif shutdown_timer < 7:
        screen.blit(shutdown_6,[0,0])
        shutdown_timer += 1
    elif shutdown_timer < 8:
        screen.blit(shutdown_7,[0,0])
        shutdown_timer += 1
    elif shutdown_timer < 9:
        screen.blit(shutdown_8,[0,0])
        shutdown_timer += 1
    elif shutdown_timer < 10:
        screen.blit(shutdown_9,[0,0])
        shutdown_timer += 1
    elif shutdown_timer < 20:
        screen.blit(shutdown_10,[0,0])
        shutdown_timer += 1
    elif shutdown_timer >= 20:
        pygame.quit()
        sys.exit()

#tic tac toe
def board_draw():
    screen.blit(board,[135,80])

def mouse_hover(x_hover,y_hover,x_click,y_click):
    global turn, tile, xohover_played
    for y in range (3):
        for x in range(3):
            if 263+x*133 > x_hover > 135+x*133 and 208+y*133 > y_hover > 80+y*133 and tile[y*3+x] == 0:
                if turn == 1:
                    screen.blit(o_tile,[143+x*133,88+y*133])
                elif turn == 2:
                    screen.blit(x_tile,[143+x*133,88+y*133])

            if 263+x*133 > x_click > 135+x*133 and 208+y*133 > y_click > 80+y*133 and turn == 1 and tile[y*3+x] == 0:
                xo_enter.play()
                o_input.append([143+x*133,88+y*133])
                mouse_click.insert(0,[-10000,-10000])
                tile[y*3+x] = 1
                turn = 2
            elif 263+x*133 > x_click > 135+x*133 and 208+y*133 > y_click > 80+y*133 and turn == 2 and tile[y*3+x] == 0:
                xo_enter.play()
                x_input.append([143+x*133,88+y*133])
                mouse_click.insert(0,[-10000,-10000])
                tile[y*3+x] = -1
                turn = 1

def xo_draw(o_input,x_input):
    for entry in o_input:
        screen.blit(o_tile,[entry[0],entry[1]])
    for entry in x_input:
        screen.blit(x_tile,[entry[0],entry[1]])

def win_check():
    wins = [[tile[0],tile[1],tile[2]],[tile[3],tile[4],tile[5]],\
            [tile[6],tile[7],tile[8]],[tile[0],tile[3],tile[6]],\
            [tile[1],tile[4],tile[7]],[tile[2],tile[5],tile[8]],\
            [tile[0],tile[4],tile[8]],[tile[2],tile[4],tile[6]]]
    sum_list = []
    for i in range (len(wins)):
        sum_tiles = 0
        for space in wins[i]:
            sum_tiles += space
        sum_list.append(sum_tiles)
    if 3 in sum_list:
        return "o"
    elif -3 in sum_list:
        return "x"
    elif (0 not in sum_list) and (3 not in sum_list) and (-3 not in sum_list) and len(o_input)+len(x_input) == 9:
        return "tie"

def point_counter():
    global o_win, x_win, tile, game_done
    if win_check() == "o":
        o_win += 1
        game_history.insert(0,"O WIN")
    elif win_check() == "x":
        x_win += 1
        game_history.insert(0,"X WIN")
    elif win_check() == "tie":
        game_history.insert(0,"CATS")
    tile = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    game_done = True

def keep_playing(x,y):
    global button_hover_played
    screen.blit(button_2,[603,375])
    font = pygame.font.SysFont('Courier New', 23, True, False)
    text = font.render("PLAY AGAIN?",True,GREY)
    screen.blit(text, [626,413])
    if game_done == True:
        screen.blit(button_0,[603,375])
        text = font.render("PLAY AGAIN?",True,WHITE)
        screen.blit(text, [626,413])
        if 803 >= x >= 603 and 475 >= y >= 375:
            if button_hover_played == False:
                button_hover.play()
                button_hover_played = True
            screen.blit(button_1,[603,375])
            text = font.render("PLAY AGAIN?",True,WHITE)
            screen.blit(text, [626,413])
        else:
            button_hover_played = False
        reset_check(mouse_click[0][0],mouse_click[0][1])

def reset_check(x,y):
    if 795 >= x >= 595 and 475 >= y >= 375:
        button_press.play()
        reset_TTT()

def reset_TTT():
    global turn, tile, o_input, x_input, game_done
    turn = random.randint(1,2)
    tile = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    o_input = []
    x_input = []
    game_done = False
    xo_win == 0

def score_reset():
    global o_win, x_win, game_history
    o_win = 0
    x_win = 0
    game_history = []

def score_blit():
    screen.blit(score_bg,[562,67])
    font = pygame.font.SysFont('Courier New', 30, True, False)
    screen.blit(tictactoe,[570,75])
    screen.blit(score_o,[640,240])
    screen.blit(score_x,[640,285])

    text = font.render(":   " + str(o_win),True,WHITE)
    screen.blit(text, [675, 240])
    text = font.render(":   " + str(x_win),True,WHITE)
    screen.blit(text, [675, 285])

    font = pygame.font.SysFont('Courier New', 20, True, False)
    if len(game_history) == 0:
        text = font.render("FIRST GAME OF SESSION",True,WHITE)
        screen.blit(text, [574, 330])
    else:
        text = font.render("PREVIOUS GAME: " + str(game_history[0]),True,WHITE)
        screen.blit(text, [580, 330])

#main functions
def TTT():
    global menu_check
    menu_check = False
    board_draw()
    xo_draw(o_input,x_input)
    score_blit()
    if game_done == False:
        mouse_hover(x_pos,y_pos,mouse_click[0][0],mouse_click[0][1])
    if win_check() != None:
        point_counter()
    keep_playing(x_pos,y_pos)

def HM():
    global menu_check
    menu_check = False
    print "PLAY hangman"

def main():
    global menu_check, mouse_click, screen_state
    screen.blit(bg_img,[0,0])
    done = exit_check(mouse_click[0][0],mouse_click[0][1])
    button_draw(x_pos,y_pos,menu_check)
    music_button(mouse_click[0][0],mouse_click[0][1])
    sound_button(mouse_click[0][0],mouse_click[0][1])
    info_button(x_pos,y_pos)
    info_show()
    sound_player()
    if screen_state == 0:
        press_check(mouse_click[0][0],mouse_click[0][1],menu_check)
    if done == True:
        shut_down()
    elif screen_state == 1:
        TTT()
        mouse_click = [[-10000,-10000]]
    elif screen_state == 2:
        HM()
        mouse_click = [[-10000,-10000]]

    #cursor_draw(x_pos,y_pos)

#loop until the user clicks the close button.
done = False

#variables/original values
#hangman variables
rand_number = random.randint(0,19)
wordFile = open('Words.txt','r')
cateFile = open('Cates.txt','r')
wordList = wordFile.readlines()
cateList = cateFile.readlines()
word = wordList[rand_number][:-1]
category = cateList[rand_number][:-1]

line1 = ['A','B','C','D','E','F','G','H','I']
line2 = ['J','K','L','M','N','O','P','Q','R']
line3 = ['S','T','U','V','W','X','Y','Z']
letter_list = []
letter_coords = []
wrong_letterlist = []
correct_letterlist = []

cursor_horiz = 0
cursor_vert = 0
selected_letter = 97
validity = 0

#tic tac toe variables
turn = random.randint(1,2)
tile = [0, 0, 0, 0, 0, 0, 0, 0, 0]
o_input = []
x_input = []
o_win = 0
x_win = 0
xo_win = 0
game_done = False
game_history = []

#menu variables
mouse_click = [[-10000,-10000]]
menu_check = True
screen_state = 0
music_mute = True
sound_mute = False
info_screen = False
shutdown_timer = 0

#sound variables
bg_played = False
button_hover_played = False
xohover_played = False
blue_hover_played = False
open_sound = False
close_sound = False

#Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    #get mouse coordinates
    #pygame.mouse.set_visible(False)
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
            mouse_click.insert(0,[x_pos,y_pos])

    #set the screen background colour
    screen.fill(WHITE)

    main()

    if music_mute == False:
        bg_music.set_volume(1)
    elif music_mute == True:
        bg_music.set_volume(0)

    if sound_mute == False:
        button_hover.set_volume(1)
        xo_enter.set_volume(0.5)
        button_press.set_volume(1)
        back_sound.set_volume(1)
        door_open.set_volume(1)
        door_close.set_volume(1)
    elif sound_mute == True:
        button_hover.set_volume(0)
        xo_enter.set_volume(0)
        button_press.set_volume(0)
        back_sound.set_volume(0)
        door_open.set_volume(0)
        door_close.set_volume(0)

    #limit to 30 frames per second
    clock.tick(30)

    #update screen with drawings
    pygame.display.flip()

#idle friendly, anti-hang quit line
pygame.quit()
