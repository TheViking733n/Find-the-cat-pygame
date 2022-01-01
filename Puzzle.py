# -*- coding: utf-8 -*-
"""
Created on Sat Nov 9 00:51:17 2019

@author: ANANT PRAKASH SINGH
"""


import pygame
import time


#Resolution
res_x, res_y = 1366, 768
run_fulscreen = False

ct = .25  #Coef. of wait time (This will increase or decrease delays in the game)


#Color codes
white,blue,navy_blue,green,dark_green,red,dark_red,black,orange,yellow,grey,dark_grey,brown=(255,255,255),(0,0,255),(0,0,100),(0,255,0),(0,50,0),(255,0,0),(250,50,50),(0,0,0),(255,100,10),(255,255,0),(200,200,200),(100,100,100),(100,40,0)





#Global Variables declaration and initilisation
MOVE = ""
ANSWER = ""


#Coordinates declaration and initilisation
unit = res_y/165
gap = 15*unit
sky = 100*unit
brh = 12*unit
block_w, block_h, block_c = 21*unit, 4*unit   , dark_grey
pit_w  , pit_h  , pit_c   = 15*unit, 18*unit  , black
grass_w, grass_h, grass_c = res_x  , 2*unit   , dark_green
soil_w , soil_h , soil_c  = res_x  , res_y-sky, brown
graph_x = [75*unit+(res_x-75*unit)*i/11 for i in range(11)]
graph_y = [30*unit, 45*unit, 60*unit]
line_c = [red,yellow,green]
dark_line_c = [dark_red,orange,dark_green]
greet_msg=["You failed to find the cat in " +str(len(MOVE))+ " days", "", "", "", "", "", "PERFECT!!!    You traced the CAT in 6 days", "NICE !!!    You traced the CAT in 7 days.  Try to reduce your solution", "NICE!!!    You traced the CAT in 8 days.  Try to reduce your solution", "Not Bad...    You traced the CAT in 9 days.  Try to reduce your solution", "Not Bad...    You traced the CAT in 10 days.  Try to reduce your solution", ]


#Initilising pygame and defining objects
pygame.init()
if run_fulscreen:
    gameDisplay = pygame.display.set_mode((res_x,res_y),pygame.FULLSCREEN)
else:
    gameDisplay = pygame.display.set_mode((res_x,res_y))
pygame.display.set_caption("PUZZLE")


#Configuring Fonts
min_font = res_y/40
font = [ pygame.font.SysFont(None,int(min_font*i)) for i in range(1,11) ]
def print_txt(x_pos,y_pos,msg,color,height):
    #font = pygame.font.SysFont(None,height)
	screen_text=font[height-1].render(msg,True,color)
	gameDisplay.blit(screen_text,[int(x_pos),int(y_pos)])
	pygame.display.update()


#Defining Functions
def draw(x,y,w,h,col):
    gameDisplay.fill(col,rect=[x,y,w,h])
    
def clear():
    draw(0,0,res_x,res_y,black)
    pygame.display.update()

def pit_x(n):
    return ((0.5)*res_x+(n-3)*gap+(n-3.5)*pit_w)

def pit_y(n):
    return sky

def block_x(n):
    return ((0.5)*(res_x-block_w)+(n-3)*(gap+pit_w))

def block_y(n):
    return (sky-block_h)

def draw_pit(n):
    draw(pit_x(n),pit_y(n),pit_w,pit_h,pit_c)
    l=pit_w-4
    x1, y1 = pit_x(n)+2, pit_y(n)+pit_h-1
    while l>0:
        draw(x1,y1,l,1,pit_c)
        x1+=2
        y1+=1
        l-=4
    pygame.display.update()

def draw_block(n):
    draw(block_x(n),block_y(n),block_w,block_h,block_c)
    pygame.display.update()

def draw_background():
    draw(0,sky,soil_w,soil_h,soil_c)
    draw(0,sky,grass_w,grass_h,grass_c)
    for i in range(1,6):
        draw_pit(i)
        draw_block(i)
        print_txt(pit_x(i)+0.5*pit_w-2*unit, pit_y(i)+1.2*pit_h,str(i),block_c,3)
        print_questionmark(i)
    print_txt(res_x/2-50*unit, res_y-8*unit,"CREDITS: ANANT PRAKASH SINGH",black,2)
    pygame.display.update()
        
def block_up(n):
    for i in range(1,int(brh)+1):
        draw(block_x(n),block_y(n)-i+1,block_w,block_h,black)
        draw(block_x(n),block_y(n)-i,block_w,block_h,block_c)
        pygame.display.update()
        time.sleep(.5*ct/brh)
    pygame.display.update()

def block_down(n):
    draw(pit_x(n)-0.75*gap,block_y(n)-block_h,pit_w+1.5*gap,2*block_h-unit,black) #Erasing "No CAT!" or "CAT Found!" message
    for i in range(1,int(brh)+1):
        draw(block_x(n),block_y(n)-int(brh)+i-1,block_w,block_h,black)
        draw(block_x(n),block_y(n)-int(brh)+i,block_w,block_h,block_c)
        pygame.display.update()
        time.sleep(.125*ct/brh)
    pygame.display.update()

