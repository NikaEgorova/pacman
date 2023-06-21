from pygame import *
mixer.init()
mixer.music.load('music.mp3')
mixer.music.play(-1)
mouse=mixer.Sound('mouse.wav')

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x, player_y, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed,player_y_speed, bar):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)

        self.x_speed = player_x_speed
        self.y_speed = player_y_speed
        self.barriers = bar
    def update(self):  
        if self.rect.x <= win_width-85 and self.x_speed > 0 or self.rect.x >= 0 and self.x_speed < 0:
            self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, self.barriers, False)
        if self.x_speed > 0: 
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left) 
        elif self.x_speed < 0: 
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right) 
        if self.rect.y <= win_height-85 and self.y_speed > 0 or self.rect.y >= 0 and self.y_speed < 0:
            self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self, self.barriers, False)
        if self.y_speed > 0: 
            for p in platforms_touched:
                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = p.rect.top
        elif self.y_speed < 0: 
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom) 
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.right, self.rect.centery,20,20, 10)
        bullets.add(bullet)         
                
                    
class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y,size_x,size_y, player_speed, direct):
        GameSprite.__init__(self, player_image, player_x, player_y,size_x,size_y)
        self.speed = player_speed
        self.direct = direct
        if self.direct == 'vert':
            self.side = 'down'
        else:
            self.side = 'left'
                    
                
    def update(self):
        if self.direct == 'hort':
            if self.rect.x<=165:
                self.side = "right"
            if self.rect.x>= win_width-390:
                self.side = "left"
            if self.side == "left":
                self.rect.x -= self.speed
            else:
                self.rect.x += self.speed

        if self.direct == 'vert':
            if self.rect.y<=100:
                self.side = "up"
            if self.rect.y>= 250:
                self.side = "down"
            if self.side == "down":
                self.rect.y -= self.speed
            else:
                self.rect.y += self.speed
#########################level2#############
        if self.direct == 'hort1':
            if self.rect.x<=350:
                self.side = "right"
            if self.rect.x>=650:
                self.side = "left"
            if self.side == "left":
                self.rect.x -= self.speed
            else:
                self.rect.x += self.speed

        elif self.direct == 'hort2':
            if self.rect.x<=120:
                self.side = "left"
            if self.rect.x>=165:
                self.side = "right"
            if self.side == "right":
                self.rect.x -= self.speed
            else:
                self.rect.x += self.speed
                                
        if self.direct == 'vert1':
            if self.rect.y<=340:
                self.side = "up"
            if self.rect.y>= 370:
                self.side = "down"
            if self.side == "down":
                self.rect.y -= self.speed
            else:
                self.rect.y += self.speed


###############level3######################


        if self.direct == 'hort3':
            if self.rect.x<=5:
                self.side = "left"
            if self.rect.x>= win_width-640:
                self.side = "right"
            if self.side == "right":
                self.rect.x -= self.speed
            else:
                self.rect.x += self.speed
                                                
        elif self.direct == 'vert2':
            if self.rect.y<=130:
                self.side = "up"
            if self.rect.y>= 240:
                self.side = "down"
            if self.side == "down":
                self.rect.y -= self.speed
            else:
                self.rect.y += self.speed

        elif self.direct == 'vert3':
            if self.rect.y<=10:
                self.side = "up"
            if self.rect.y>= 150:
                self.side = "down"
            if self.side == "down":
                self.rect.y -= self.speed
            else:
                self.rect.y += self.speed
                                            
        elif self.direct == 'vert4':
            if self.rect.y<=300:
                self.side = "up"
            if self.rect.y>= 420:
                self.side = "down"
            if self.side == "down":
               self.rect.y -= self.speed
            else:
                self.rect.y += self.speed


class Bullet(GameSprite):
    def __init__(self, player_image, player_x, player_y,size_x,size_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y,size_x,size_y)
        self.speed = player_speed

    def update(self):
        self.rect.x += self.speed
        if self.rect.x > win_width+10:
            self.kill()
                    

win_width = 700 
win_height = 500
display.set_caption('Лабіринт')
window = display.set_mode((win_width, win_height))
picture = transform.scale(image.load('fon.png'), (700,500))

w1 = GameSprite('hort.png',400,50,300, 50)
w2 = GameSprite('vert.png',120, -30, 50,400)
w3 = GameSprite('vert.png',400, 200, 50,400)

monster = Enemy('tapok.png', 450,200,70,60,6, 'vert')
monster1 = Enemy('tapok.png', 200, 250,70,60,6, 'hort')

bullets = sprite.Group()
monsters = sprite.Group()
barriers = sprite.Group()

barriers.add(w1)
barriers.add(w2)
barriers.add(w3)

monsters.add(monster)
monsters.add(monster1)

pacman = Player('cat.png',5, 60, 80,80,0,0, barriers)

final_sprite = GameSprite('final.png', win_width - 85, win_height-100,80,80)
text = GameSprite('text.png', 100,0,500,500)
########### 2 level ############
wh1 = GameSprite('hort.png',230,120,200,30)
wh2 = GameSprite('hort.png',100,300,700,30)
wh3 = GameSprite('hort.png',0,450,600,30)
wv1 = GameSprite('vert.png',100,100,30,200)
wv2 = GameSprite('vert.png',230,150,30,150)
wv3 = GameSprite('vert.png',530,120,30,180)

monster_2 = Enemy('tapok.png', 500,350,70,60,4, 'vert1')
monster2_2 = Enemy('tapok.png', 100,320,70,60,6, 'vert1')
monster1_2 = Enemy('tapok.png', 550, 20,70,60,6, 'hort1')
monster3_2 = Enemy('tapok.png', 120, 200,70,60,6, 'hort2')

bullets = sprite.Group()
monsters_2 = sprite.Group()
barriers_2 = sprite.Group()

barriers_2.add(wh1)
barriers_2.add(wh2)
barriers_2.add(wh3)
barriers_2.add(wv1)
barriers_2.add(wv2)
barriers_2.add(wv3)


monsters_2.add(monster_2)
monsters_2.add(monster1_2)
monsters_2.add(monster2_2)
monsters_2.add(monster3_2)

pacman_2 = Player('cat.png',350, 180, 80,80,0,0, barriers_2)

final_sprite_2 = GameSprite('final.png', 600, 400,80,80)

########## 3 level ###########
wh1_3 = GameSprite('hort.png',0,-10,280, 20)
wh2_3 = GameSprite('hort.png',400,-10,300, 20)
wh3_3 = GameSprite('hort.png',250,100,250, 20)
wh4_3 = GameSprite('hort.png',400,220,150, 20)
wh5_3 = GameSprite('hort.png',150,300,250, 20)
wh6_3 = GameSprite('hort.png',250,360,300, 20)
wh7_3 = GameSprite('hort.png',400,480,300, 20)
wh8_3 = GameSprite('hort.png',-20,480,300, 20)


wv1_3 = GameSprite('vert.png',140, 10, 20,400)
wv2_3 = GameSprite('vert.png',400, 10, 20,90)
wv3_3 = GameSprite('vert.png',399, 240, 20,80)
wv4_3 = GameSprite('vert.png',530, 240, 20,120)
wv5_3 = GameSprite('vert.png',-15, 0, 20,500)
wv6_3 = GameSprite('vert.png',690, 0, 20,500)


monsterv1 = Enemy('tapok.png', 250,150,70,60,6, 'vert2')
monsterv2 = Enemy('tapok.png', 500,150,70,60,6, 'vert3')
monsterv3 = Enemy('tapok.png', 60,300,70,60,6, 'vert4')
monsterh1 = Enemy('tapok.png', 50,200,70,60,6, 'hort3')

bullets = sprite.Group()
monsters_3 = sprite.Group()
barriers_3 = sprite.Group()

barriers_3.add(wh1_3)
barriers_3.add(wh2_3)
barriers_3.add(wh3_3)
barriers_3.add(wh4_3)
barriers_3.add(wh5_3)
barriers_3.add(wh6_3)
barriers_3.add(wh7_3)
barriers_3.add(wh8_3)

barriers_3.add(wv1_3)
barriers_3.add(wv2_3)
barriers_3.add(wv3_3)
barriers_3.add(wv4_3)
barriers_3.add(wv5_3)
barriers_3.add(wv6_3)


monsters_3.add(monsterh1)
monsters_3.add(monsterv1)
monsters_3.add(monsterv2)
monsters_3.add(monsterv3)

pacman_3 = Player('cat.png',300, -10, 80,80,0,0, barriers_3)

final_sprite_3 = GameSprite('final.png', 420, 0,80,80)
falsh_final_sprite = GameSprite('final.png',300,430,80,80)
falsh_final_sprite2 = GameSprite('final.png',10,10,80,80)

finish = False
run = True
a = 'level0'    

while run:
        if a == 'level0':
            window.blit(picture, (0,0))
            text.reset()
            for e in event.get():
                if e.type == QUIT:
                    run = False
                elif e.type == KEYDOWN:
                    if e.key == K_SPACE:
                        a = 'level1'

        elif a == 'level1':
            for e in event.get():
                if e.type == QUIT:
                    run = False
                elif e.type == KEYDOWN:
                    if e.key == K_LEFT:
                        pacman.x_speed = -7
                    if e.key == K_RIGHT:
                        pacman.x_speed = 7
                    if e.key == K_UP:
                        pacman.y_speed = -7
                    if e.key == K_DOWN:
                        pacman.y_speed = 7
                    if e.key == K_SPACE:
                        pacman.fire()
                        mouse.play()
                elif e.type == KEYUP:
                    if e.key == K_LEFT:
                        pacman.x_speed = 0
                    if e.key == K_RIGHT:
                        pacman.x_speed = 0
                    if e.key == K_UP:
                        pacman.y_speed = 0
                    if e.key == K_DOWN:
                        pacman.y_speed = 0
            if not finish:
                window.blit(picture, (0,0))
                pacman.reset()
                pacman.update()
                barriers.draw(window)
                final_sprite.reset()
                bullets.draw(window)
                bullets.update()


                sprite.groupcollide(monsters,bullets, True, True)
                monsters.update()
                monsters.draw(window)
                sprite.groupcollide(bullets, barriers, True, False)


                if sprite.spritecollide(pacman,monsters, False):
                    finish = True
                    mixer.music.stop()
                    img = image.load('over.png')
                    window.blit(transform.scale(img, (win_width, win_height)), (0,0))

                if sprite.collide_rect(pacman,final_sprite):
                    a = 'level2'
        elif a == 'level2':
            for e in event.get():
                if e.type == QUIT:
                    run = False
                elif e.type == KEYDOWN:
                    if e.key == K_LEFT:
                        pacman_2.x_speed = -7
                    if e.key == K_RIGHT:
                        pacman_2.x_speed = 7
                    if e.key == K_UP:
                        pacman_2.y_speed = -7
                    if e.key == K_DOWN:
                        pacman_2.y_speed = 7
                    if e.key == K_SPACE:
                        pacman_2.fire()
                        mouse.play()
                elif e.type == KEYUP:
                    if e.key == K_LEFT:
                        pacman_2.x_speed = 0
                    if e.key == K_RIGHT:
                        pacman_2.x_speed = 0
                    if e.key == K_UP:
                        pacman_2.y_speed = 0
                    if e.key == K_DOWN:
                        pacman_2.y_speed = 0
            if not finish:
                window.blit(picture, (0,0))
                pacman_2.reset()
                pacman_2.update()
                barriers_2.draw(window)
                final_sprite_2.reset()
                bullets.draw(window)
                bullets.update()


                sprite.groupcollide(monsters_2,bullets, True, True)
                monsters_2.update()
                monsters_2.draw(window)
                sprite.groupcollide(bullets, barriers_2, True, False)


                if sprite.spritecollide(pacman_2,monsters_2, False):
                    finish = True
                    mixer.music.stop()
                    img = image.load('over.png')
                    window.blit(transform.scale(img, (win_width, win_height)), (0,0))

                if sprite.collide_rect(pacman_2,final_sprite_2):
                    a = 'level3'
        elif a == 'level3':
            for e in event.get():
                if e.type == QUIT:
                    run = False
                elif e.type == KEYDOWN:
                    if e.key == K_LEFT:
                        pacman_3.x_speed = -7
                    if e.key == K_RIGHT:
                        pacman_3.x_speed = 7
                    if e.key == K_UP:
                        pacman_3.y_speed = -7
                    if e.key == K_DOWN:
                        pacman_3.y_speed = 7
                    if e.key == K_SPACE:
                        pacman_3.fire()
                        mouse.play()
                elif e.type == KEYUP:
                    if e.key == K_LEFT:
                        pacman_3.x_speed = 0
                    if e.key == K_RIGHT:
                        pacman_3.x_speed = 0
                    if e.key == K_UP:
                        pacman_3.y_speed = 0
                    if e.key == K_DOWN:
                        pacman_3.y_speed = 0
            if not finish:
                window.blit(picture, (0,0))
                pacman_3.reset()
                pacman_3.update()
                barriers_3.draw(window)
                final_sprite_3.reset()
                falsh_final_sprite.reset()
                falsh_final_sprite2.reset()
                bullets.draw(window)
                bullets.update()

                sprite.groupcollide(monsters_3,bullets, True, True)
                monsters_3.update()
                monsters_3.draw(window)
                sprite.groupcollide(bullets, barriers_3, True, False)

                if sprite.spritecollide(pacman_3,monsters_3, False):
                    finish = True
                    mixer.music.stop()
                    img = image.load('over.png')
                    window.blit(transform.scale(img, (win_width, win_height)), (0,0))

                if sprite.collide_rect(pacman_3,final_sprite_3):
                    finish = True
                    mixer.music.stop()
                    img = image.load('win.png')
                    window.blit(transform.scale(img, (win_width, win_height)), (0,0))

        time.delay(50)
        display.update()
