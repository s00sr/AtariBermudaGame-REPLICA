from pygame_functions import *
from pygameMenu import *
from pygame.locals import *
import pygame
import sys
import random
import pygameMenu
#screen var.
width = 810
height = 540
screenSize(width,height)
setAutoUpdate(False)
#global var.
vida = 3
cVida = 3
gas = 20
pnts = 0
#background img and audio.
setBackgroundImage("imgs/fondo.png")
music = pygame.mixer.music.load("sounds/babyshark.mp3")
playMusic()
#sounds.
sdShoot = makeSound("sounds/Wav/Shoot_00.wav")
explosion = makeSound("sounds/Wav/Explosion_00.wav")
#tiles.
tile = makeSprite("imgs/dustTile.png")#("imgs/dustTile.png") - ("imgs/rockTile.png")   ## cambiar imagen a dustTile para lvl 2 y rockTile para lvl 3
#character objects.
sShip = makeSprite("imgs/sMove.gif",2)
sShoot = makeSprite("imgs/sShoot.gif",2)
#main objs.
#   -----     fAuto = makeSprite("imgs/fullA.png")    --  INTENTO DE POWERUP ADICIONAL
cloud = makeSprite("imgs/cloud.png")
fuel = makeSprite("imgs/fuel.png")
enemy = makeSprite("imgs/enemy.png")
bullet1 = makeSprite("imgs/bullet.png")
bullet2 = makeSprite("imgs/bullet.png")
#power ups: escudo y supergasolina
fFuel = makeSprite("imgs/fullFuel.png")
shield = makeSprite("imgs/shield.png")
#labels.
score = makeLabel("SCORE : "+str(pnts), 36, 50, 100, fontColour='red', font='Comic Sans MS')
vidas = makeLabel("<3 "*cVida, 36, 50, 50, fontColour='red', font='Comic Sans MS')
indic = makeLabel("FUEL:", 36, 50,404, fontColour='red', font='Comic Sans MS')
fuelC = makeLabel("|"*gas, 36, 50,454, fontColour='red', font='Comic Sans MS')
lvl_2 = makeLabel("LEVEL 2 EN CONSTRUCCION...", 36, 50, 100, fontColour='red', font='Comic Sans MS')
#game vars.
yTile = -15218+height/2
xPos = width/2
yPos = height/2
xSpeed = 0
ySpeed = 0
nextFrame = clock()
frame=0
xShip = xPos
yShip = yPos
#sprite initial positions.
moveSprite(sShip, xPos, yPos)
moveSprite(sShoot, xPos, yPos)
moveSprite(tile, 0, yTile)
#spawning objects.
enemies = []
clouds = []
fuels = []
bullets1 = []
bullets2 = []
shields = []
fFuels = []
for x in range(3):
    enemy.x = random.randint(0,810)
    enemy.y = random.randint(0,540)
    moveSprite(enemy, enemy.x, enemy.y)
    enemy.xspeed = random.randint(-3,3)
    showSprite(enemy)
    enemies.append(enemy)
for x in range(1):
    fuel.x = random.randint(150,650)
    fuel.y = random.randint(0,540)
    fuel.xspeed = random.randint(-1,1)
    fuel.yspeed = 2
    moveSprite(fuel, fuel.x, fuel.y)
    showSprite(fuel)
    fuels.append(fuel)
for x in range(1):
    shield.x = random.randint(150,650)
    shield.y = random.randint(0,540)
    shield.yspeed = 1
    moveSprite(shield, shield.x, shield.y)
    showSprite(shield)
    shields.append(shield)
for x in range(1):
    fFuel.x = random.randint(150,650)
    fFuel.y = random.randint(0,540)
    fFuel.yspeed = 1
    moveSprite(fFuel, fFuel.x, fFuel.y)
    showSprite(fFuel)
    fFuels.append(fFuel)
for x in range(7):
    cloud.x = random.randint(0,810)
    cloud.y = random.randint(0,540)
    cloud.xspeed = random.randint(-2,2)
    cloud.yspeed = random.randint(-1,1)
    moveSprite(cloud, cloud.x, cloud.y)
    showSprite(cloud)
    clouds.append(cloud)
for e in range(1):
    bullet1.x = xShip+5
    bullet1.y = yShip
    bullet1.yspeed = 0
    bullet2.x = xShip+45
    bullet2.y = yShip
    bullet2.yspeed = 0
    moveSprite(bullet1, bullet1.x, yShip)
    showSprite(bullet1)
    bullets1.append(bullet1)
    moveSprite(bullet2, bullet2.x, yShip)
    showSprite(bullet2)
    bullets2.append(bullet2)
