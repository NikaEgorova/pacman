import pygame

# музика
pygame.mixer.init()
pygame.mixer.music.load('unkown.mp3')
pygame.mixer.music.play()

#Створюємо віконце
win_width = 900
win_height = 500
pygame.display.set_caption("Лабіринт")
background = pygame.transform.scale(pygame.image.load("sea.png"), (win_width, win_height))
window = pygame.display.set_mode((win_width, win_height))

#клас-батько для інших спрайтів
class GameSprite(pygame.sprite.Sprite):
    #конструктор класу
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        # Викликаємо конструктор класу (Sprite):
        pygame.sprite.Sprite.__init__(self)

        #кожен спрайт повинен зберігати властивість image - зображення
        self.image = pygame.transform.scale(pygame.image.load(player_image), (size_x, size_y))

        #кожен спрайт повинен зберігати властивість rect - прямокутник, в який він вписаний
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    #метод, що малює героя на вікні
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#клас головного гравця
class Player(GameSprite):
    #метод, у якому реалізовано управління спрайтом за кнопками стрілочкам клавіатури
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed, player_y_speed):
        # Викликаємо конструктор класу (Sprite):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)

        self.x_speed = player_x_speed
        self.y_speed = player_y_speed
    ''' переміщає персонажа, застосовуючи поточну горизонтальну та вертикальну швидкість'''
    def update(self):
        # Спершу рух по горизонталі
        if packman.rect.x <= win_width - 80 and packman.x_speed > 0 or packman.rect.x >= 0 and packman.x_speed < 0:
            self.rect.x += self.x_speed
        # якщо зайшли за стінку, то встанемо впритул до стіни
        platforms_touched = pygame.sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0:  # йдемо праворуч, правий край персонажа - впритул до лівого краю стіни
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)  # якщо торкнулися відразу кількох, то правий край - мінімальний із можливих
        elif self.x_speed < 0:  # йдемо ліворуч, ставимо лівий край персонажа впритул до правого краю стіни
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)  # якщо торкнулися кількох стін, то лівий край - максимальний
        if packman.rect.y <= win_height - 80 and packman.y_speed > 0 or packman.rect.y >= 0 and packman.y_speed < 0:
            self.rect.y += self.y_speed
        # якщо зайшли за стінку, то встанемо впритул до стіни
        platforms_touched = pygame.sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0:  # йдемо вниз
            for p in platforms_touched:
                # Перевіряємо, яка з платформ знизу найвища, вирівнюємося по ній, запам'ятовуємо її як свою опору:
                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = p.rect.top
        elif self.y_speed < 0:  # йдемо вгору
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom)  # вирівнюємо верхній край по нижніх краях стінок, на які наїхали
    # метод "постріл" (використовуємо місце гравця, щоб створити там кулю)
    def fire(self):
        bullet = Bullet('star.png', self.rect.right, self.rect.top, 15, 20, 15)
        bullets.add(bullet)

#клас спрайту-ворога
class Enemy_h(GameSprite):
    side = "left"
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Викликаємо конструктор класу (Sprite):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed

    #рух ворога
    def update(self):
        if self.rect.x <= 460:  #w1.wall_x + w1.wall_width
            self.side = "right"
        if self.rect.x >= win_width - 85:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
          
class Enemy_h2(GameSprite):
  side = 'left'
  def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
    #Викликаємо конструктор класу (Sprite):
    GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
    self.speed = player_speed

  #рух ворога
  def update(self):
      if self.rect.x <= 200: #w1.wall_x + w1.wall_width
          self.side = 'right'
      if self.rect.x >= win_width - 320:
          self.side = 'left'
      if self.side == 'left':
          self.rect.x -= self.speed
      else:
          self.rect.x += self.speed

class Enemy_v(GameSprite):
    side = 'up'
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
      #Викликаємо конструктор класу (Sprite):
      GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
      self.speed = player_speed

    #рух ворога
    def update(self):
      if self.rect.y <= 200: #w1.wall_x + w1.wall_width
        self.side = 'down'
      if self.rect.y >= win_height - 85:
        self.side = 'up'
      if self.side == 'up':
        self.rect.y -= self.speed
      else:
        self.rect.y += self.speed

