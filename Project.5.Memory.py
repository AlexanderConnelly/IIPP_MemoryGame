# implementation of card game - Memory

import simplegui
import random
CWidth=1600
CHeight=150
font_size=80
card_width=CWidth/16
card_pos=[]
state=0
turns=0
for x in range(0,17):
    card_pos.append(card_width*x)

back = simplegui.load_image('http://animals.mom.me/DM-Resize/photos.demandstudios.com/getty/article/97/181/87815878.jpg?w=600&h=600&keep_ratio=1&webp=1')
# helper function to initialize globals
def new_game():
    global hand,exposed,state,perm_exposed,select,turn
    state=0  
    hand=[1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8]
    random.shuffle(hand)
    exposed=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    perm_exposed=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    select=[0,0,0,0]
    turns=0
    #exposed=[1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8]
     
# define event handlers
def mouseclick(pos):
    global exposed,hand,state,perm_exposed,turns,select
    
        
    # add game state logic here
    if state == 0:
        for x in range(0,17):
            if pos[0]>card_pos[x] and pos[0]<card_pos[x+1]:
                exposed[x]=1
                select[0]=hand[x]
                select[1]=x
                state=1
        
        
        
    elif state == 1:
        for x in range(0,17):
            if pos[0]>card_pos[x] and pos[0]<card_pos[x+1] and exposed[x]!=1 and perm_exposed[x]!=1:
                exposed[x]=1
                select[2]=hand[x]
                select[3]=x
                state = 2
    else:
        for x in range(0,17):
            
            if pos[0]>card_pos[x] and pos[0]<card_pos[x+1] and exposed[x]!=1 and perm_exposed[x]!=1:
                state=1
                #test for match
                if select[0]==select[2]:
                    perm_exposed[select[1]]=1
                    perm_exposed[select[3]]=1
                exposed=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]    
                for y in range(0,16):
                    if perm_exposed[y]==1:
                        exposed[y]=1
                
                select[0]=hand[x]
                select[1]=x
                exposed[x]=1
                turns+=1
               
                
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global exposed, hand,font_size
    #draw back of cards first
    for x in range(0,16):
        canvas.draw_image(back,(200,300),(400,600),((CWidth/16-CWidth/32+(CWidth/16)*x),CHeight/2),(CWidth/16,CHeight))
    #draw numbers when called in exposed
    for x in range(0,16):
        if exposed[x]==1:
            canvas.draw_polygon([(card_pos[x],0), (card_pos[x+1], 0), (card_pos[x+1], CHeight),(card_pos[x],CHeight)], 1, 'Green','Green')
            canvas.draw_text(str(hand[x]), (card_pos[x]+CWidth/32-font_size/3,CHeight-CHeight/3),font_size, 'Purple')
    str_turns="Turns =",turns
    label.set_text(str_turns)

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", CWidth, CHeight)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric