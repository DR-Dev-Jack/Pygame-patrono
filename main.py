import pygame
import random

pygame.init()

score = 0
event = ""
lengte_sprong = 0
jump_total = 0
jump = False
width = 20.1
height = 20
x_player = 200
y_player = 200
x_target = (random.randint(50, 450))
y_target = (random.randint(50, 350))
x_flames = x_player
y_flames = y_player
size_target = 100
kleur_buiten = (255, 0, 0)
kleur_binnen = (61, 0, 201)
x_block = 0
how_many_presses = 0
seconden = 0
stopwatch = 0
minuten = 0
hoogte = 0

display = pygame.display.set_mode((500, 500))  # venster aanmaken
random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
color = random_color
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 225)

flames = "/Users/jackladde/PycharmProjects/PyGame/images/mini_flames.png"  # plek op de computer bestanden van de flames
image = pygame.image.load(flames).convert()  # laad/rendered de flames
parachute = "images/parachute.png"
image_parachute = pygame.image.load(parachute).convert()

punten = 0
font = pygame.font.Font('freesansbold.ttf', 32)
text_score = font.render(str("score"), bool(1), green)
text_variable = font.render(str("0"), bool(1), green)

text_rect_score = text_score.get_rect()
text_rect_variable = text_variable.get_rect()
text_rect_score.center = (390, 20)
text_rect_variable.center = (450, 20)

# boven is de punten display en onder de tijd display

text_time = font.render(str("time"), bool(1), green)
text_variable_stopwatch = font.render(str(round(stopwatch)), bool(1), green)
textRect_time = text_time.get_rect()
textRect_variable_stopwatch = text_variable_stopwatch.get_rect()
textRect_time.center = (40, 20)
textRect_variable_stopwatch.center = (100, 20)

# onder is hoogte
text_hoogte = font.render(str("hoogte"), bool(1), green)
text_variable_hoogte = font.render(str(round(y_player)), bool(1), green)
textRect_hoogte = text_hoogte.get_rect()
textRect_variable_hoogte = text_variable_hoogte.get_rect()
textRect_hoogte.center = (60, 480)
textRect_variable_hoogte.center = (160, 480)

pygame.display.set_caption("patrono (:")  # naam

clock = pygame.time.Clock()

print("song 2 is hackerland by Twin Musicom website is twinmusicom.org")
print("song 3 is The coal Mine by Twin Musicom website is twinmusicom.org")

play_1 = ["luke: 40 punten 1,1 minuten", "stan: 66 punten 1,1 minuten ", "remy 20 punten 1,1 minuut"]
play_2 = [""]
plays = play_1 + play_2
print(plays)
run = True
music_theme = "sounds/theme_song.mp3"
pygame.mixer.music.load(music_theme)
pygame.mixer.music.play(-1)

# pygame.mixer.Channel(0).play(pygame.mixer.Sound('sounds/rocket_noise.mp3'))