# клас спрайту-кулі
class Bullet(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Викликаємо конструктор класу (Sprite):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
    #рух ворога
    def update(self):
        self.rect.x += self.speed
        # зникає, якщо дійде до краю екрана
        if self.rect.x > win_width + 10:
            self.kill()

#Створюємо групу для стін
barriers = pygame.sprite.Group()

#створюємо групу для куль
bullets = pygame.sprite.Group()

#Створюємо групу для монстрів
monsters = pygame.sprite.Group()

#Створюємо стіни картинки
w1 = GameSprite('algae 1.png', 180, 90, 250, 60)
w2 = GameSprite('algae.png', 0, 0, 60, 250)
w3 = GameSprite('algae 1.png', 0, 245, 300, 60)
w4 = GameSprite('algae.png', 420, 0, 60, 365)
w5 = GameSprite('algae.png', 170, 400, 40, 120)
w6 = GameSprite('algae.png', 650, 160, 80, 320)

#додаємо стіни до групи
barriers.add(w1)
barriers.add(w2)
barriers.add(w3)
barriers.add(w4)
barriers.add(w5)
barriers.add(w6)

#створюємо спрайти
packman = Player('mermeid.png', 5, win_height - 80, 110, 70, 0, 0)
monster = Enemy_v('seahorse.png', win_width - 580, 210, 80, 100, 5)
monster1 = Enemy_v('seahorse.png', win_width - 377, 410, 80, 100, 5)
monster2 = Enemy_h2('octopus.png', win_width - 500, 400, 100, 100, 3)
monster3 = Enemy_h('crab.png', win_width - 120, 30, 110, 130, 9)
final_sprite = GameSprite('bag.png', win_width - 85, win_height - 100, 80, 80)
coin1 = GameSprite('key.png', 350,40, 70,50)
coin2 = GameSprite('pearl.png', 820,10, 60,50)
coins = pygame.sprite.Group()
coins.add(coin1)
coins.add(coin2)
#додаємо монстра до групи
monsters.add(monster)
monsters.add(monster1)
monsters.add(monster2)
monsters.add(monster3)
amount_coins = 0
#змінна, що відповідає за те, як закінчилася гра
finish = False
#ігровий цикл
run = True
while run:
    #цикл спрацьовує кожну 0.05 секунд
    pygame.time.delay(50)
    #перебираємо всі події, які могли статися
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                packman.x_speed = -5
            elif e.key == pygame.K_RIGHT:
                packman.x_speed = 5
            elif e.key == pygame.K_UP:
                packman.y_speed = -5
            elif e.key == pygame.K_DOWN:
                packman.y_speed = 5
            elif e.key == pygame.K_SPACE:
                packman.fire()

      
        elif e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT:
                packman.x_speed = 0
            elif e.key == pygame.K_RIGHT:
                packman.x_speed = 0
            elif e.key == pygame.K_UP:
                packman.y_speed = 0
            elif e.key == pygame.K_DOWN:
                packman.y_speed = 0

#перевірка, що гра ще не завершена
    if not finish:
        #оновлюємо фон кожну ітерацію
        window.blit(background, (0,0))

        #запускаємо рухи спрайтів
        packman.update()
        bullets.update()

        #оновлюємо їх у новому місці при кожній ітерації циклу
        packman.reset()
        #рисуємо стіни 2
        bullets.draw(window)
        barriers.draw(window)
        final_sprite.reset()
        coins.draw(window)
        if pygame.sprite.spritecollide(packman, coins, True):
            amount_coins += 1

        pygame.sprite.groupcollide(monsters, bullets, True, True)
        monsters.update()
        monsters.draw(window)
        pygame.sprite.groupcollide(bullets, barriers, True, False)

        #Перевірка зіткнення героя з ворогом та стінами
        if pygame.sprite.spritecollide(packman, monsters, False):
            finish = True
            # обчислюємо ставлення
            pygame.mixer.music.stop()
            pygame.mixer.init()
            pygame.mixer.music.load('lose.ogg')
            pygame.mixer.music.play()
            img = pygame.image.load('game-over.png')
            d = img.get_width() // img.get_height()
            window.fill((255, 255, 255))
            window.blit(pygame.transform.scale(img, (win_width, win_height)), (0, 0))

        if pygame.sprite.collide_rect(packman, final_sprite) and amount_coins == 2:
            finish = True
            pygame.mixer.music.stop()
            pygame.mixer.init()
            pygame.mixer.music.load('win.ogg')
            pygame.mixer.music.play()
            img = pygame.image.load('finish.png')
            window.fill((255, 255, 255))
            window.blit(pygame.transform.scale(img, (win_width, win_height)), (0, 0))

    pygame.display.update()
