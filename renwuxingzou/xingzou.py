import random
import pygame
pygame.init()

def move(image1, image2):
    global count
    if count < 5:
        image = image1
    elif count >= 5:
        image = image2

    if count >= 10:
        count = 0
    else:
        count += 1
    return image

windowsize = [400,300]
screen = pygame.display.set_mode(windowsize)
clock = pygame.time.Clock()

standing = pygame.image.load('li.png')

down1 = pygame.image.load('xia.png')
down2 = pygame.image.load('xia1.png')
up1 = pygame.image.load('shang.png')

up2 = pygame.image.load('shang1.png')
left1 = pygame.image.load('zuo.png')
left2 = pygame.image.load('zuo1.png')

right1 = pygame.transform.flip(left1, True, False)#第一个Ture水平翻转，第二个竖直反转
right2 = pygame.transform.flip(left2, True, False)

tport1 = pygame.image.load('teleport1.png')
tport2 = pygame.image.load('teleport2.png')
tport3 = pygame.image.load('teleport3.png')

white = pygame.color.Color('#ffffff')

pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)
teleportsound = pygame.mixer.Sound('teleport.wav') #载入音乐

count = 0
x = 0
y = 0
asd = 16
locked = False
done = False
while not done:
    screen.fill(white)
    keys = pygame.key.get_pressed()

    #player movent
    if keys[pygame.K_s]:
        image = move(down1,down2)
        y += 1
    elif keys[pygame.K_w]:
        image = move(up1,up2)
        y -= 1
    elif keys[pygame.K_d]:
        image = move(right1,right2)
        x += 1
    elif keys[pygame.K_a]:
        image = move(left1,left2)
        x -= 1
    elif keys[pygame.K_SPACE]:
        if asd > 0:
            locked = True
            asd = asd - 1
    else:
        image = standing
        count = 0
    while locked:
        teleportsound.play()
        if count < 5:
            image = tport1
        elif count < 10:
            image = tport2
        elif count < 15:
            image = tport3
        else:
            x = random.randrange(0,windowsize[0])
            y = random.randrange(0,windowsize[1])
            count = 0
            locked = False
        count += 1
    screen.blit(image,(x,y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
    clock.tick(32)
pygame.quit()