while run:

    # pygame.time.delay(10)  # delay zodat je computer niet kapot gaat

    clock.tick(60)  # de frames
    seconden += clock.get_time() / 1000  # haalt de tijd op
    hele_seconden = round(seconden)  # verander seconden met miniseconden naar alleen seconden
    if seconden >= 60:  # kijkt of er 60 seconden voorbij zijn
        minuten += 1  # als er 60 seconden voorbij zijn voegt hij 1 minuut toe
        seconden = 0  # en voegt 1 minuut row
    stopwatch = minuten, hele_seconden

    if y_player <= 450 and not jump:  # soort van grond en kijkt of jumpt
        y_player = y_player + 4  # de gravity

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:  # escape de game met escape
        event.type = pygame.QUIT

    if keys[pygame.K_SPACE] or keys[pygame.K_UP]:  # springen
        lengte_sprong += 3
        if jump:
            y_player = y_player - 3
    else:
        if lengte_sprong >= 1:
            jump_total += 3
            jump = True
            y_player = y_player - 3
            if jump_total >= lengte_sprong:
                jump = False
                lengte_sprong = 0
                jump_total = 0

    if keys[pygame.K_TAB] and keys[pygame.K_1]:
        music_theme = "sounds/theme_song.mp3"  # laad de theme song op gevonden op zapsplat
        pygame.mixer.music.load(music_theme)
        pygame.mixer.music.play(-1)

    if keys[pygame.K_TAB] and keys[pygame.K_2]:
        music_theme = "sounds/HackerLand_theme_song.mp3"  # laad the hackerland van twin musicom
        pygame.mixer.music.load(music_theme)
        pygame.mixer.music.play(-1)

    if keys[pygame.K_TAB] and keys[pygame.K_3]:
        music_theme = "sounds/coalmine_theme_song.mp3"  # laad the coal mine van twin musicom
        pygame.mixer.music.load(music_theme)
        pygame.mixer.music.play(-1)

    if y_player >= 450:  # lopen op de grond
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            x_player = x_player - 0.5
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            x_player = x_player + 0.5

    if y_player <= 450:  # lopen in de lucht
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            x_player = x_player - 1.5
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            x_player = x_player + 1.5

    if x_player >= 445:
        x_player = 5
    if x_player <= 1:
        x_player = 440

    if lengte_sprong >= int("270"):  # maximale jump hoogte
        lengte_sprong = int("270")

    display.fill((0, 0, 0))  # scherm kleur

    random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    player = pygame.draw.rect(display, blue, (x_player, y_player, 50, 50))  # player <<<< daar <<< daar
    target = pygame.draw.rect(display, color, (x_target, y_target, size_target, size_target))  # target
    # hier onder is collision van dingen boven mij
    collide = player.colliderect(target)  # kijkt of de player de target aanraakt

    if collide:
        punten = punten + 1
        size_target = size_target - size_target / 100
        x_target = (random.randint(50, 450))
        y_target = (random.randint(50, 350))
        color = random_color
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('sounds/pop_noise.mp3'))  # plays the: "pop" noise
        pygame.mixer.music.set_volume(1)

    amogus_cijfer = random.randint(0, 5000)  # this code does nothing
    if amogus_cijfer == 420:  # this code does nothing
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.Channel(2).play(pygame.mixer.Sound('sounds/no_noise.mp3'))  # this code does nothing
        pygame.mixer.music.set_volume(1)  # this code does nothing

    # bar
    BarPercentage = lengte_sprong // int("3")
    pygame.draw.rect(display, kleur_buiten, pygame.Rect(390, 460, 100, 30), 2)  # omtrek jump box
    pygame.draw.rect(display, kleur_binnen, pygame.Rect(395, 465, BarPercentage, 20))  # binnenkant jump box

    # score print op het scherm
    text_score = font.render(str("score"), bool(1), green)
    text_variable = font.render(str(punten), bool(1), green)
    display.blit(text_score, text_rect_score)
    display.blit(text_variable, text_rect_variable)

    # tijd printen
    text_time = font.render(str("time"), bool(1), green)
    text_variable_stopwatch = font.render(str(stopwatch), bool(1), green)
    display.blit(text_time, textRect_time)
    display.blit(text_variable_stopwatch, textRect_variable_stopwatch)

    # hoogte printen
    if y_player <= 450:
        hoogte = 450 - y_player

    text_hoogte = font.render(str("hoogte"), bool(1), green)
    text_variable_hoogte = font.render(str(hoogte), bool(1), green)
    display.blit(text_hoogte, textRect_hoogte)
    display.blit(text_variable_hoogte, textRect_variable_hoogte)

    x_flames = x_player  # zet de x van de flames naar de x van de player
    y_flames = y_player + 50  # zet de y van de flames naar de y van de player
    if jump:
        display.blit(image, (x_flames, y_flames))

    x_parachute = x_player - 13
    y_parachute = y_player - 66
    if keys[pygame.K_DOWN] or keys[pygame.K_LSHIFT]:
        if not jump and y_player <= 450:
            display.blit(image_parachute, (x_parachute, y_parachute))
            y_player -= 2

    pygame.display.update()

pygame.quit()
