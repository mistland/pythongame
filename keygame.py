import random
import pygame
pygame.init()
size = [400,300]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# player position
x = size[0] / 2
y = size[1] / 2

#ball position
ballx = random.randrange(0,size[0])
bally = random.randrange(0,size[1])

# goal position
goalx = size[0] / 2 - 10
goaly = size[1] / 2 - 10
goalw = 20
goalh = 20

#points
points = 0

# colours
red = pygame.color.Color('#ff8080')
blue = pygame.color.Color('#8080ff')
green = pygame.color.Color('#00ff00')
white = pygame.color.Color('#ffffff')
black = pygame.color.Color('#000000')

def checkx(x):
    if x > size[0]:
        x = 0
    elif x < 0:
        x = size[0]
    return x
def checky(y):
    if y > size[1]:
        y = 0
    elif y < 0:
        y = size[1]
    return y

def checktouching():
    global x
    global y
    global ballx
    global bally

    # check if player and ball are touching
    if -10 < y - bally < 10 and -10 < x - ballx < 10:
        #draw an explosion
        pygame.draw.circle(screen, white, [x,y], 15)

        xdiff = x - ballx
        ydiff = y - bally

        #check if ball is on edge of screen
        if ballx == 0:
            xdiff -= 5
        elif ballx == size[0]:
            xdiff += 5
        if bally == 0:
            ydiff -= 5
        elif bally == size[0]:
            ydiff += 5
            

        # move the ball and player
        x += xdiff * 3
        ballx -= xdiff * 3

        y += ydiff * 3
        bally -= ydiff * 3

# game loop
done = False



while not done:
    screen.fill(black)#清空每一帧

    #得到程序开始运行的时间
    timestart = pygame.time.get_ticks()
    times = 60000 - timestart
    
    #draw the goal
    pygame.draw.rect(screen, white, (goalx,goaly,goalw,goalh))

    #check ball is in goal
    if goalx <= ballx <= goalx + goalw and goaly <= bally <= goaly + goalh:
        points += 1
        ballx = random.randrange(0,size[0])
        bally = random.randrange(0,size[1])

    #draw points
    for point in range(points):
        pointX = 0 + point * 5
        pygame.draw.rect(screen, white, (pointX, 3, 4, 7))

    for time in range(times):
        
        timeX = times / 1000
        pygame.draw.rect(screen, green, (0, 13, timeX, 5))
    
    keys = pygame.key.get_pressed()

    #player movement
    if keys[pygame.K_UP]:
        y -= 3
        
    if keys[pygame.K_DOWN]:
        y += 3

    if keys[pygame.K_LEFT]:
        x -= 3

    if keys[pygame.K_RIGHT]:
        x += 3

    #check off screen
    x = checkx(x)
    y = checky(y) 
    ballx = checkx(ballx)
    bally = checky(bally)
    # check if player is touching the ball
    checktouching()
    
    #draw player
    pygame.draw.circle(screen,red,[x,y],6)

    #draw ball
    pygame.draw.circle(screen,blue,[ballx,bally],5)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    clock.tick(64)

    #检查游戏是否运行了60s
    timenow = pygame.time.get_ticks()
    if timenow >= 60000:
        done = True
    
pygame.quit()
print "total points:" + str(points)   