def draw_cat(n):
    draw_pit(n)
    print_txt(pit_x(n)+0.5*pit_w-2*unit, pit_y(n)+0.5*pit_h-6*unit,"C",yellow,2)
    print_txt(pit_x(n)+0.5*pit_w-2*unit, pit_y(n)+0.5*pit_h,"A",yellow,2)
    print_txt(pit_x(n)+0.5*pit_w-2*unit, pit_y(n)+0.5*pit_h+6*unit,"T",yellow,2)

def write_info1():
    puz0 = "PUZZLE"
    puz1 = "A cat is in any of the 5 pits as shown below. The cat's specialty is that she changes the pit every night"
    puz2 = "by moving to the pit adjacent to her pit. The question is, if given a chance to see a pit once a day,"
    puz3 = "how many days will it take to trace the cat's pit?"
    puz4 = ""
    puz5 = "Press any key to continue..."
    print_txt((res_x/2)-37*unit,7*unit,puz0,red,6)
    print_txt(7*unit,30*unit,puz1,green,2)
    print_txt(7*unit,40*unit,puz2,green,2)
    print_txt(7*unit,50*unit,puz3,green,2)
    print_txt(7*unit,60*unit,puz4,green,2)
    print_txt(7*unit,70*unit,puz5,blue,2)
    pygame.display.update()
    
def write_info2():
    info1 = "Press 1,  2,  3,  4 or 5 to open respective pit.   Press Space Bar to end Puzzle and see Cat's position."
    info2 = "Press R to Retry and Esc to Exit."
    info3 = "DAY"
    info4 = "Cat's Position"
    info5 = "Your Move"
    print_txt(10*unit,8*unit,info1,blue,2)
    print_txt(10*unit,16*unit,info2,blue,2)
    print_txt(10*unit,30*unit,info3,red,3)
    print_txt(10*unit,45*unit,info4,yellow,3)
    print_txt(10*unit,60*unit,info5,green,3)
    #Printing Colons
    print_txt(graph_x[0],graph_y[0],":",line_c[0],3)
    print_txt(graph_x[0],graph_y[1],":",line_c[1],3)
    print_txt(graph_x[0],graph_y[2],":",line_c[2],3)
    #Printing day no.
    for i in range(1,11):
        print_txt(graph_x[i],graph_y[0],str(i),line_c[0],3)
    pygame.display.update()

def print_questionmark(n):
    print_txt(pit_x(n)+0.5*pit_w-2*unit, pit_y(n)+0.5*pit_h,"?",yellow,3)
    pygame.display.update()

def print_nocat(n):
    draw_pit(n) #Erasing Question Mark
    print_txt(pit_x(n)+0.5*pit_w-12*unit, pit_y(n)-8*unit,"No  CAT!",yellow,2)
    pygame.display.update()

def print_catfound(n):
    draw_pit(n) #Erasing Question Mark
    print_txt(pit_x(n)+0.5*pit_w-17*unit, pit_y(n)-8*unit,"CAT  Found!",yellow,2)
    pygame.display.update()
    
def earse_graph_pos(x,y):
    draw(graph_x[x],graph_y[y],5*unit,12*unit,black)

def greetings(n):
    global MOVE
    global ANSWER
    global greet_msg
    greet_msg[0]="You failed to find the cat in " +str(len(MOVE))+ " days"
    print_txt(8*unit,8*unit,greet_msg[n],blue,3)
    pygame.display.update()

def check(move):
    n=len(move)
    ans=""
    for i in range(1,6):
        ans=str(i)
        if ans==move[0]:
            continue
        for j in range(2**(n-1)):
            ans=str(i)
            b=bin(j)
            b=b[2:]
            b="0"*(n-1-len(b))+b
            for k in range(n-1):
                #Checking boundary
                if ans[k]=="1" and b[k]=="0" or ans[k]=="5" and b[k]=="1":
                    break
                num=int(ans[-1])
                if b[k]=="0":
                    ans+=str(num-1)
                if b[k]=="1":
                    ans+=str(num+1)
                #Comparing ans and move
                if move[k+1]==ans[k+1]:
                    break
            else:
                return ans

def askmove(): #returns "1", "2", "3", "4", "5", " ", "R" and "Esc"
    #Asking move
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_1 or event.key==pygame.K_KP1:
                    return "1"
                if event.key==pygame.K_2 or event.key==pygame.K_KP2:
                    return "2"
                if event.key==pygame.K_3 or event.key==pygame.K_KP3:
                    return "3"
                if event.key==pygame.K_4 or event.key==pygame.K_KP4:
                    return "4"
                if event.key==pygame.K_5 or event.key==pygame.K_KP5:
                    return "5"
                if event.key==pygame.K_SPACE:
                    return " "
                if event.key==pygame.K_r:
                    return "R"
                if event.key==pygame.K_ESCAPE:
                    return "Esc"


