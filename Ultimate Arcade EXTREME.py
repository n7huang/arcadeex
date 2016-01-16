import pygame #import libraries to draw game functions, etc. from
import random
from pygame.locals import *
import sys
import pygame.mixer

#define colours
WHITE    = ( 255, 255, 255)
RED      = ( 255,   0,   0)
GREY     = ( 200, 200, 200)

pygame.init()#initialize game engine
pygame.mixer.init()#initialize sound engine

#set height & width of screen
size = [1000, 600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ultimate Arcade Extreme v1.1")

#---------- Imported Media ----------
#different button states
button_0 = pygame.image.load("images/button_0.png")
button_1 = pygame.image.load("images/button_1.png")
button_2 = pygame.image.load("images/button_2.png")
button_3 = pygame.image.load("images/button_3.png")
button_4 = pygame.image.load("images/button_4.png")
button_5 = pygame.image.load("images/button_5.png")
exit_0 = pygame.image.load("images/exit_0.png")
exit_1 = pygame.image.load("images/exit_1.png")
mute_0 = pygame.image.load("images/mute_0.png")
mute_1 = pygame.image.load("images/mute_1.png")
back_0 = pygame.image.load("images/back_0.png")
back_1 = pygame.image.load("images/back_1.png")
info = pygame.image.load("images/info_button.png")
music_0 = pygame.image.load("images/music_0.png")
music_1 = pygame.image.load("images/music_1.png")
info_bg = pygame.image.load("images/info_screen.png")

#general images
title = pygame.image.load("images/titlecard.png")
cursor = pygame.image.load("images/cursor.png")
bg_img = pygame.image.load("images/bg_image.png")

#tic tac toe images
board = pygame.image.load("images/board.png")
o_tile = pygame.image.load("images/circle.png")
x_tile = pygame.image.load("images/cross.png")
tictactoe = pygame.image.load("images/tictactoetitle.png")
score_bg = pygame.image.load("images/score_bg.png")
score_o = pygame.image.load("images/score_o.png")
score_x = pygame.image.load("images/score_x.png")

#shutdown sequence images
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

#hangman images
hangman = pygame.image.load("images/hangmantitle.png")
hangman_bg = pygame.image.load("images/hangman_bg.png")
gallows = pygame.image.load("images/hang_0.png")
hang_1 = pygame.image.load("images/hang_1.png")
hang_2 = pygame.image.load("images/hang_2.png")
hang_3 = pygame.image.load("images/hang_3.png")
hang_4 = pygame.image.load("images/hang_4.png")
hang_5 = pygame.image.load("images/hang_5.png")
hang_6 = pygame.image.load("images/hang_6.png")
angry_mob = pygame.image.load("images/angry_mob.png")

#letters for hangman keyboard
a_ltr = pygame.image.load("images/A.png")
b_ltr = pygame.image.load("images/B.png")
c_ltr = pygame.image.load("images/C.png")
d_ltr = pygame.image.load("images/D.png")
e_ltr = pygame.image.load("images/E.png")
f_ltr = pygame.image.load("images/F.png")
g_ltr = pygame.image.load("images/G.png")
h_ltr = pygame.image.load("images/H.png")
i_ltr = pygame.image.load("images/I.png")
j_ltr = pygame.image.load("images/J.png")
k_ltr = pygame.image.load("images/K.png")
l_ltr = pygame.image.load("images/L.png")
m_ltr = pygame.image.load("images/M.png")
n_ltr = pygame.image.load("images/N.png")
o_ltr = pygame.image.load("images/O.png")
p_ltr = pygame.image.load("images/P.png")
q_ltr = pygame.image.load("images/Q.png")
r_ltr = pygame.image.load("images/R.png")
s_ltr = pygame.image.load("images/S.png")
t_ltr = pygame.image.load("images/T.png")
u_ltr = pygame.image.load("images/U.png")
v_ltr = pygame.image.load("images/V.png")
w_ltr = pygame.image.load("images/W.png")
x_ltr = pygame.image.load("images/X.png")
y_ltr = pygame.image.load("images/Y.png")
z_ltr = pygame.image.load("images/Z.png")

#sounds
bg_music = pygame.mixer.Sound("audio/unconditional.ogg")
back_sound = pygame.mixer.Sound("audio/back_button.ogg")
button_hover = pygame.mixer.Sound("audio/button_hover.ogg")
button_press = pygame.mixer.Sound("audio/button_press.ogg")
blue_button = pygame.mixer.Sound("audio/soundonoff.ogg")
entry = pygame.mixer.Sound("audio/xopress.ogg")
door_open = pygame.mixer.Sound("audio/door_open.ogg")
door_close = pygame.mixer.Sound("audio/door_close.ogg")
beep = pygame.mixer.Sound("audio/beep.ogg")

#---------- Functions ----------
#----- Main Menu -----
def cursor_draw(x,y):
    #draws cursor at mouse position
    screen.blit(cursor,[x,y])

def button_draw(x,y):
    #draws main game buttons and exit/back button depending on screen state
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

    #draws hover states of buttons & plays button sounds
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

    #back button
    elif menu_check == False:
        if 100 >= x >= 0 and y >= 545:
            screen.blit(back_1,[0,545])
        else:
            screen.blit(back_0,[0,545])

def press_check(x_click,y_click):
    #checks which game button is pressed & determines which game to play
    global screen_state
    if 400 >= x_click >= 200 and 450 >= y_click >= 350 and menu_check == True:
        button_press.play()
        mouse_click.insert(0,[-10000,-10000])
        screen_state = 1
    elif 800 >= x_click >= 600 and 450 >= y_click >= 350 and menu_check == True:
        button_press.play()
        mouse_click.insert(0,[-10000,-10000])
        screen_state = 2

def reset_check(x,y):
    #determines which game to reset the board for & runs appropriate reset function
    if screen_state == 1:
        if 795 >= x >= 595 and 475 >= y >= 375:
            button_press.play()
            reset_TTT()
    elif screen_state == 2:
        if 215 <= x <= 404 and 425 <= y <= 488:
            button_press.play()
            reset_HM()
            mouse_click.insert(0,[-10000,-10000])

def exit_check(x,y):
    #on main menu: checks for a click on the exit button, returns a True value
    #in game screens: checks for a click on the back button, resets games completely
    global screen_state, menu_check, close_sound
    if menu_check == True:
        if x >= 950 and y >= 550:
            if close_sound == False:
                door_close.play()
                close_sound = True
            return True
    elif menu_check == False:
        if 100 >= x >= 0 and y >= 545:
            highscore_update()
            back_sound.play()
            menu_check = True
            screen_state = 0
            reset_TTT()
            reset_HM()
            score_reset()

def highscore_update():
    #increments highscore values
    highscore_read = open('highscores.txt','r')
    highscore_lst = highscore_read.readlines()
    highscore_write = open('highscores.txt','w')
    highscore_write.write(str(int(highscore_lst[0][:-1])+o_win)+"\n"+\
                          str(int(highscore_lst[1][:-1])+x_win)+"\n"+\
                          str(int(highscore_lst[2][:-1])+tie_game)+"\n")
    highscore_write.close()
    hshm_file = open('highscore_hm.txt','r')
    hshm = hshm_file.read()
    init_hs = int(hshm)
    if hangman_hs > init_hs:
        hmhs_file = open('highscore_hm.txt','w')
        hmhs_file.write(str(hangman_hs))
        hmhs_file.close()

def music_button(x,y):
    #toggles music button state and music mute/on
    global music_mute
    if music_mute == False:
        screen.blit(music_0,[950,1])
    elif music_mute == True:
        screen.blit(music_1,[950,1])
    if x >= 950 and 1 < y <= 50:
        music_mute = not(music_mute)
        blue_button.play()
        mouse_click.insert(0,[-10000,-10000])

def sound_button(x,y):
    #toggles sound button state and sound mute/on
    global sound_mute
    if sound_mute == False:
        screen.blit(mute_0,[890,1])
    elif sound_mute == True:
        screen.blit(mute_1,[890,1])
    if 940 >= x >= 890 and 1 < y <= 50:
        sound_mute = not(sound_mute)
        blue_button.play()
        mouse_click.insert(0,[-10000,-10000])

def info_button(x,y):
    #sets screen state to output the info on screen
    global screen_state
    if screen_state == 0:
        screen.blit(info,[830,1])
        if 880 >= x >= 830 and 5 < y <= 50:
            blue_button.play()
            mouse_click.insert(0,[-10000,-10000])
            screen_state = 3

def sound_player():
    #plays background music so that it doesn't overlap itself 60 times/sec
    global bg_played
    if bg_played == False:
        bg_music.play(-1)
        bg_played = True

def shut_down():
    #shutdown pseudo-animation
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

#----- Tic Tac Toe -----
def board_draw():
    #blits tictactoe board
    screen.blit(board,[135,80])

def mouse_hover(x_hover,y_hover,x_click,y_click):
    #blits an x or o on the area where the cursor is hovered over depending on the turn
    global turn, tile, xohover_played
    for y in range (3):
        for x in range(3):
            if 263+x*133 > x_hover > 135+x*133 and 208+y*133 > y_hover > 80+y*133 and tile[y*3+x] == 0:
                if turn == 1:
                    screen.blit(o_tile,[143+x*133,88+y*133])
                elif turn == 2:
                    screen.blit(x_tile,[143+x*133,88+y*133])

    #adds coordinates to a list when mouse is clicked in an available spot on the board & changes turn
            if 263+x*133 > x_click > 135+x*133 and 208+y*133 > y_click > 80+y*133 and turn == 1 and tile[y*3+x] == 0:
                entry.play()
                o_input.append([143+x*133,88+y*133])
                mouse_click.insert(0,[-10000,-10000])
                tile[y*3+x] = 1
                turn = 2
            elif 263+x*133 > x_click > 135+x*133 and 208+y*133 > y_click > 80+y*133 and turn == 2 and tile[y*3+x] == 0:
                entry.play()
                x_input.append([143+x*133,88+y*133])
                mouse_click.insert(0,[-10000,-10000])
                tile[y*3+x] = -1
                turn = 1

def xo_draw(o_input,x_input):
    #blitz Xs and Os using coordinates from the list created in mouse_hover()
    for entry in o_input:
        screen.blit(o_tile,[entry[0],entry[1]])
    for entry in x_input:
        screen.blit(x_tile,[entry[0],entry[1]])

def win_check():
    #checks from list of possible outcomes of wins for a win, returns a value depending on outcome
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
    #increments score depending on value returned from win_check()
    global o_win, x_win, tie_game, tile, game_done
    if win_check() == "o":
        o_win += 1
        game_history.insert(0,"O WIN")
    elif win_check() == "x":
        x_win += 1
        game_history.insert(0,"X WIN")
    elif win_check() == "tie":
        tie_game += 1
        game_history.insert(0,"CATS")
    tile = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    game_done = True

def keep_playing(x,y):
    #activates the play again? button that runs reset_check()
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

def reset_TTT():
    #resets all tic tac toe variables for the next game of the session
    global turn, tile, o_input, x_input, game_done
    turn = random.randint(1,2)
    tile = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    o_input = []
    x_input = []
    game_done = False

def score_reset():
    #resets the score, for both tic tac toe and hangman; keeps sessions separate
    global o_win, x_win, tie_game, game_history, words_guessed, words_shown
    o_win = 0
    x_win = 0
    tie_game = 0
    game_history = []
    words_guessed = 0
    words_shown = 0

def score_blit():
    #blits the current scores of the session, and the result of the previous game
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

#----- Hangman -----
#Drawn objects
def hanger():
    #blits the gallows to the screen, as well as the play again? button
    screen.blit(gallows,[152,223])
    screen.blit(hangman_bg,[145,60])
    screen.blit(hangman,[145,60])
    screen.blit(angry_mob,[200,310])
    screen.blit(button_3,[215,425])
    font = pygame.font.SysFont('Courier New', 22, True, False)
    text = font.render("PLAY AGAIN?",True,GREY)
    screen.blit(text, [239,445])

def lines(line_number):
    #draws the lines for the unknown word based on the length of the word
    for x_offset in range(0,line_number*45,45):
        pygame.draw.line(screen,WHITE,[490+x_offset,160],[520+x_offset,160],3)

def highlighter(letter_horiz,letter_vert):
    #draws the selector for the letters, controlled by arrowkeys
    pygame.draw.rect(screen,RED,[460 + letter_horiz,390 + letter_vert,45,45])

def letters():
    #blits letters for the keyboard to the screen
    for i in range(0,9):
        screen.blit(line1[i], [460+(45 * i),390])
        screen.blit(line2[i], [460+(45 * i),435])
    for i in range(0,8):
        screen.blit(line3[i], [460+(45 * i),480])

#Drawing functions
def human_drawer():
    #blitz different body parts of the man based on number of incorrect letters
    if len(wrong_letterlist) == 1:
        screen.blit(hang_1,[152,223])
    elif len(wrong_letterlist) == 2:
        screen.blit(hang_2,[152,223])
    elif len(wrong_letterlist) == 3:
        screen.blit(hang_3,[152,223])
    elif len(wrong_letterlist) == 4:
        screen.blit(hang_4,[152,223])
    elif len(wrong_letterlist) == 5:
        screen.blit(hang_5,[152,223])
    elif len(wrong_letterlist) == 6:
        screen.blit(hang_6,[152,223])

def cate_drawer():
    #blits the category of the word to the screen
    font = pygame.font.SysFont('Courier New', 25, True, False)
    text = font.render("Category: "+ category,True,WHITE)
    screen.blit(text, [525, 80])

def letter_drawer(letter,positions):
    #blits the correct letters in the word over the lines
    for i in range(len(letter_coords)):
        font = pygame.font.SysFont('Courier New', 30, True, False)
        text = font.render(letter,True,WHITE)
        screen.blit(text, [497+(45*positions), 130])

def strikethru():
    #draws a line through already selected letters
    for point in selected:
        pygame.draw.line(screen,WHITE,[463+point[0],410+point[1]],[502+point[0],410+point[1]],7)

#Logic functions
def incorrect_letters():
    #blits the incorrect letters chosen to the screen
    font = pygame.font.SysFont('Courier New', 25, True, False)
    text = font.render("Incorrect Letters:",True,WHITE)
    screen.blit(text, [487, 290])
    for i in range(len(wrong_letterlist)):
        text = font.render(wrong_letterlist[i],True,WHITE)
        screen.blit(text, [505+(60*i), 325])

def score_keeper():
    #blits the score of correct words guessed over the number of words presented
    if len(correct_letterlist) != len(word) and len(wrong_letterlist) != 6:
        font = pygame.font.SysFont('Courier New', 25, True, False)
        if words_shown == 0:
            text = font.render("First word of session.",True,WHITE)
            screen.blit(text, [487, 220])
        else:
            text = font.render("Words guessed: "+str(words_guessed)+"/"+str(words_shown),True,WHITE)
            screen.blit(text, [487, 220])

def letter_checker():
    #checks if the chosen letter is correct or not
    no_word = 0
    for i in range(len(word)):
        if chr(selected_letter) == word[i]:
            letter_coords.append([word[i],i])
            correct_letterlist.append(chr(selected_letter))
        else:
            no_word += 1
    if no_word == len(word) and len(wrong_letterlist) < 6:
        wrong_letterlist.append(chr(selected_letter))

#End game functions
def victory():
#Displays a congratulations screen if the user won
    global words_guessed, words_shown, word_done
    font = pygame.font.SysFont('Courier New', 25, True, False)
    text = font.render('Congratulations!',True,WHITE)
    screen.blit(text, [487, 220])
    text = font.render('You\'ve guessed the word!',True,WHITE)
    screen.blit(text, [487, 250])
    if word_done == False:
        words_guessed += 1
        words_shown += 1
        word_done = True

def lose():
#Displays loss screen if the user lost
    global words_shown, word_done
    font = pygame.font.SysFont('Courier New', 25, True, False)
    text = font.render('Oh no! You were hung!',True,WHITE)
    screen.blit(text, [487, 220])
    text = font.render('The word was: '+word,True,WHITE)
    screen.blit(text, [487,250])
    if word_done == False:
        words_shown += 1
        word_done = True

def reset_HM():
#Resets all variables and the game
    global rand_number,word,category,letter_list,letter_coords,wrong_letterlist,\
    correct_letterlist,cursor_horiz,cursor_vert,selected_letter,validity,no_word,\
    selected, word_done
    rand_number = random.randint(0,49)
    word = wordList[rand_number][:-1]
    category = cateList[rand_number][:-1]
    letter_list = []
    letter_coords = []
    wrong_letterlist = []
    correct_letterlist = []
    selected = []
    cursor_horiz = 0
    cursor_vert = 0
    selected_letter = 97
    validity = 0
    no_word = 0
    word_done = False

def end_screen(x,y):
#Creates a button at the end of the game that when pressed runs the reset_HM function
    global button_hover_played, hangman_hs
    if len(correct_letterlist) == len(word):
        victory()
        screen.blit(button_4,[215,425])
    elif len(wrong_letterlist) == 6:
        lose()
        screen.blit(button_4,[215,425])
    if word_done == True:
        if words_shown > 0:
            if words_guessed/words_shown == 1:
                hangman_hs = words_guessed
        screen.blit(button_4,[215,425])
        font = pygame.font.SysFont('Courier New', 22, True, False)
        text = font.render("PLAY AGAIN?",True,WHITE)
        screen.blit(text, [239,445])
        if 404 >= x >= 215 and 488 >= y >= 425:
            if button_hover_played == False:
                button_hover.play()
                button_hover_played = True
            screen.blit(button_5,[215,425])
            text = font.render("PLAY AGAIN?",True,WHITE)
            screen.blit(text, [239,445])
        else:
            button_hover_played = False
        reset_check(mouse_click[0][0],mouse_click[0][1])

def main_menu():
#calls main functions
    button_draw(x_pos,y_pos)
    music_button(mouse_click[0][0],mouse_click[0][1])
    sound_button(mouse_click[0][0],mouse_click[0][1])
    sound_player()
    info_button(mouse_click[0][0],mouse_click[0][1])

def TTT():
#calls functions for and runs the Tic Tac Toe game
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
#calls functions for and runs the Hangman game
    global menu_check
    menu_check = False
    hanger()
    human_drawer()
    highlighter(cursor_horiz,cursor_vert)
    cate_drawer()
    letters()
    lines(len(word))
    for i in range(len(letter_coords)):
        letter_drawer(letter_coords[i][0],letter_coords[i][1])
    incorrect_letters()
    score_keeper()
    strikethru()
    end_screen(x_pos,y_pos)

def info_show():
#Displays the information for the game
    global menu_check
    menu_check = False
    for i in range (len(info_list)):
        if i == 0:
            font = pygame.font.SysFont('Courier New', 20, True, False)
            text = font.render(info_list[i][:-1],True,WHITE)
            screen.blit(text,[310, 100])
        else:
            font = pygame.font.SysFont('Courier New', 13, True, False)
            text = font.render(info_list[i][:-1],True,WHITE)
            screen.blit(text,[235,125+i*17])
    font = pygame.font.SysFont('Courier New', 20, True, False)
    text = font.render("History of Tic Tac Toe Games:      Hangman Highscore:",True,WHITE)
    screen.blit(text,[150, 370])
    highscore_read = open('highscores.txt','r')
    highscore_lst = highscore_read.readlines()
    for i in range (len(highscore_lst)):
        text = font.render(highscore_lst[i][:-1],True,WHITE)
        screen.blit(text,[150,395+i*25])
    hshm_file = open('highscore_hm.txt','r')
    hshm = hshm_file.read()
    text = font.render(hshm,True,WHITE)
    screen.blit(text,[570,395])
    text = font.render("O WINS",True,WHITE)
    screen.blit(text,[190,395])
    text = font.render("X WINS",True,WHITE)
    screen.blit(text,[190,420])
    text = font.render("TIES",True,WHITE)
    screen.blit(text,[190,445])
    text = font.render("WORDS IN A ROW",True,WHITE)
    screen.blit(text,[610,395])
    highscore_reset(x_pos,y_pos,mouse_click[0][0],mouse_click[0][1])

def highscore_reset(x,y,x_click,y_click):
#Resets the high score on button press in info screen
    global button_hover_played, hangman_hs
    screen.blit(button_4,[570,430])
    font = pygame.font.SysFont('Courier New', 15, True, False)
    text = font.render("RESET HIGHSCORES",True,WHITE)
    screen.blit(text, [594,454])
    if 759 >= x >= 570 and 493 >= y >= 430:
        if button_hover_played == False:
                button_hover.play()
                button_hover_played = True
        screen.blit(button_5,[570,430])
        screen.blit(text, [594,454])
    else:
        button_hover_played = False
    if 759 >= x_click >= 570 and 493 >= y_click >= 430:
        button_press.play()
        highscore_write = open('highscores.txt','w')
        highscore_write.write("0\n"+\
                              "0\n"+\
                              "0\n")
        highscore_write.close()
        hmhs_file = open('highscore_hm.txt','w')
        hmhs_file.write("0")
        hmhs_file.close()
        hangman_hs = 0
        mouse_click.insert(0,[-10000,-10000])

def main():
#Main function of the game; calls every other function
    global menu_check, mouse_click, screen_state
    print rand_number
    screen.blit(bg_img,[0,0])
    main_menu()
    done = exit_check(mouse_click[0][0],mouse_click[0][1])
    if done == True:
        shut_down()
    if screen_state == 0:
        press_check(mouse_click[0][0],mouse_click[0][1])
    elif screen_state == 1:
        TTT()
        mouse_click = [[-10000,-10000]]
    elif screen_state == 2:
        HM()
        mouse_click = [[-10000,-10000]]
    elif screen_state == 3:
        info_show()
    cursor_draw(x_pos,y_pos)

#---------- Variables ----------
#loop until the user clicks the close button.
done = False

#variables/original values
#hangman variables
#Picks a random word and corresponding category
##rand_number = random.randint(0,49)
rand_number = 28
wordFile = open('Words.txt','r')
cateFile = open('Cates.txt','r')
wordList = wordFile.readlines()
cateList = cateFile.readlines()
word = wordList[rand_number][:-1]
category = cateList[rand_number][:-1]

selected = []
#Letters on the virtual keyboard
line1 = [a_ltr,b_ltr,c_ltr,d_ltr,e_ltr,f_ltr,g_ltr,h_ltr,i_ltr]
line2 = [j_ltr,k_ltr,l_ltr,m_ltr,n_ltr,o_ltr,p_ltr,q_ltr,r_ltr]
line3 = [s_ltr,t_ltr,u_ltr,v_ltr,w_ltr,x_ltr,y_ltr,z_ltr]
#Tracks letters that were already used
letter_list = []
#Stores correct letters and which line they will be drawn on
letter_coords = []
#Stores all incorrectly guessed letters
wrong_letterlist = []
#Stores all correctly guessed letters
correct_letterlist = []
#Determines the position of the highlighter function
cursor_horiz = 0
cursor_vert = 0
#Stores the current letter's ASCII number
selected_letter = 97
#Determines whether a letter is usable or not
validity = 0
#Tracks how many letters were guessed
words_guessed = 0
words_shown = 0
#Determines if the word is done
word_done = False

#keeps track of a hangman session's highscore
hangman_hs = 0

#tic tac toe variables
turn = random.randint(1,2)
tile = [0, 0, 0, 0, 0, 0, 0, 0, 0]
o_input = []
x_input = []
o_win = 0
x_win = 0
tie_game = 0
game_done = False
game_history = []

#menu variables
mouse_click = [[-10000,-10000]]
menu_check = True
screen_state = 0
music_mute = True
sound_mute = False
shutdown_timer = 0
info_file = open('info.txt','r')
info_list = info_file.readlines()

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
    pygame.mouse.set_visible(False)
    pos = pygame.mouse.get_pos()
    x_pos = pos[0]
    y_pos = pos[1]

# ----- Main Event Loop -----
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if word_done == False and screen_state == 2:
                #Moves the letter cursor to the right
                if (event.key == K_RIGHT) and cursor_horiz < 360 and selected_letter != 122:
                    beep.play()
                    cursor_horiz += 45
                    selected_letter += 1
                #Moves the letter cursor to the left
                elif (event.key == K_LEFT) and cursor_horiz > 0:
                    beep.play()
                    cursor_horiz -= 45
                    selected_letter -= 1
                #Moves the letter cursor down
                elif (event.key == K_DOWN) and cursor_vert < 90 and selected_letter != 114:
                    beep.play()
                    cursor_vert += 45
                    selected_letter += 9
                #Moves the letter cursor up
                elif (event.key == K_UP) and cursor_vert > 0:
                    beep.play()
                    cursor_vert -= 45
                    selected_letter -= 9
                #Enters the letter currently being hovered over to the list of used letters
                elif (event.key == K_RETURN):
                    entry.play()
                    for i in range(len(letter_list)):
                        if chr(selected_letter) == letter_list[i]:
                            validity += 1
                    if validity == 0:
                        letter_list.append(chr(selected_letter))
                        letter_checker()
                    validity = 0
                    selected.append([cursor_horiz,cursor_vert])
        #Enters the current coordinates of the mouse cursor
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_click.insert(0,[x_pos,y_pos])

    #set the screen background colour
    screen.fill(WHITE)

    #calls main function
    main()

    #setting volumes if mute or not
    if music_mute == False:
        bg_music.set_volume(1)
    elif music_mute == True:
        bg_music.set_volume(0)

    if sound_mute == False:
        button_hover.set_volume(1)
        entry.set_volume(0.5)
        button_press.set_volume(1)
        back_sound.set_volume(1)
        door_open.set_volume(1)
        door_close.set_volume(1)
        blue_button.set_volume(1)
        beep.set_volume(1)
    elif sound_mute == True:
        button_hover.set_volume(0)
        entry.set_volume(0)
        button_press.set_volume(0)
        back_sound.set_volume(0)
        door_open.set_volume(0)
        door_close.set_volume(0)
        blue_button.set_volume(0)
        beep.set_volume(0)

    #limit to 30 frames per second
    clock.tick(30)

    #update screen with drawings
    pygame.display.flip()

#idle friendly, anti-hang quit line
pygame.quit()
