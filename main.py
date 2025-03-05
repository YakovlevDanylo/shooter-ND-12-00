from random import randint

from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, image_name, x, y, width, height, speed):
        super().__init__()
        self.image = transform.scale(image.load(image_name), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):

    def update(self, screen):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 630:
            self.rect.x += self.speed

    def fire(self):
        bullet = Bullet("bullet.png", self.rect.centerx, self.rect.top, 15, 20, 15)
        bullets.add(bullet)
class Enemy(GameSprite):

     def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y >= 400:
            lost += 1
            self.rect.x = randint(0, 600)
            self.rect.y = 0
            self.speed = randint(1, 3)

class Bullet(GameSprite):

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()


lost = 0

bullets = sprite.Group()
enemies = sprite.Group()
for i in range(5):
    enemy = Enemy("ufo.png", randint(0, 600), 0, 80, 50, randint(1, 3))
    enemies.add(enemy)

window = display.set_mode((700, 500))
display.set_caption("Шутер")

background = transform.scale(image.load("galaxy.jpg"), (700, 500))
player = Player("rocket.png", 5, 400, 70,100, 10)
clock = time.Clock()
fps = 60

mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()

finish = False
run = True
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

        if e.type == KEYDOWN and e.key == K_SPACE:
            player.fire()


    window.blit(background, (0, 0))

    player.update(window)
    player.reset(window)

    enemies.update()
    enemies.draw(window)

    bullets.update()
    bullets.draw(window)

    display.update()
    clock.tick(fps)