def processmove(): #NOTE: Call this function only if len(MOVE)<=9
    #This function updates MOVE and ANSWER value, prints "?" and keypressed, move blocks up and down, and prints "No CAT!" or "CAT Found!" message
    global MOVE
    global ANSWER
    dayno=len(MOVE)+1
    print_txt(graph_x[dayno],graph_y[1],"?",line_c[1],3)
    print_txt(graph_x[dayno],graph_y[2],"_",line_c[2],3)
    pygame.display.update()
    keypressed=askmove()
    if keypressed in ["1","2","3","4","5"]:
        MOVE+=keypressed
        print_txt(graph_x[dayno],graph_y[2],keypressed,line_c[2],3)
        if dayno!=1:
            block_down(int(MOVE[-2]))
            print_questionmark(int(MOVE[-2]))
        block_up(int(keypressed))
        pygame.display.update()
        ANSWER=check(MOVE)
        if ANSWER==None:
            print_catfound(int(keypressed))
        else:
            print_nocat(int(keypressed))
        pygame.display.update()
    else:
        return keypressed

def gamestart():
    global MOVE
    global ANSWER
    MOVE=""
    ANSWER=""
    clear()
    draw_background()
    write_info2()
    
    for dayno in range(1,11):
        processmove_output=processmove()
        if processmove_output==" ":
            break
        elif processmove_output=="R":
            return
        elif processmove_output=="Esc":
            pygame.quit()
            quit()
        elif processmove_output==None:
            #This code will be executed when keypressed is "1", "2", "3", "4" or "5"
            #Checking CAT is caught or not
            if ANSWER==None:
                #CAT is caught
                break
    #This code is outside for loop and will be executed when 10 days are over or Space bar is pressed or CAT is caught
    #Checking if Space bar is pressed on first day or what
    if MOVE=="":
        return
    gameend()
    #Game will restart when flow of control reaches here
    return

def showcatpos():
    global MOVE
    global ANSWER
    #Checking CAT is caught or not
    if ANSWER==None:
        ANSWER=check(MOVE[:-1])+MOVE[-1]
    #Erasing Question Marks
    draw(graph_x[1],graph_y[1],res_x-graph_x[1],12*unit,black)
    for i in range(1,6):
        draw_pit(i)
    #Drawing CAT in pit
    draw_cat(int(ANSWER[-1]))
    #Writing CAT Moves
    for i in range(len(ANSWER)):
        print_txt(graph_x[i+1],graph_y[1],ANSWER[i],line_c[1],3)
    pygame.display.update()

def pressanykeytocont():
    keypressed=False
    while not keypressed:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                keypressed=True

def showreplay():
    global MOVE
    global ANSWER
    global ct
    ct=ct/2
    #Preparing for replay
    block_down(int(MOVE[-1]))
    print_questionmark(int(MOVE[-1]))
    draw(graph_x[1],graph_y[1],res_x-75*unit,80*unit-graph_y[1],black) #Erasing CAT's and Player's Moves
    for i in range(1,6):
        draw_pit(i)
    pygame.display.update()
    #Starting replay loop
    for i in range(len(MOVE)):
        #For CAT
        print_txt(graph_x[i+1],graph_y[1],ANSWER[i],line_c[1],3)
        draw_cat(int(ANSWER[i]))
        if i!=0:
            draw_pit(int(ANSWER[i-1])) #Erasing CAT
        pygame.display.update()
        #for event in pygame.event.get():
        #    if event.type==pygame.QUIT:
        #        pygame.quit()
        #        quit()
        #pygame.display.update()
        #time.sleep(10*ct)
        
        #For Player
        print_txt(graph_x[i+1],graph_y[2],MOVE[i],line_c[2],3)
        if i!=0:
            block_down(int(MOVE[i-1])) #Calling block_down()
        block_up(int(MOVE[i]))
        #if ANSWER[i]!=MOVE[i]:
        #    print_nocat(int(MOVE[i]))
        #else:
        #    print_catfound(int(MOVE[i]))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()
        time.sleep(10*ct)
    print_txt(8*unit,20*unit,"FACT: The CAT can be traced in minimum of 6 days.   Press any key to restart game...",green,2)
    pygame.display.update()
    pressanykeytocont()
    return

def gameend():
    global MOVE
    global ANSWER
    #Erasing info2
    draw(0,0,res_x,29*unit,black)
    print_txt(8*unit,8*unit,"Press R to see replay or press Space Bar to skip replay...",green,2)
    pygame.display.update()
    catcaught=ANSWER==None #Below function call will change the value of ANSWER if it is None
    showcatpos()
    pygame.display.update()
    while True:
        askmove_output=askmove()
        if askmove_output==" ":
            return
        if askmove_output=="R":
            #Checking CAT is caught or not
            if catcaught:
                draw(0,0,res_x,29*unit,black)
                greetings(len(MOVE))
            else:
                draw(0,0,res_x,29*unit,black)
                greetings(0)
            pygame.display.update()
            showreplay()
            return


        
        
        
        
        

#-----------------------------------------------------------------------------
#                               _main_
#-----------------------------------------------------------------------------
MOVE=""
ANSWER=""
draw_background()
write_info1()
pressanykeytocont()
while True:
    gamestart()            
    

pygame.quit()
