import pygame
import random
import schedule
from time import sleep
import time
from pygame.locals import *

WHITE = (255, 255, 255)
RED = (255, 0, 0)
pad_width = 1024
pad_height = 512
background_width = 1024
bat_width = 110
bat_height = 67
aircraft_width = 90
aircraft_height = 55
end_time = 0

fireball1_width = 140
fireball1_height = 60
fireball2_width = 86
fireball2_height = 60

isTrue = False

def game_start():
    start_screen = pygame.display.set_mode((pad_width,pad_height))
    
    pygame.font.init() #폰트 초기화
    
    start_button_img = pygame.image.load('start_button.png')
    start_button_img = pygame.transform.scale(start_button_img, (120,50))
    instructions_button = pygame.image.load('instructions_button.png')
    instructions_button = pygame.transform.scale(instructions_button, (120,50))

    logo_img = pygame.image.load('logo.png')
    logo_img = pygame.transform.scale(logo_img, (170,170))
   

    #start_button 위치 지정
    start_button_rect = start_button_img.get_rect()
    start_button_rect.center = (pad_width/2, 320)
    
    #instructions_button 위치 지정
    instructions_button_rect = instructions_button.get_rect()
    instructions_button_rect.center = (pad_width/2, 400)
    logo_img_rect = logo_img.get_rect()
    logo_img_rect.center = (pad_width/2, 120)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                pygame.sys.exit()
            #만약 event type이 내가 마우스 버튼을 누른거라면
            if event.type == MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    return
                elif instructions_button_rect.collidepoint(event.pos):
                    return instructions()
            
        #start screen에 검은색 바탕 칠하기
        start_screen.fill((255,255,255)) 
        #글자 나타내기: start_button_img를 start_button_rect에 
        start_screen.blit(start_button_img, start_button_rect)
        start_screen.blit(instructions_button, instructions_button_rect)
        start_screen.blit(logo_img, logo_img_rect)
        
        pygame.display.update() 

def instructions():
    instructions_screen = pygame.display.set_mode((pad_width,pad_height))
    pygame.font.init() #폰트 초기화
    
    back_button_img = pygame.image.load('back_button.png')
    back_button_img = pygame.transform.scale(back_button_img, (100,50))

    #back_button 위치 지정
    back_button_rect = back_button_img.get_rect()
    back_button_rect.center = (950, 450)
    
    #instructions_font = pygame.font.SysFont('freesansbold.ttf', 30,True, True)
    #instructions_message = 'How to play'
    #instructions_object = instructions_font.render(instructions_message,True, (0,0,0))
    

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                pygame.sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                # 만약 start button이 클릭되었다면 게임을 시작
                if back_button_rect.collidepoint(event.pos):
                    return game_start()
        instructions_screen.fill((255,255,255))
        instructions_screen.blit(back_button_img, back_button_rect)
        #instructions_screen.blit(instructions_object, back_button_rect)
        pygame.display.update()  

def scheduling() :
    global isTrue
    isTrue = True

def textObj(text, font):
    textSurface = font.render(text, True, RED)
    return textSurface, textSurface.get_rect()

def dispMessage(text):
    global gamepad, end_time

    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = textObj(text, largeText)
    TextRect.center = ((pad_width / 2), (pad_height / 2))
    gamepad.blit(TextSurf, TextRect)

    pygame.display.update()
    sleep(2)
    runGame()

def crash():
    global gamepad
    time_Title = myFont.render("Time: " + str(end_time), True, RED)
    time_rect = time_Title.get_rect()
    time_rect.topleft = (10, 40)
    gamepad.blit(time_Title, time_rect)
    dispMessage('Crashed!')

def drawObject(obj, x, y):
    global gamepad
    gamepad.blit(obj, (x, y))

def back(background, x, y):
    global gamepad
    gamepad.blit(background, (x, y))

def airplane(x, y):
    global gamepad, aircraft
    gamepad.blit(aircraft, (x, y))