#sprites in screen
showSprite(sShip)
showSprite(tile)
jugando = True
while jugando:
    showLabel(indic)
    showLabel(fuelC)
    showLabel(score)
    showLabel(vidas)
    #cambio de imagen de GIFS
    if clock() > nextFrame:
        frame = (frame+1)%1
        nextFrame += 10    
    #puntuacion
    if pnts%5 == 0:
        changeLabel(score,"SCORE :"+str(pnts))
    #final nivel 1    
    if pnts == 2000:
        changeLabel(vidas,"CONGRATULATIONS! END OF LEVEL 1")
        hideLabel(score)
        showLabel(lvl_2)
        vida = 3
        cVida = 3
        gas = 20
        pause(2000, False)
        jugando = False
        #lvl 2 en construccion
        hideLabel(lvl_2)
        showLabel(score)
        moveSprite(sShip, xPos, yPos)
        moveSprite(sShoot, xPos, yPos)
    
    #formas de perder vidas
    if touching(sShip or sShoot, tile)or(gas == 0):
        moveSprite(sShip, xPos, yPos)
        moveSprite(sShoot, xPos, yPos)
        xShip = xPos
        yShip = yPos
        cVida -= 1
        vida -= 1
        changeLabel(vidas,"<3 "*cVida)
        if vida == 0:
            hideSprite(sShip)
            hideSprite(sShoot)
            changeLabel(vidas,"GAME OVER, GOOD LUCK NEXT TIME :)")
            stopMusic()
            jugando = False
            
    if keyPressed("up"):
        pnts += 1
        changeSpriteImage(sShip, 1+frame)
        changeSpriteImage(sShoot, 1+frame)
        scrollBackground(0, 8)
        moveSprite(tile, 0, yTile+10)
        yTile += 10
        if keyPressed("right"):    
            moveSprite(sShip, xShip+7, yPos)
            moveSprite(sShoot, xShip+7, yPos)
            xShip += 8
        if keyPressed("left"):    
            moveSprite(sShip, xShip-7, yPos)
            moveSprite(sShoot, xShip-7, yPos)
            xShip -= 8
        #contador de gasolina
        if pnts%75 == 0:
            gas -= 1
            changeLabel(fuelC,"|"*gas)
    else:
        pnts += 0
        changeSpriteImage(sShip, frame)
        
    xPos += xSpeed
    if xPos > width:
        xPos = 0
    elif xPos < 0:
        xPos = width

    for enemy in enemies:
        enemy.x += enemy.xspeed
        if enemy.x > width:
            enemy.x = 0
        elif enemy.x < 0:
            enemy.x = width
        if touching(sShip or sShoot, enemy):
            vida -= 1
            cVida -= 1
            
        moveSprite(enemy, enemy.x, enemy.y)
    for cloud in clouds:
        cloud.x += cloud.xspeed
        if cloud.x > width:
            cloud.x = 0
        elif cloud.x < 0:
            cloud.x = width
        cloud.y += cloud.yspeed
        if cloud.y > height:
            cloud.y = 0
        elif cloud.y < 0:
            cloud.y = height
        moveSprite(cloud, cloud.x, cloud.y)
    for fuel in fuels:    
        if touching(sShip or sShoot, fuel):
            hideSprite(fuel)
            if gas in range(0,19):
                gas += 1
        fuel.x += fuel.xspeed
        if fuel.x > width:
            fuel.x = 150
        elif fuel.x < 0:
            fuel.x = 650
        fuel.y += fuel.yspeed
        if fuel.y > height:
            fuel.y = 0
            showSprite(fuel)
        moveSprite(fuel, fuel.x, fuel.y)
    for shield in shields:
        shield.y += shield.yspeed
        if shield.y > height:
            shield.y = 0
            showSprite(shield)
        elif touching(sShip or sShoot, shield):
            if vida in range(0,5):
                vida += 1
                cVida += 1
            hideSprite(shield)
        moveSprite(shield, shield.x, shield.y)
    for fFuel in fFuels:
        fFuel.y += fFuel.yspeed
        if fFuel.y > height:
            fFuel.y = 0
            showSprite(fFuel)
        elif touching(sShip or sShoot, fFuel):
            hideSprite(fFuel)
            if gas in range(0,19):
                gas = 20
        moveSprite(fFuel, fFuel.x, fFuel.y)
    for bullet1 in bullets1:
        if bullet1.y < 0:
            moveSprite(bullet1, xShip+5, yShip)
        elif touching(bullet1,shield):
            hideSprite(shield)
            moveSprite(bullet1, xShip+5, yShip)
        elif touching(bullet1,fuel):
            hideSprite(fuel)
            moveSprite(bullet1, xShip+5, yShip)
        elif touching(bullet1,enemy):
            hideSprite(enemy)
            moveSprite(bullet1, xShip+5, yShip)
    for bullet2 in bullets2:
        if bullet2.y < 0:
            moveSprite(bullet2, xShip+45, yShip)
        elif touching(bullet2,shield):
            hideSprite(shield)
            moveSprite(bullet2, xShip+45, yShip)
        elif touching(bullet2,fuel):
            hideSprite(fuel)
            moveSprite(bullet2, xShip+45, yShip)
        elif touching(bullet2,enemy):
            hideSprite(enemy)
            moveSprite(bullet2, xShip+45, yShip)
            
        if keyPressed("space"):
            bullet1.yspeed = -10
            bullet1.y += bullet1.yspeed
            moveSprite(bullet1, xShip+5, bullet1.y)
            showSprite(bullet1)
            bullet2.yspeed = -10
            bullet2.y += bullet2.yspeed
            moveSprite(bullet2, xShip+20, bullet2.y)
            showSprite(bullet2)
            playSound(sdShoot)
            hideSprite(sShip)
            showSprite(sShoot)
            changeSpriteImage(sShoot, 1+frame)
        else:
            moveSprite(bullet1, xShip+5, yShip)
            moveSprite(bullet2, xShip+20, yShip)
            hideSprite(sShoot)
            showSprite(sShip)
            changeSpriteImage(sShoot, frame)
            
    tick(45)
    updateDisplay()

endWait()
