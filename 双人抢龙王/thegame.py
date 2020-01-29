import random
import pygame
pygame.init()

#走路动画
def moveanimation(image1,image2,count):
    if 10 < count % 20 <= 20:
        return image2
    else:
        return image1

#墙壁
def upclear(x,y):#向上
    canmove = True

    if verticaldoorleft <= x <= verticaldoorright and y - 1 < topwall:
        canmove = True
    elif y - 1 < topwall:
        canmove = False
    elif (x < leftwall or x > rightwall) and y - 1 < middledoorstop:
        canmove = False

    if canmove:#如果玩家可以移动，函数返回1，如果玩家不能移动，返回0
        return 1
    else:
        return 0

def downclear(x,y):
    canmove = True

    if verticaldoorleft <= x <= verticaldoorright and bottomwall < y + 1:
        canmove = True
    elif bottomwall < y + 1:
        canmove = False
    elif (x < leftwall or x > rightwall) and y + 1 > middledoorsbuttom:
        canmove = False

    if canmove:#如果玩家可以移动，函数返回1，如果玩家不能移动，返回0
        return 1
    else:
        return 0
def leftclear(x,y):#向左
    canmove = True

    if middledoorstop <= y <= middledoorsbottom and x - 1 < leftwall:
        canmove = True
    elif x - 1 < leftwall:
        canmove = False
    elif (y > bottomwall or y < topwall) and x - 1 < verticaldoorleft:
        canmove = False

    if canmove:#如果玩家可以移动，函数返回1，如果玩家不能移动，返回0
        return 1
    else:
        return 0
def rightclear(x,y):
    canmove = True

    if middledoorstop <= y <= middledoorsbottom and x + 1 > rightwall:
        canmove = True
    elif x + 1 > rightwall:
        canmove = False
    elif (y > bottomwall or y < topwall) and x + 1 > verticaldoorright:
        canmove = False

    if canmove:#如果玩家可以移动，函数返回1，如果玩家不能移动，返回0
        return 1
    else:
        return 0

#门，碰撞效果，金币
def checkoffscreen(x,y):
    if x < -14:#上下两门传送
        x = windowsize[0] - 14
    elif x > windowsize[0] - 14:
        x = -14
    if y < -20:#左右传送
        y = windowsize[1] - 20
    elif y > windowsize[1] - 20:
        y = -20
    return x, y

def playerstouching():#玩家碰撞
    global ponex, poney, ptwox, ptwoy

    if -32 < ponex - ptwox < 32 and -40 < poney - ptwoy < 40:
        xdiff = ponex - ptwox
        ydiff = poney - ptwoy
        
        for dist in range(abs(xdiff) / 2):
            ponemove = leftclear(ponex, poney) + rightclear(ponex, poney)
            ptwomove = leftclear(ptwox, ptwoy) + rightclear(ptwox, ptwoy)
            if xdiff > 0:
                ponex += ponemove / 2 * xdiff / xdiff
                ptwox -= ptwomove / 2 * xdiff / xdiff
            else:
                ponex -= ponemove / 2 * xdiff / xdiff
                ptwox += ptwomove / 2 * xdiff / xdiff
        for dist in range(abs(ydiff) / 2):
            ponemove = upclear(ponex, poney) + downclear(ponex, poney)
            ptwomove = upclear(ptwox, ptwoy) + downclear(ptwox, ptwoy)
            if ydiff > 0:
                poney += ponemove / 2 * ydiff / ydiff
                ptwoy -= ptwomove / 2 * ydiff / ydiff
            else:
                poney -= ponemove / 2 * ydiff / ydiff
                ptwoy += ptwomove / 2 * ydiff / ydiff

def touchingcoin(x,y):#是否碰触龙王
    return -32 < x - coinpos[0] < 20 and -40 < y - coinpos[1] < 20

def randomposition():#生成随机位置
    x = random.randrange(32, windowsize[0] - 52)
    y = random.randrange(32, windowsize[1] - 52)
    return x, y

windowsize = [640, 384]
screen = pygame.display.set_mode(windowsize)
clock = pygame.time.Clock()

#得分字体
pointfont = pygame.font.SysFont('Monospace', 15)

#变量大集合 =_=
ponex = windowsize[0] / 4
poney = windowsize[1] / 2

ptwox = windowsize[0] / 4 * 3
ptwoy = windowsize[1] / 2

