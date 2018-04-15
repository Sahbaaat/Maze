
import simplegui
import random

matrix=[[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]
row=0
col=0

for k in range(7):
    i=random.randint(0,3)      #make barriers
    j=random.randint(0,3)
    matrix[i][j]=1
matrix[3][3]=0
matrix[0][0]=0
print( matrix)

#outputs
def lost_handler(canvas):
    canvas.draw_text('You Lost! ', (100, 100), 35, 'Red')
    
def move_handler(canvas):
    global row,col
    i=str(row)
    j=str(col)
    c="column = "+i
    r="row = "+j
    canvas.draw_text(c,(100,100),30,'blue')
    canvas.draw_text(r,(100,70),30,'blue')
    
def win_handler(canvas):
    canvas.draw_text('You Won!', (100, 100), 35, 'green')



def keydown(key): #key_handler
    global matrix,row,col
    if simplegui.KEY_MAP["left"] == key:
        if col>0:
            col=col-1
        if col<4 and col>=0 and row<4 and row>=0 and matrix[row][col]==0:
                frame.set_draw_handler(move_handler)
        else:
            row=0
            col=0
            frame.set_draw_handler(lost_handler)
            
        
    if simplegui.KEY_MAP["right"] == key:
        if col<4:
            col=col+1
        if col<4 and col>=0 and row<4 and row>=0 and matrix[row][col]==0:
                frame.set_draw_handler(move_handler)
        else:
            row=0
            col=0
            frame.set_draw_handler(lost_handler)
            
               
    if simplegui.KEY_MAP["up"] == key:
        if row>0:
            row=row-1
            
        if col<4 and col>=0 and row<4 and row>=0 and matrix[row][col]==0:
                frame.set_draw_handler(move_handler)
        else:
            row=0
            col=0
            frame.set_draw_handler(lost_handler)
            
            
    if simplegui.KEY_MAP["down"] == key:
        if row<4:
            row=row+1
        if col<4 and col>=0 and row<4 and row>=0 and matrix[row][col]==0:
                frame.set_draw_handler(move_handler)
        else:
            row=0
            col=0
            frame.set_draw_handler(lost_handler)
            
            
    if col==3 and row==3:
        frame.set_draw_handler(win_handler)
    
    
                
frame = simplegui.create_frame("Maze", 300, 200)
frame.set_keydown_handler(keydown)

frame.start()