import pygame

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
RED = (200,0 ,0)
WINDOW_HEIGHT = 480
WINDOW_WIDTH = 480
blockSize = 60 #Set the size of the grid block
global z; global zs; global skips; global ss; global step; global x,y


def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    while True:
        drawer(1,1,8,6)#input X1 , Y1 , X2 , Y2
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

def drawGrid():
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)

def ploter(x,y):
    plot = pygame.Rect((x-1)*blockSize, (y-1)*blockSize, blockSize, blockSize)
    pygame.draw.rect(SCREEN, RED, plot)

def zvalue(px,py):
    z=0
    if(px>py):
        while(px>0):
            px=px-py;z=z+1
    elif(py>px):
        while(py>0):
            py=py-px;z=z+1
    return z

def skipvalue(px,py,oz):
    skip = 0
    if(px>py):
        sub=py-oz ; skip = abs(oz-sub)
    elif(py>px):
        sub=px-oz ; skip = abs(oz-sub)
    return skip

def steps(dirx,diry,gors):
    global x,y,step,skips,ss,z,zs,oz
    ploter(x, y);step = step+1
    if(gors==-1):
        if(ss>0):
            ss=ss-1 ;x=x+dirx; step=0
        elif(step==zs and oz>0):
            oz=oz-1;ss=skips;x=dirx
        y=y+diry
    if(gors==1):
        if(ss>0):
            ss=ss-1 ;y=y+diry; step=0
        elif(step==zs and oz>0):
            oz=oz-1;ss=skips;y=y+diry
        x=x+dirx

def drawer(x1,y1,x2,y2):
    global x,y,step,skips,ss,z,zs,oz
    dx=abs(x2-x1) ; px = dx+1
    dy=abs(y2-y1) ; py = dy+1
    z = zvalue(px, py) ; zminus = z-1 ; zs = z
    oz = abs(px-py) ; skips = skipvalue(px, py, oz)
    x=x1 ; y=y1 ; step = 0 ; ss = 0
    #print(skips)
    if (dy==dx):
        if(x<=x2):
                while(x<=x2):
                    ploter(x, y);x=x+1;y=y+1
        elif(x<=x2):
                while(x<=x2):
                    ploter(x, y);x=x+1;y=y-1
        elif(x>=x2):
                while(x>=x2):
                    ploter(x, y);x=x-1;y=y-1
        elif(x>=x2):
                while(x>=x2):
                    ploter(x, y);x=x-1;y=y+1

    elif(dy<dx):
        if(y==y2 and x<x2):
                while(x<=x2):
                    ploter(x, y);x=x+1
        elif(y==y2 and x>x2):
                while(x>=x2):
                    ploter(x, y);x=x-1
        elif(x<x2 and y<y2):
                while(x<=x2):
                    steps(1, 1, 1)
        elif(x<x2 and y>y2):
                while(x<=x2):
                    steps(1, -1, 1)
        elif(x>x2 and y>y2):
                while(x>=x2):
                    steps(-1, -1, 1)
        elif(x>x2 and y<y2):
                while(x>=x2):
                    steps(-1, 1, 1)

    elif(dy>dx):
        if(x==x2 and y<y2):
                while(y<=y2):
                    ploter(x, y);y=y+1
        elif(x==x2 and y>y2):
                while(y>=y2):
                    ploter(x, y);y=y-1
        elif(x<x2 and y<y2):
                while(x<=x2):
                    steps(1, 1, -1)
        elif(x<x2 and y>y2):
                while(x<=x2):
                    steps(1, -1, -1)
        elif(x>x2 and y>y2):
                while(x>=x2):
                    steps(-1, -1, -1)
        elif(x>x2 and y<y2):
                while(x>=x2):
                    steps(-1, 1, -1)


main()