def runGame():
    global gamepad, aircraft, clock, background1, background2
    global bat, fires, bullet, boom
    global myFont, isTrue, end_time

    isShotBat = False
    boom_count = 0
    score = 0
    life = 2
    life_img0 = pygame.image.load('life0.png')
    life_img0 = pygame.transform.scale(life_img0, (50, 50))
    life_img1 = pygame.image.load('life1.png')
    life_img1 = pygame.transform.scale(life_img1, (50, 50))

    bullet_xy = []

    x = pad_width * 0.05
    y = pad_height * 0.8
    y_change = 0

    background1_x = 0
    background2_x = background_width

    bat_x = pad_width
    bat_y = random.randrange(0, pad_height)

    fire_x = pad_width
    fire_y = random.randrange(0, pad_height)

    random.shuffle(fires)
    fire = fires[0]

    bullet_x = x + aircraft_width
    bullet_y = y + aircraft_height / 2
    bullet_xy.append([bullet_x, bullet_y])

    crashed = False
    clock = pygame.time.Clock()
    last_time = pygame.time.get_ticks()
    start_time = pygame.time.get_ticks()
    
    while not crashed:
        if isTrue == True :
            bullet_x = x + aircraft_width
            bullet_y = y + aircraft_height / 2
            bullet_xy.append([bullet_x, bullet_y])
            isTrue = False
        schedule.run_pending()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5
                elif event.key == pygame.K_LCTRL:
                    bullet_x = x + aircraft_width
                    bullet_y = y + aircraft_height / 2
                    bullet_xy.append([bullet_x, bullet_y])
                elif event.key == pygame.K_SPACE:
                    sleep(5)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
        
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - last_time

        end_time = pygame.time.get_ticks()
        end_time = (end_time - start_time) / 1000

        if(elapsed_time >= 10000):
            score = score + 300
            last_time = current_time

        y += y_change
        gamepad.fill(WHITE)

        text_Title = myFont.render("Score: " + str(score), True, RED)
        text_rect = text_Title.get_rect()
        text_rect.topleft = (10, 10)
        gamepad.blit(text_Title, text_rect)

        background1_x -= 2
        background2_x -= 2

        if y < 0:
            y = 0
        elif y > pad_height - aircraft_height:
            y = pad_height - aircraft_height

        bat_x -= 7
        if bat_x <= 0:
            bat_x = pad_width
            bat_y = random.randrange(0, pad_height)

        if fire[1] == None:
            fire_x -= 30
        else:
            fire_x -= 15

        if fire_x < 0:
            fire_x = pad_width
            fire_y = random.randrange(0, pad_height)
            random.shuffle(fires)
            fire = fires[0]
        
        if len(bullet_xy) != 0:
            for i, bxy in enumerate(bullet_xy):
                bxy[0] += 15
                bullet_xy[i][0] = bxy[0]
                if bxy[0] > bat_x:
                    if bxy[1] > bat_y and bxy[1] < bat_y + bat_height :
                        score = score + 100
                        bullet_xy.remove(bxy)
                        isShotBat = True
                    if bxy[0] >= pad_width :
                        try :
                            bullet_xy.remove(bxy)
                        except :
                            pass

        if x + aircraft_width > bat_x:
            if (y > bat_y and y < bat_y + bat_height) or \
            (y + aircraft_height > bat_y and y + aircraft_height < bat_y + bat_height):
                life = life - 1
                if life == 0:
                    crash()
                else:
                    bat_x = pad_width
                    bat_y = random.randrange(0, pad_height - bat_height)
                    if life == 1:
                        life_img0.set_alpha(0)

        if fire[1] != None:
            if fire[0] == 0:
                fireball_width = fireball1_width
                fireball_height = fireball1_height
            elif fire[0] == 1:
                fireball_width = fireball2_width
                fireball_height = fireball2_height
            if x + aircraft_width > fire_x:
                if (y > fire_y and y < fire_y + fireball_height) or \
                (y + aircraft_height > fire_y and y + aircraft_height < fire_y + fireball_height):
                    life = life - 1
                    if life == 0:
                        crash()
                    else:
                        fire_x = pad_width
                        fire_y = random.randrange(0, pad_height - fireball_height)
                        random.shuffle(fires)
                        fire = fires[0]
                        if life == 1:
                            life_img0.set_alpha(0)

        if background1_x == -background_width:
            background1_x = background_width

        if background2_x == -background_width:
            background2_x = background_width

        drawObject(background1, background1_x, 0)
        drawObject(background2, background2_x, 0)
        gamepad.blit(text_Title, text_rect)
        gamepad.blit(life_img0, (900, 10))
        gamepad.blit(life_img1, (960, 10))
        drawObject(bat, bat_x, bat_y)

        if fire[1] != None:
            drawObject(fire[1], fire_x, fire_y)

        if len(bullet_xy) != 0:
            for bx, by in bullet_xy:
                drawObject(bullet, bx, by)

        if not isShotBat:
            drawObject(bat, bat_x, bat_y)
        else:
            drawObject(boom, bat_x, bat_y)
            boom_count += 1
            if boom_count > 5:
                boom_count = 0
                bat_x = pad_width
                bat_y = random.randrange(0, pad_height - bat_height)
                isShotBat = False

        drawObject(aircraft, x, y)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

def initGame():
    global gamepad, aircraft, clock, background1, background2
    global bat, fires, bullet, boom
    global myFont

    #게임 시작화면
    game_start()

    fires = []

    pygame.init()

    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption('PyFlying')

    aircraft = pygame.image.load('plane.png')
    clock = pygame.time.Clock()
    background1 = pygame.image.load('background.png')
    background1 = pygame.transform.scale(background1, (1024, 512))
    background2 = background1.copy()
    bat = pygame.image.load('bat.png')
    fires.append((0, pygame.image.load('fireball1.png')))
    fires.append((1, pygame.image.load('fireball2.png')))
    bullet = pygame.image.load('bullet.png')
    boom = pygame.image.load('boom.png')

    for n in range(3):
        fires.append((n + 2, None))

    myFont = pygame.font.SysFont("arial", 30, True, False)

    runGame()

schedule.every(1).seconds.do(scheduling)
initGame()