coinpos = randomposition()

ponepoints = 0
ptwopoints = 0

ponecount = 0
ptwocount = 0

ponemoving = False
ptwomoving = False

#墙壁和门的位置值
leftwall = 28
topwall = 16
rightwall = windowsize[0] - 60
bottomwall = 312

middledoorstop = 144
middledoorsbottom = 182
verticaldoorleft = 284
verticaldoorright = verticaldoorleft + 40

#载入图像
background = pygame.image.load('background.png')
background = pygame.transform.scale(background, windowsize)

light = pygame.image.load('light.png')
light = pygame.transform.scale(light, windowsize)

ponemove1 = pygame.image.load('sprite1_walking1.png')
ponemove1 = pygame.transform.scale2x(ponemove1)

ponemove2 = pygame.image.load('sprite1_walking2.png')
ponemove2 = pygame.transform.scale2x(ponemove2)

ponestanding = pygame.image.load('sprite1_standing.png')
ponestanding = pygame.transform.scale2x(ponestanding)

ptwomove1 = pygame.image.load('sprite2_walking1.png')
ptwomove1 = pygame.transform.scale2x(ptwomove1)

ptwomove2 = pygame.image.load('sprite2_walking2.png')
ptwomove2 = pygame.transform.scale2x(ptwomove2)

ptwostanding = pygame.image.load('sprite2_standing.png')
ptwostanding = pygame.transform.scale2x(ptwostanding)

coin = pygame.image.load('coin.png')
coin = pygame.transform.scale2x(coin)

#载入声音
coinsound = pygame.mixer.Sound('coin.wav')
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)

#开始循环(角色控制与动画)
done = False
while not done:
    #玩家一
    ponemoving = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        poney += downclear(ponex,poney)
        ponemoving = True

    if keys[pygame.K_w]:
        poney -= upclear(ponex,poney)
        ponemoving = True
        
    if keys[pygame.K_a]:
        ponex -= leftclear(ponex,poney)
        ponemoving = True

    if keys[pygame.K_d]:
        ponex += rightclear(ponex,poney)
        ponemoving = True

    ponex, poney = checkoffscreen(ponex, poney)

    if ponemoving:
        ponecount += 1
        poneimage = moveanimation(ponemove1,ponemove2,ponecount)
    else:
        poneimage = ponestanding

    #玩家二
    ptwomoving = False
    if keys[pygame.K_DOWN]:
        ptwoy += downclear(ptwox,ptwoy)
        ptwomoving = True

    if keys[pygame.K_UP]:
        ptwoy -= upclear(ptwox,ptwoy)
        ptwomoving = True
        
    if keys[pygame.K_LEFT]:
        ptwox -= leftclear(ptwox,ptwoy)
        ptwomoving = True

    if keys[pygame.K_RIGHT]:
        ptwox += rightclear(ptwox,ptwoy)
        ptwomoving = True

    ptwox, ptwoy = checkoffscreen(ptwox, ptwoy)

    if ptwomoving:
        ptwocount += 1
        ptwoimage = moveanimation(ptwomove1,ptwomove2,ptwocount)
    else:
        ptwoimage = ptwostanding

    #检查碰触
    playerstouching()

    #检查龙王碰触
    if touchingcoin(ponex, poney):
        ponepoints += 1
        coinsound.play()

    if touchingcoin(ptwox, ptwoy):
        ptwopoints += 1
        coinsound.play()
        
    #下一个龙王
    if touchingcoin(ponex,poney) or touchingcoin(ptwox, ptwoy):
        coinpos = randomposition()

    #显示得分并更新窗口
    ponepointlabel = pointfont.render(str(ponepoints),1,(255,255,255))
    ptwopointlabel = pointfont.render(str(ptwopoints),1,(255,255,255))

    #输出表面
    screen.blit(background, (0,0))
    screen.blit(coin, coinpos)
    screen.blit(poneimage, [ponex, poney])
    screen.blit(ptwoimage, [ptwox, ptwoy])
    screen.blit(ponepointlabel, [ponex - 9, poney - 9])
    screen.blit(ptwopointlabel, [ptwox - 9, ptwoy - 9])
    screen.blit(light, (0,0))

    pygame.display.flip()

    #退场
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    clock.tick(60)
pygame.quit()
    
        
    





















































        
    
